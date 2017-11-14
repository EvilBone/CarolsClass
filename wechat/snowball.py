import logging
import re
from math import floor

import requests
import simplejson
from bs4 import BeautifulSoup as bsp

from wechat.article import Article, User, Stock
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CarolsClass.settings")
django.setup()
from wechat.models import MUser, MArticle, MStock

logger = logging.getLogger(__name__)

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
           "Cache-Control": "max-age=0",
           "Connection": "keep-alive",
           "Cookie": "device_id=67d4d66c3a9d3abedc793b08d34f8d37; aliyungf_tc=AQAAADhn2gNHMAwAdxVtcfj4DOtMUCHl; remember=1; remember.sig=K4F3faYzmVuqC0iXIERCQf55g2Y; xq_a_token=0e929442f3f54b7c60ec13a9fb46796e8808a5ca; xq_a_token.sig=M_WTO0z1W9gX80t4hjtiU06h1iQ; xq_r_token=fc261bfc3c49d86b8374c563ae1f39600cfb277d; xq_r_token.sig=acSZhW9ni2QwlVLNfLQEXcH_CRQ; xq_is_login=1; xq_is_login.sig=J3LxgPVPUzbBg3Kee_PquUfih7Q; u=2125465036; u.sig=nHm_EvrF1GFLjXz891QT-YNA_-0; s=eb125afxye; bid=c39cf376a8f6bfa40b2d1a5ee4f12525_j9ihq748; Hm_lvt_1db88642e346389874251b5a1eded6e3=1508075470,1509628322; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1509628329",
           "Host": "xueqiu.com",
           "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"}


def get_friends(users, user_id, page):
    url = 'https://xueqiu.com/friendships/groups/members.json'
    params = {"uid": user_id, "page": page, "gid": "0"}
    try:
        resp = requests.get(url=url, headers=headers, params=params)
        raw_content = resp.text
        # print(raw_content)
        json_content = simplejson.loads(raw_content)
        json_users = json_content["users"]
        for json_user in json_users:
            user = User()
            user.user_id = json_user["id"]
            user.user_name = json_user["screen_name"]
            user.user_description = json_user["description"]
            user.user_follower_counts = json_user["followers_count"]
            user.user_friends_count = json_user["friends_count"]
            user.user_gender = json_user["gender"]
            user.user_province = json_user["province"]
            users.append(user)
        page_count = json_content["maxPage"]
        page += 1
        if page <= page_count:
            get_friends(users, user_id, page)
    except Exception as e:
        logger.error(e)

    return users


def get_stocks_hs(stocks=[], page=1, pages=61):
    # print("page: %d" % page)
    stockurl = 'https://xueqiu.com/stock/cata/stocklist.json'
    try:
        params = {'page': page, "size": 90, "order": "desc", "orderby": "percent", "type": "11,12"}
        resp = requests.get(stockurl, headers=headers, params=params)
        raw_cotent = resp.text
        json_content = simplejson.loads(raw_cotent)
        count = json_content["count"]
        # stock_count = count["count"]
        json_stocks = json_content["stocks"]
        # print("json_stocks: %d" %len(json_stocks))
        for json_stock in json_stocks:
            stock = Stock()
            stock.stock_symbol = json_stock["symbol"]
            stock.stock_code = json_stock["code"]
            stock.stock_name = json_stock["name"]
            stock.stock_cprice = json_stock["current"]
            stock.stock_mprice = json_stock["high"]
            stock.stock_low_price = json_stock["low"]
            stock.stock_amount_moneny = json_stock["amount"]
            stock.stock_amount_qty = json_stock["volume"]
            stock.stock_pbv = json_stock["pettm"]
            stock.stock_change = json_stock["change"]
            stock.stock_high52w = json_stock["high52w"]
            stock.stock_low52w = json_stock["low52w"]
            stock.stock_marketcapital = json_stock["marketcapital"]
            stock.stock_percent = json_stock["percent"]
            stock.stock_market = '沪深'
            stocks.append(stock)
        page += 1
        if page <= pages:
            stocks = get_stocks_hs(stocks=stocks, page=page, pages=pages)
    except Exception as e:
        logger.error(e)
    return stocks


def get_article(url):
    resp = requests.get(url=url, headers=headers)
    soup = bsp(resp.text, 'lxml')
    article = Article()
    article.article_title = soup.find('h1', class_='article__bd__title').text
    article.article_content = soup.find('div', class_='article__bd__detail').text
    article.article_author = soup.find('a', class_='name').text
    article.article_author_id = soup.find('a', class_='name').get('href').replace('/', '')
    article.articl_url = url
    return article

def get_stock_hs(stockid):

    try:
        stock = Stock()
        url = 'https://xueqiu.com/S/'+stockid
        resp = requests.get(url=url,headers=headers)
        soup = bsp(resp.text,'lxml')
        stock.stock_symbol = stockid
        stock.stock_code = stockid[-1:-6]
        stock.stock_pbv= soup.find(text=re.compile("市净率")).parent.find('span').text
        stock.stock_assets = soup.find(text=re.compile("每股净资产")).parent.find('span').text
        stock.stock_profit = soup.find(text=re.compile("每股收益")).parent.find('span').text
        stock.stock_desc = soup.find(class_='widget-content stock-profile').text
        stock.stock_business = soup.findAll(class_='widget-content')[-1].text
    except Exception as e:
        print("%s " % stockid)

    return stock

def update_stocks():
    mstocks  = MStock.objects.all()
    for mstock in mstocks:
        stock = get_stock_hs(mstock.stock_symbol)
        mstock.stock_pbv = 0 if stock.stock_pbv=='' or  stock.stock_pbv=='-' else stock.stock_pbv
        mstock.stock_assets = 0 if stock.stock_assets=='' or  stock.stock_assets=='-' else stock.stock_assets
        mstock.stock_profit = 0 if stock.stock_profit=='' or  stock.stock_profit=='-' else  stock.stock_profit
        mstock.stock_desc = stock.stock_desc
        mstock.stock_business = stock.stock_business
        mstock.save()

def save_to_stocks(stocks):
    for stock in stocks:
        print("stock : %s" % stock.stock_symbol)
        try:
            if not MStock.objects.filter(stock_symbol=stock.stock_symbol).exists():
                mstock = MStock()
                mstock.stock_symbol = stock.stock_symbol
                mstock.stock_code = stock.stock_code
                mstock.stock_name = stock.stock_name
                mstock.stock_mprice = stock.stock_mprice
                mstock.stock_lowprice = stock.stock_low_price
                mstock.stock_cprice = stock.stock_cprice
                mstock.stock_amount_qty = 0 if stock.stock_amount_qty == ''  else stock.stock_amount_qty
                mstock.stock_amount_moneny = 0 if stock.stock_amount_moneny == '' else stock.stock_amount_moneny
                mstock.stock_market = stock.stock_market
                mstock.stock_52lowprice = stock.stock_low52w
                mstock.stock_52mprice = stock.stock_high52w
                mstock.stock_stock_marketcapital = 0 if stock.stock_marketcapital == '' else stock.stock_marketcapital
                mstock.stock_pbv = 0 if stock.stock_pbv == '' else stock.stock_pbv
                mstock.stock_change = 0 if stock.stock_change =='' else stock.stock_change
                mstock.stock_percent = 0 if stock.stock_percent=='' else stock.stock_percent
                mstock.save()
            else:
                mstock = MStock.objects.get(stock_symbol=stock.stock_symbol)
                mstock.stock_mprice = stock.stock_mprice
                mstock.stock_lowprice = stock.stock_low_price
                mstock.stock_cprice = stock.stock_cprice
                mstock.stock_amount_qty = 0 if stock.stock_amount_qty == '' else stock.stock_amount_qty
                mstock.stock_amount_moneny = 0 if stock.stock_amount_moneny == '' else stock.stock_amount_moneny
                mstock.stock_52lowprice = stock.stock_low52w
                mstock.stock_52mprice = stock.stock_high52w
                mstock.stock_stock_marketcapital = 0 if stock.stock_marketcapital == '' else stock.stock_marketcapital
                mstock.stock_pbv = 0 if stock.stock_pbv == '' else stock.stock_pbv
                mstock.stock_change = 0 if stock.stock_change == '' else stock.stock_change
                mstock.stock_percent = 0 if stock.stock_percent == '' else stock.stock_percent
                mstock.stock_market = stock.stock_market
                mstock.save()
        except Exception as e:
            logger.error(e)
    return 1


def save_to_users(users):
    musers = []
    for user in users:
        if not MUser.objects.filter(user_id=user.user_id).exists():
            m_user = MUser()
            m_user.user_id = user.user_id
            m_user.user_province = user.user_province
            m_user.user_friends_count = user.user_friends_count
            m_user.user_follower_counts = user.user_follower_counts
            m_user.user_description = user.user_description
            m_user.user_name = user.user_name
            m_user.user_gender = user.user_gender
            m_user.user_is_deal = False
            musers.append(m_user)
    if len(musers) > 0:
        MUser.objects.bulk_create(musers)
    return len(musers)

def save_to_his():
    stocks = MStock.objects.all()
    for stock in stocks:
        hstock = MStock_His()
        hstock.his_stock_52lowprice = stock.stock_52lowprice
        hstock.his_stock_52mprice = stock.stock_52mprice
        hstock.his_stock_amount_moneny = stock.stock_amount_moneny
        hstock.his_stock_amount_qty = stock.stock_amount_qty
        hstock.his_stock_assets = stock.stock_assets
        hstock.his_stock_change = stock.stock_change
        hstock.his_stock_code = stock.stock_code
        hstock.his_stock_cprice = stock.stock_cprice
        hstock.his_stock_dividend = stock.stock_dividend
        hstock.his_stock_followers_count = stock.stock_followers_count
        hstock.his_stock_lowprice = stock.stock_lowprice
        hstock.his_stock_lprice = stock.stock_lprice
        hstock.his_stock_mprice = stock.stock_mprice
        hstock.his_stock_pbv = stock.stock_pbv
        hstock.his_stock_pe = stock.stock_pe
        hstock.his_stock_name = stock.stock_name
        hstock.his_stock_business = stock.stock_business
        hstock.his_stock_desc = stock.stock_desc
        hstock.his_stock_market = stock.stock_market
        hstock.his_stock_percent = stock.stock_percent
        hstock.his_stock_profit = stock.stock_profit
        hstock.his_stock_stock_marketcapital = stock.stock_stock_marketcapital
        hstock.his_stock_symbol = stock.stock_symbol
        hstock.save()

if __name__ == '__main__':
    print("task spider_stocks Start...")
    # stocks = get_stocks_hs()
    # save_to_stocks(stocks=stocks)
    update_stocks()
    print("task spider_stocks End...")
    print("task save_his Start...")
    save_to_his()
    print("task save_his End...")
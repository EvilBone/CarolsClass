import re
import requests
import simplejson
from bs4 import  BeautifulSoup as bsp

from wechat.article import Article, User, Stock
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CarolsClass.settings")
django.setup()
from wechat.models import MUser, MArticle, MStock

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
           "Cache-Control": "max-age=0",
           "Connection": "keep-alive",
           "Cookie": "device_id=67d4d66c3a9d3abedc793b08d34f8d37; aliyungf_tc=AQAAADhn2gNHMAwAdxVtcfj4DOtMUCHl; remember=1; remember.sig=K4F3faYzmVuqC0iXIERCQf55g2Y; xq_a_token=0e929442f3f54b7c60ec13a9fb46796e8808a5ca; xq_a_token.sig=M_WTO0z1W9gX80t4hjtiU06h1iQ; xq_r_token=fc261bfc3c49d86b8374c563ae1f39600cfb277d; xq_r_token.sig=acSZhW9ni2QwlVLNfLQEXcH_CRQ; xq_is_login=1; xq_is_login.sig=J3LxgPVPUzbBg3Kee_PquUfih7Q; u=2125465036; u.sig=nHm_EvrF1GFLjXz891QT-YNA_-0; s=eb125afxye; bid=c39cf376a8f6bfa40b2d1a5ee4f12525_j9ihq748; Hm_lvt_1db88642e346389874251b5a1eded6e3=1508075470,1509628322; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1509628329",
           "Host": "xueqiu.com",
           "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"}

def get_friends(users,user_id,page):
    url = 'https://xueqiu.com/friendships/groups/members.json'
    params = { "uid":user_id,"page":page,"gid":"0"}
    resp = requests.get(url=url, headers=headers,params=params)
    raw_content = resp.text
    # print(raw_content)
    json_content = simplejson.loads(raw_content)
    json_users = json_content["users"]
    for json_user in json_users:
        user = User()
        user.user_id=json_user["id"]
        user.user_name=json_user["screen_name"]
        user.user_description=json_user["description"]
        user.user_follower_counts = json_user["followers_count"]
        user.user_friends_count = json_user["friends_count"]
        user.user_gender = json_user["gender"]
        user.user_province = json_user["province"]
        users.append(user)
    page_count = json_content["maxPage"]
    page += 1
    if page<=page_count:
        get_friends(users,user_id,page)
    return users

def get_stocks(stock_id):
    stockurl = "https://xueqiu.com/S/"+stock_id
    print(stock_id+" : "+stockurl)
    resp = requests.get(stockurl,headers=headers)
    soup = bsp(resp.text,'lxml')
    stock = Stock()
    try:
        stock.stock_code = stockurl.split('/')[-1]
        stock.stock_name = soup.find('span',class_='stockName').text
        stock.stock_cprice = soup.find('div',class_='currentInfo').find("strong").get("data-current")
        stock.stock_lprice = soup.find(text=re.compile("昨收")).parent.find('span').text
        stock.stock_mprice = soup.find(text=re.compile("最高")).parent.find('span').text
        stock.stock_low_price = soup.find(text=re.compile("最低")).parent.find('span').text
        stock.stock_amount_moneny = soup.find(text=re.compile("成交额")).parent.find('span').text
        stock.stock_amount_qty = soup.find(text=re.compile("成交量")).parent.find('span').text
        stock.stock_pbv = soup.find(text=re.compile("市盈率")).parent.find('span').text
        stock.stock_pe = soup.find(text=re.compile("市净率")).parent.find('span').text
        stock.stock_dividend = soup.find(text=re.compile("每股股息：")).parent.find('span').text
        stock.stock_assets = soup.find(text=re.compile("每股净资产：")).parent.find('span').text
        stock.stock_profit = soup.find(text=re.compile("每股收益：")).parent.find('span').text
        stock.stock_desc = soup.find("p",class_='companyInfo detailContent').text
        stock.stock_business = soup.find('strong',class_ = 'title',text=re.compile("业务")).parent.text
        stock.stock_followers_count = soup.find('a',id='followsCount')
    except:
        print("异常")
    return stock


def get_article(url):
    resp = requests.get(url=url,headers=headers)
    soup = bsp(resp.text,'lxml')
    article = Article()
    article.article_title = soup.find('h1',class_='article__bd__title').text
    article.article_content = soup.find('div',class_='article__bd__detail').text
    article.article_author = soup.find('a',class_='name').text
    article.article_author_id = soup.find('a', class_='name').get('href').replace('/','')
    article.articl_url = url
    return article

def get_users_stock(user_id):
    url = 'https://xueqiu.com/v4/stock/portfolio/stocks.json'
    params = {'size':1000,"type":1,"category":2,"uid":user_id}
    resp = requests.get(url=url,headers=headers,params=params)
    raw_content = resp.text
    json_content = simplejson.loads(raw_content)
    json_stocks = json_content['stocks']
    c_stocks = []
    for j_stock in json_stocks:
        stock_id= j_stock["code"]
        c_stock = get_stocks(stock_id)
        c_stocks.append(c_stock)
    return c_stocks

def save_to_stocks(stocks):
    mstocks  = []
    for stock in stocks:
        if not MStock.objects.filter(stock_code=stock.stock_code).exists():
            try:
                mstock = MStock()
                mstock.stock_code = stock.stock_code
                mstock.stock_name = stock.stock_name
                mstock.stock_followers_count = stock.stock_followers_count
                mstock.stock_business = stock.stock_business
                mstock.stock_desc = stock.stock_desc
                mstock.stock_profit = stock.stock_profit
                mstock.stock_assets = stock.stock_assets
                mstock.stock_dividend = stock.stock_dividend
                mstock.stock_pbv = stock.stock_pbv
                mstock.stock_lprice = stock.stock_lprice
                mstock.stock_mprice = stock.stock_mprice
                mstock.stock_low_price = stock.stock_low_price
                mstock.stock_cprice = stock.stock_cprice
                mstock.stock_amount_qty = stock.stock_amount_qty
                mstock.stock_amount_moneny = stock.stock_amount_moneny
                mstock.save()
            except:
                print("保存异常")
            mstocks.append(mstock)
    # if len(mstocks)>0:
        # MStock.objects.bulk_create(mstocks)
    return len(mstocks)

def save_to_users(users):
    musers = []
    for user in users:
        if not MUser.objects.filter(user_id=user.user_id).exists():
            m_user= MUser()
            m_user.user_id = user.user_id
            m_user.user_province = user.user_province
            m_user.user_friends_count = user.user_friends_count
            m_user.user_follower_counts = user.user_follower_counts
            m_user.user_description = user.user_description
            m_user.user_name = user.user_name
            m_user.user_gender = user.user_gender
            m_user.user_is_deal = False
            musers.append(m_user)
            stocks = get_users_stock(m_user.user_id)
            count = save_to_stocks(stocks)
            print("用户名 %s, 股票数 %s"% (user.user_name,count))
    if len(musers)>0:
        MUser.objects.bulk_create(musers)
    return len(musers)

if __name__ == '__main__':
    # url = 'https://xueqiu.com/S/SH600846'
    # get_stocks(url)
    musers = MUser.objects.all()
    if len(musers)==0:
        users = []
        users=get_friends(users,'3037882447',1)
        save_to_users(users)
    else:
        while True:
            f_users =  MUser.objects.filter(user_is_deal=False)
            if len(f_users)>0:
                for f_user in f_users:
                    users = []
                    users = get_friends(users, f_user.user_id, 1)
                    save_to_users(users)
                    f_user.user_is_deal=True
                    f_user.save()
                    print(f_user.user_name)
                else:
                    exit()
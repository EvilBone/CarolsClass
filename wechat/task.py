from wechat.mylog import logging

from celery import task, platforms

from wechat.models import MUser, MStock, MStock_His
from wechat.snowball import get_friends, save_to_users, get_users_stock, save_to_stocks, get_stocks

logger = logging.getLogger('task')
platforms.C_FORCE_ROOT = True
@task
def spider_users():

    logger.info("task spider_users Start...")
    musers = MUser.objects.all()
    # MUser.objects.filter(user_is_deal=False)
    if len(musers) == 0:
        users = []
        users = get_friends(users, '3037882447', 1)
        save_to_users(users)
    else:
        while True:
            f_users = MUser.objects.filter(user_is_deal=False)
            if len(f_users) > 0:
                for f_user in f_users:
                    users = []
                    users = get_friends(users, f_user.user_id, 1)
                    save_to_users(users)
                    f_user.user_is_deal = True
                    f_user.save()
                    print(f_user.user_name)
                else:
                    exit()
    logger.info("task spider_users End...")

@task
def spider_stocks():
    logger.info("task spider_stocks Start...")
    stocks = get_stocks()
    save_to_stocks(stocks=stocks)
    logger.info("task spider_stocks End...")

@task
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

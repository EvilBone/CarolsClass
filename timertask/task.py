import time

from wechat.mylog import logging

from celery import task, platforms

from wechat.models import MUser, MStock, MStock_His
from wechat.snowball import get_friends, save_to_users, save_to_stocks, update_stocks, \
    get_stocks_hs
from timertask.models import MScheLog, MSche, MTask

logger = logging.getLogger('task')
platforms.C_FORCE_ROOT = True


@task
def spider_users():
    mslog = MScheLog()
    mslog.ms_task = MTask.objects.get(task_name='SpiderUsers')
    mslog.ms_start_time = time.time()
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
    mslog.ms_end_time = time.time()
    mslog.ms_message='Success!'
    mslog.save()

@task
def spider_stocks():
    mslog = MScheLog()
    mslog.ms_task = MTask.objects.get(task_name='SpiderStocks')
    mslog.ms_start_time = time.time()
    stocks = get_stocks_hs()
    save_to_stocks(stocks=stocks)
    update_stocks()
    mslog.ms_end_time = time.time()
    mslog.ms_message='Success!'
    mslog.save()


@task
def save_to_his():
    mslog = MScheLog()
    mslog.ms_task = MTask.objects.get(task_name='SpiderStocks')
    mslog.ms_start_time = time.time()
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
    mslog.ms_end_time = time.time()
    mslog.ms_message = 'Success!'
    mslog.save()

from wechat.mylog import logging

from celery import task, platforms

from wechat.models import MUser
from wechat.snowball import get_friends, save_to_users, get_users_stock, save_to_stocks

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
    musers = MUser.objects.all()
    if len(musers) != 0:
        for muser in musers:
            stocks = get_users_stock(muser.user_id)
            save_to_stocks(stocks=stocks)
    logger.info("task spider_stocks End...")
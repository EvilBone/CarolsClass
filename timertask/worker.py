# coding=utf-8
"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""
import time
import os

import django
import sys
from apscheduler.schedulers.background import BackgroundScheduler
sys.path.append(r'/root/CarolsClass')
sys.path.append(r'/root/CarolsClass/timertask')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CarolsClass.settings")
django.setup()
from timertask.task import spider_stocks, spider_users, save_to_his

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    # scheduler.add_job(tick, 'interval', seconds=3)
    # scheduler.add_job(tick, 'date', run_date='2016-02-14 15:01:05')
    scheduler.add_job(spider_stocks, 'cron', hour='16',minute ='30')
    scheduler.add_job(spider_users, 'cron', hour='22', minute='30')
    scheduler.add_job(save_to_his, 'cron', hour='17', minute='00')
    '''
        year (int|str) – 4-digit year
        month (int|str) – month (1-12)
        day (int|str) – day of the (1-31)
        week (int|str) – ISO week (1-53)
        day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
        hour (int|str) – hour (0-23)
        minute (int|str) – minute (0-59)
        second (int|str) – second (0-59)

        start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
        end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
        timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)

        *    any    Fire on every value
        */a    any    Fire every a values, starting from the minimum
        a-b    any    Fire on any value within the a-b range (a must be smaller than b)
        a-b/c    any    Fire every c values within the a-b range
        xth y    day    Fire on the x -th occurrence of weekday y within the month
        last x    day    Fire on the last occurrence of weekday x within the month
        last    day    Fire on the last day within the month
        x,y,z    any    Fire on any matching expression; can combine any number of any of the above expressions
    '''
    scheduler.start()  # 这里的调度任务是独立的一个线程
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)  # 其他任务是独立的线程执行
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
        print('Exit The Job!')
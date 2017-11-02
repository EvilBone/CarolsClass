from celery import task

from wechat.models import MUser
from wechat.snowball import get_friends, save_to_users


@task
def spider_users():
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
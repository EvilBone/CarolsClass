import requests
import simplejson
from bs4 import  BeautifulSoup as bsp

from wechat.article import Article, User
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CarolsClass.settings")
django.setup()
from wechat.models import MUser,MArticle

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
    print(raw_content)
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
    MUser.objects.bulk_create(musers)

if __name__ == '__main__':
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
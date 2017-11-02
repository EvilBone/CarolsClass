

class Article:

    def __init__(self,title='',content='',author='',url='',author_id=''):
        self.article_title = title
        self.article_content = content
        self.article_author = author
        self.article_author_id = author_id
        self.article_url = url

    def __str__(self):
        return 'Article (%s, %s, %s, %s, %s)' % (self.article_title,self.article_author,self.article_author_id,self.article_url, self.article_content)

class User:
    def __init__(self,id ='',name='',description='',followers_count='',friends_count='',gender='',province='',stocks_count=''):
        self.user_id = id
        self.user_name = name
        self.user_description = description
        self.user_follower_counts = followers_count
        self.user_friends_count = friends_count
        self.user_gender = gender
        self.user_province = province
        self.user_stocks_count = stocks_count

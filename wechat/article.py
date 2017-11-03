class Article:
    def __init__(self, title='', content='', author='', url='', author_id=''):
        self.article_title = title
        self.article_content = content
        self.article_author = author
        self.article_author_id = author_id
        self.article_url = url

    def __str__(self):
        return 'Article (%s, %s, %s, %s, %s)' % (
        self.article_title, self.article_author, self.article_author_id, self.article_url, self.article_content)

class User:
    def __init__(self, id='', name='', description='', followers_count='', friends_count='', gender='', province='',
                 stocks_count=''):
        self.user_id = id
        self.user_name = name
        self.user_description = description
        self.user_follower_counts = followers_count
        self.user_friends_count = friends_count
        self.user_gender = gender
        self.user_province = province
        self.user_stocks_count = stocks_count


class Stock:
    def __init__(self, code='', name='', cprice=0, lprice=0, followers_count=0, mprice=0, low_price=0, amount_qty=0,
                 amount_moneny=0,description='', business='', pbv=0, pe=0, profit=0, assets=0,
                 dividend=0):
        self.stock_code = code
        self.stock_name = name
        self.stock_cprice = cprice
        self.stock_lprice = lprice
        self.stock_followers_count = followers_count
        self.stock_mprice = mprice
        self.stock_low_price = low_price
        self.stock_amount_qty = amount_qty
        self.stock_amount_moneny = amount_moneny
        self.stock_desc = description
        self.stock_business = business
        self.stock_pbv = pbv
        self.stock_pe = pe
        self.stock_profit = profit
        self.stock_assets = assets
        self.stock_dividend = dividend

    def stock_amplitude(self):
        if self.stock_lprice != 0:
            amplitude = (self.stock_mprice-self.stock_low_price)/self.stock_lprice
        else:
            amplitude=0
        return round(amplitude,2)

    def stock_increase(self):
        if self.stock_lprice != 0:
            amplitude = (self.stock_cprie-self.stock_lprice)/self.stock_lprice
        else:
            amplitude=0
        return round(amplitude,2)

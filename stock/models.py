from django.db import models

# Create your models here.


class MUser(models.Model):
    user_id = models.CharField(max_length=20,verbose_name='id')
    user_name = models.CharField(max_length=100,verbose_name='名称',default='',blank=True,null=True)
    user_description = models.TextField(max_length=500,verbose_name='描述',default='',blank=True,null=True)
    user_follower_counts = models.IntegerField(verbose_name='粉丝数')
    user_friends_count = models.IntegerField(verbose_name='关注数')
    user_gender = models.CharField(max_length=2,verbose_name='性别',blank=True,null=True,default='')
    user_province = models.CharField(max_length=20,verbose_name='省份',blank=True,null=True)
    user_stocks_count = models.IntegerField(verbose_name='股票数',blank=True,null=True,default=0)
    user_is_deal = models.BooleanField(verbose_name='是否处理',default=False)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = "用户"

class MStock(models.Model):
    stock_symbol = models.CharField(max_length=10,verbose_name='股票编码',null=True,blank=True,unique=True)
    stock_code = models.CharField(max_length=10,verbose_name='股票代码',null=True,blank=True)
    stock_name = models.CharField(max_length=50,verbose_name='股票名称',null=True,blank=True)
    stock_market = models.CharField(max_length=10,verbose_name='所属市场',null=True,blank=True)
    stock_cprice = models.FloatField(verbose_name='当前价格',null=True,blank=True)
    stock_lprice = models.FloatField(verbose_name='昨收价格',null=True,blank=True)
    stock_followers_count = models.IntegerField(verbose_name='关注人数',null=True,blank=True)
    stock_mprice = models.FloatField(verbose_name='最高价格',null=True,blank=True)
    stock_lowprice = models.FloatField(verbose_name='最低价格',null=True,blank=True)
    stock_52mprice = models.FloatField(verbose_name='52周最高价',null=True,blank=True)
    stock_52lowprice = models.FloatField( verbose_name='52周最高价', null=True, blank=True)
    stock_amount_qty = models.FloatField(verbose_name='成交量',null=True,blank=True)
    stock_amount_moneny = models.FloatField(verbose_name='成交额',null=True,blank=True)
    stock_desc = models.TextField(verbose_name='简介',null=True,blank=True)
    stock_business = models.TextField(verbose_name='业务',null=True,blank=True)
    stock_pbv = models.FloatField(verbose_name='市盈率',null=True,blank=True)
    stock_pe = models.FloatField(verbose_name='市净率',null=True,blank=True)
    stock_profit = models.FloatField(verbose_name='每股收益',null=True,blank=True)
    stock_assets = models.FloatField(verbose_name='每股资产',null=True,blank=True)
    stock_dividend = models.FloatField(verbose_name='每股股息',null=True,blank=True)
    stock_stock_marketcapital = models.FloatField(verbose_name='市值',null=True,blank=True)
    stock_change = models.FloatField(verbose_name='涨跌额',null=True,blank=True)
    stock_percent = models.FloatField(verbose_name='涨跌幅',null=True,blank=True)
    stock_update_datetime = models.DateTimeField(verbose_name='更新时间',blank=True,null=True,auto_now=True)

    class Meta:
        verbose_name = '股票'
        verbose_name_plural = "股票"

class MStock_His(models.Model):
    his_stock_symbol = models.CharField(max_length=10, verbose_name='股票编码', null=True, blank=True)
    his_stock_code = models.CharField(max_length=10, verbose_name='股票代码', null=True, blank=True)
    his_stock_name = models.CharField(max_length=50, verbose_name='股票名称', null=True, blank=True)
    his_stock_market = models.CharField(max_length=10, verbose_name='所属市场', null=True, blank=True)
    his_stock_cprice = models.FloatField(verbose_name='当前价格', null=True, blank=True)
    his_stock_lprice = models.FloatField(verbose_name='昨收价格', null=True, blank=True)
    his_stock_followers_count = models.IntegerField(verbose_name='关注人数', null=True, blank=True)
    his_stock_mprice = models.FloatField(verbose_name='最高价格', null=True, blank=True)
    his_stock_lowprice = models.FloatField(verbose_name='最低价格', null=True, blank=True)
    his_stock_52mprice = models.FloatField(verbose_name='52周最高价', null=True, blank=True)
    his_stock_52lowprice = models.FloatField(verbose_name='52周最高价', null=True, blank=True)
    his_stock_amount_qty = models.FloatField(verbose_name='成交量', null=True, blank=True)
    his_stock_amount_moneny = models.FloatField(verbose_name='成交额', null=True, blank=True)
    his_stock_desc = models.TextField(verbose_name='简介', null=True, blank=True)
    his_stock_business = models.TextField(verbose_name='业务', null=True, blank=True)
    his_stock_pbv = models.FloatField(verbose_name='市盈率', null=True, blank=True)
    his_stock_pe = models.FloatField(verbose_name='市净率', null=True, blank=True)
    his_stock_profit = models.FloatField(verbose_name='每股收益', null=True, blank=True)
    his_stock_assets = models.FloatField(verbose_name='每股资产', null=True, blank=True)
    his_stock_dividend = models.FloatField(verbose_name='每股股息', null=True, blank=True)
    his_stock_marketcapital = models.FloatField(verbose_name='市值', null=True, blank=True)
    his_stock_change = models.FloatField(verbose_name='涨跌额', null=True, blank=True)
    his_stock_percent = models.FloatField(verbose_name='涨跌幅', null=True, blank=True)
    his_stock_date = models.DateField(verbose_name='日期',null=True,blank=True,auto_now_add=True)

    class Meta:
        verbose_name = '股票历史'
        verbose_name_plural = "股票历史"

class MArticle(models.Model):
    article_title = models.CharField(max_length=400,verbose_name='标题')
    article_content = models.TextField(verbose_name='内容')
    article_author = models.CharField(max_length=100,verbose_name='作者')
    article_author_id = models.CharField(max_length=20,verbose_name='作者id')
    article_url = models.URLField(verbose_name='文章地址')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = "文章"

from django.contrib import admin
from .models import MUser, MStock


# Register your models here.

class MUserAdmin(admin.ModelAdmin):
    list_display = (
    'user_id', 'user_name', 'user_description', 'user_follower_counts', 'user_friends_count', 'user_gender',
    'user_province', 'user_stocks_count', 'user_is_deal')
    search_fields = ('user_name',)
    list_filter = ('user_is_deal',)


class MStockAdmin(admin.ModelAdmin):
    list_display = (
    'stock_symbol', 'stock_code', 'stock_name', 'stock_cprice','stock_percent','stock_change', 'stock_lowprice', 'stock_mprice', 'stock_lowprice',
    'stock_amount_qty', 'stock_amount_moneny', 'stock_market', 'stock_stock_marketcapital','stock_52lowprice','stock_52mprice')
    search_fields = ('stock_code', 'stock_name')
    list_filter = ('stock_market',)


admin.site.register(MUser, MUserAdmin)
admin.site.register(MStock, MStockAdmin)

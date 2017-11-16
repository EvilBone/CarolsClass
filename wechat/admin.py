from django.contrib import admin
from .models import MUser, MStock, MStock_His


# Register your models here.

class MUserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', 'user_name', 'user_description', 'user_follower_counts', 'user_friends_count', 'user_gender',
        'user_province', 'user_stocks_count', 'user_is_deal')
    search_fields = ('user_name',)
    list_filter = ('user_is_deal',)


class MStockAdmin(admin.ModelAdmin):
    list_display = (
        'stock_symbol', 'stock_code', 'stock_name', 'stock_cprice', 'stock_percent', 'stock_change', 'stock_lowprice',
        'stock_mprice', 'stock_lowprice',
        'stock_amount_qty', 'stock_amount_moneny', 'stock_market', 'stock_stock_marketcapital', 'stock_52lowprice',
        'stock_52mprice','stock_update_datetime')
    search_fields = ('stock_code', 'stock_name')
    list_filter = ('stock_market',)


class HisMStockAdmin(admin.ModelAdmin):
    list_display = ('his_stock_date',
        'his_stock_symbol', 'his_stock_code', 'his_stock_name', 'his_stock_cprice', 'his_stock_percent',
        'his_stock_change', 'his_stock_lowprice', 'his_stock_mprice', 'his_stock_lowprice',
        'his_stock_amount_qty', 'his_stock_amount_moneny', 'his_stock_market', 'his_stock_marketcapital',
        'his_stock_52lowprice', 'his_stock_52mprice')
    search_fields = ('his_stock_code', 'his_stock_name')
    list_filter = ('his_stock_market',)
    date_hierarchy = 'his_stock_date'


admin.site.site_header = '木骨'
admin.site.site_title = '木骨'
admin.site.register(MUser, MUserAdmin)
admin.site.register(MStock, MStockAdmin)
admin.site.register(MStock_His, HisMStockAdmin)

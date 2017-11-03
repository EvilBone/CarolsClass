from django.contrib import admin
from .models import MUser,MStock
# Register your models here.

class MUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_description', 'user_follower_counts','user_friends_count','user_gender','user_province','user_stocks_count','user_is_deal')
    search_fields = ('user_name',)

class MStockAdmin(admin.ModelAdmin):
    list_display = ('stock_code','stock_name','stock_cprice','stock_lprice','stock_mprice','stock_low_price')
    search_fields = ('stock_code','stock_name')

admin.site.register(MUser,MUserAdmin)
admin.site.register(MStock,MStockAdmin)
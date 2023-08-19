from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(table_bank)
admin.site.register(table_price)
admin.site.register(table_gold)
admin.site.register(table_price_market)
admin.site.register(table_gold_dinar)
admin.site.register(name_table)
admin.site.register(price_numper)

names_list = ['البنك المركزي', 'اسعار متفرقة', 'سعر الذهب بالدولار', 'سعر ذهب بالدينار', 'أسعار الصرف في السوق الموازية']
for name in names_list:
    user = name_table(name=name)
    user.save()
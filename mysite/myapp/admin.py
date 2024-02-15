from django.contrib import admin
from .models import Product,OrderDetail, Coupon
# Register your models here.

admin.site.register(Product)
admin.site.register(OrderDetail)
admin.site.register(Coupon)
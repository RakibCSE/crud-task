from django.contrib import admin

from .models import Product, Attribute, Price


admin.site.register(Product)
admin.site.register(Attribute)
admin.site.register(Price)

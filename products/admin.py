from django.contrib import admin
from .models import Product, Offer, ProductSelected


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")


admin.site.register(Product)


class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "discount")


admin.site.register(Offer)

admin.site.register(ProductSelected)

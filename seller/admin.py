from django.contrib import admin

from seller.models import Seller, QuantityOfProduct, Property, Product


# Register your models here.


class SellerAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'email', 'phone', 'landmark']
    ordering = ['company_name']
    sortable_by = ['is_active', 'is_superuser', 'is_admin']
    list_display_links = ['id', 'company_name']
    list_editable = ['email', 'phone', 'landmark']


admin.site.register(Seller, SellerAdmin)
admin.site.register(QuantityOfProduct)
admin.site.register(Property)
admin.site.register(Product)

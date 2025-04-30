from django.contrib import admin
from .models import WebsiteSettings,Category,Contactus,TrandingProducts,SubCategory,\
    Product,ContactInquiry
# Register your models here.
admin.site.register(WebsiteSettings)
admin.site.register(Category)
admin.site.register(Contactus)
admin.site.register(TrandingProducts)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ContactInquiry)
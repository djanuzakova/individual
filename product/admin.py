from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, ProductImage


class InlineProductImage(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image',)


class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineProductImage, ]
    list_display = ('title', 'in_stock', 'price', "image")
    list_filter = ('category',)

    def image(self, obj):
        img = obj.Image.first()
        if img:
            return mark_safe(f"<img src='{img.image.url}' width='80' height='80' style='object-fit: contain'/>")
        else:
            return ""


admin.site.register(Product)





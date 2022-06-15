from django.contrib import admin

from .models import Cart, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'status'
    )
    readonly_fields = ('total_price',)

    def total_price(self, obj):
        total = 0
        for item in obj.items.all():
            total += item.price

        return total


admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)

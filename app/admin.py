from django.contrib import admin

from .models import Orders


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'status')
    fields = ('id', 'first_name', 'last_name', 'status', 'created')
    readonly_fields = ('id', 'created')

from django.contrib import admin

from .models import Orders


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('department', 'status', 'created')
    fields = ('id', 'department', 'status', 'created')
    readonly_fields = ('id', 'created')

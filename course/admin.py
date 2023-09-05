from django.contrib import admin

from course.models import Payment

@admin.register(Payment)
class PayAdmin(admin.ModelAdmin):
    list_display = ("date_of_pay", "cash", "payment_method")  # отображение на дисплее
    list_filter = ("date_of_pay", "cash", "payment_method")  # фильтр
    search_fields = ("date_of_pay", "cash", "payment_method")  # поля поиска

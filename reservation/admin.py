from django.contrib import admin
from django.db import reset_queries
from django_summernote.admin import SummernoteModelAdmin

from .models import Reservation

# Register your models here.


class ReservationAdmin(SummernoteModelAdmin, admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'

    list_display = ['name', 'email', 'phone', 'number_of_persons']

    search_fields = ['date', 'time']
    list_filter = ['name', 'phone']


admin.site.register(Reservation, ReservationAdmin)

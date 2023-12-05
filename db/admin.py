from django.contrib import admin
from db.models import Event, Earning, Expense,Fund

# Register your models here.


admin.site.register(Event)
admin.site.register(Earning)
admin.site.register(Expense)
admin.site.register(Fund)
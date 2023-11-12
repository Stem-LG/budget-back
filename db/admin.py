from django.contrib import admin
from db.models import Event, Person, Earning, Expense,Fund

# Register your models here.


admin.site.register(Event)
admin.site.register(Person)
admin.site.register(Earning)
admin.site.register(Expense)
admin.site.register(Fund)

from django.urls import path
from . import views


urlpatterns = [
    path("stats/",views.statsView),
    path("users/",views.usersView),
    path("event/",views.eventsView),
    path("event/<int:id>/",views.eventView),
    path("event/<int:event_id>/funds/",views.fundsView),
    path("event/<int:event_id>/expenses/",views.expensesView),
    path("event/<int:event_id>/earnings/",views.earningsView),
    path("fund/<int:id>/",views.fundView),
    path("expense/<int:id>/",views.expenseView),
    path("earning/<int:id>/",views.earningView),
]

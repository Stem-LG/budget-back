from django.urls import path
from api import views


urlpatterns = [
    path(r"stats/",views.statsView),
    path(r"users/",views.usersView),
    path(r"event/",views.eventsView),
    path(r"event/<int:id>/",views.eventView),
    path(r"event/<int:event_id>/funds/",views.fundsView),
    path(r"event/<int:event_id>/expenses/",views.expensesView),
    path(r"event/<int:event_id>/earnings/",views.earningsView),
    path(r"fund/<int:id>/",views.fundView),
    path(r"expense/<int:id>/",views.expenseView),
    path(r"earning/<int:id>/",views.earningView),
]

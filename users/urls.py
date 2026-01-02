from django.urls import path
from . import views
urlpatterns = [
    path('savings',views.account_opening,name='account_opening'),
]
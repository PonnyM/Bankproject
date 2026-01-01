from django.urls import path
from . import views
urlpatterns = [
    path('account_opening',views.account_opening,name='home'),
]
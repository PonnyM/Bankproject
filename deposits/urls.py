# from . import views
# from django.urls import path
# urlpatterns = [
#     path('',views.display,name='welcome'),
#     path('index/',views.index,name='index'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),        # homepage → index
    path('status/', views.display, name='status'),
]

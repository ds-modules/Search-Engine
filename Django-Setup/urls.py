from django.urls import path
from . import views 

# URLConf 

urlpatterns = [
    path('search/', views.search_engine, name = 'search_engine'),
    path('output_page/', views.output_page, name = 'output_page')
]

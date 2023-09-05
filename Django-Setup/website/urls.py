from django.urls import path
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# URLConf 

urlpatterns = [
    # path('search/', views.search_engine, name = 'search_engine'),
    # path('output_page/', views.output_page, name = 'output_page'),
    path('', views.main, name='main'),
    path('search/', views.search, name='search')
]

urlpatterns += staticfiles_urlpatterns()
from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='prodt_cat'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodDetails,name='details'),
    path('search',views.searching,name='search'),
    path('test',views.testing,name='test'),
  ]
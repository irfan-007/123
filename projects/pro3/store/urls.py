from django.urls import path
from . import views

urlpatterns = [
path('', views.index ,name='index'),
path('index/', views.index ,name='index'),
path('about/', views.about ,name='about'),
path('contact/', views.contact ,name='contact'),
path('product_detail/', views.product_detail ,name='product_detail'),
path('product/', views.product ,name='product'),

]   
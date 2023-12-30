from django.urls import path
from . import views 

urlpatterns = [
    path('menu/', views.menuItemView, name='menu'),
    path('menu/<int:id>/', views.itemView, name='menu_item'),
    path('', views.indexView, name='index'),
    path('booking/', views.form_view, name='booking'),
    path('aboutus', views.aboutView, name ='about' )
]

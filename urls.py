from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('/<int:month>',views.month_with_num),
    path('/<str:month>',views.months,name='disp'),
    
]
 
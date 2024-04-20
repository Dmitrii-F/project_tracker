from django.urls import path, re_path
from . import views

app_name = 'control'

urlpatterns = [
    path('', views.index),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),
]
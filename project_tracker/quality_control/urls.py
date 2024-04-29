from django.urls import path, re_path
from . import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bugs_list, name='bugs_list'),
    path('features/', views.features_list, name='features_list'),
    path('bugs/<str:bug_id>/', views.bug_detail, name='bug_detail'),
    path('features/<str:feature_id>/', views.feature_detail, name='feature_detail'),
]
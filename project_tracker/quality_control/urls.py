from django.urls import path
from . import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bugs_list, name='bugs_list'),
    path('features/', views.features_list, name='features_list'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),

    path('bugs/new/', views.add_bug_report, name='add_bug_report'),
    path('features/new/', views.add_feature_request, name='add_feature_request'),

    path('bugs/<int:bug_id>/update/', views.update_bug, name='update_bug'),
    path('features/<int:feature_id>/update/', views.update_feature, name='update_feature'),

    path('bugs/<int:bug_id>/delete/', views.delete_bug, name='delete_bug'),
    path('features/<int:feature_id>/delete/', views.delete_feature, name='delete_feature'),
]
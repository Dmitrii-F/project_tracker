from django.urls import path
from . import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bugs_list, name='bugs_list'),
    path('features/', views.features_list, name='features_list'),
    path('bugs/<str:bug_id>/', views.bug_detail, name='bug_detail'),
    path('features/<str:feature_id>/', views.feature_detail, name='feature_detail'),


    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('bugs/<int:bug_id>/update/', views.BugUpdateView.as_view(), name='update_bug'),
    path('features/<int:feature_id>/update/', views.FeatureUpdateView.as_view(), name='update_feature'),
    path('bugs/<int:bug_id>/delete/', views.BugDeleteView.as_view(), name='delete_bug'),
    path('features/<int:feature_id>/delete/', views.FeatureDeleteView.as_view(), name='delete_feature'),
]
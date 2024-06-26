from django.urls import path
from . import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugsListView.as_view(), name='bugs_list'),
    path('features/', views.FeaturesListView.as_view(), name='features_list'),
    path('bugs/create/', views.BugCreateView.as_view(), name='add_bug_report'),
    path('features/create/', views.FeatureCreateView.as_view(), name='add_feature_request'),

    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('bugs/<int:bug_id>/update/', views.BugUpdateView.as_view(), name='update_bug'),
    path('features/<int:feature_id>/update/', views.FeatureUpdateView.as_view(), name='update_feature'),
    path('bugs/<int:bug_id>/delete/', views.BugDeleteView.as_view(), name='delete_bug'),
    path('features/<int:feature_id>/delete/', views.FeatureDeleteView.as_view(), name='delete_feature'),
]
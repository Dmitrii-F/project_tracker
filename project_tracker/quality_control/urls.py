from django.urls import path, re_path
from . import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugsListView.as_view(), name='bugs_list'),
    path('features/', views.FeaturesListView.as_view(), name='features_list'),
    path('bugs/<str:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/<str:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
]
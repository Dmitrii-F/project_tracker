from django.urls import path, re_path
from . import views

app_name = 'control'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugListView.as_view(), name='bug_list'),
    path('features/', views.FeatureListView.as_view(), name='feature_list'),
    path('bugs/<str:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/<str:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
]
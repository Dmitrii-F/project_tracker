from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.task_detail, name='task_detail'),


    path('project/create/', views.ProjectCreateView.as_view(), name='create_project'),
    path('project/<int:project_id>/add_task/', views.TaskCreateView.as_view(), name='add_task_to_project'),
    path('project/<int:project_id>/update/', views.ProjectUpdateView.as_view(), name='update_project'),
    path('project/<int:project_id>/tasks/<int:task_id>/update/', views.TaskUpdateView.as_view(), name='update_task'),
    path('project/<int:project_id>/delete/', views.ProjectDeleteView.as_view(), name='delete_project'),
    path('project/<int:project_id>/tasks/<int:task_id>/delete/', views.TaskDeleteView.as_view(), name='delete_task'),
]
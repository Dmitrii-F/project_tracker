from django import forms
from django.forms import ModelForm
from .models import BugReport, FeatureRequest
from tasks.models import Project, Task

class BugForm(ModelForm):
    class Meta:
        model = BugReport
        fields = ['title','project', 'task', 'description', 'status', 'priority']

class FeatureForm(ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['title', 'project', 'task', 'description', 'status', 'priority']
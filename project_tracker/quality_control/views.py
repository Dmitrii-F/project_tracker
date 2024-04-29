
from .models import BugReport, FeatureRequest
from django.shortcuts import render

from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')

class BugsListView(ListView):
    model = BugReport
    template_name = 'quality_control/bugs_list.html'

class FeaturesListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/features_list.html'

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'



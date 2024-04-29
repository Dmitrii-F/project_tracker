
from .models import BugReport, FeatureRequest

from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView

from django.shortcuts import get_object_or_404, render, redirect
from .forms import BugForm, FeatureForm


def add_bug_report(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs_list')
    else:
        form = BugForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def add_feature_request(request):
    if request.method == 'POST':
        form = FeatureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features_list')
    else:
        form = FeatureForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})



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



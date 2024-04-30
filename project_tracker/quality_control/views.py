
from .models import BugReport, FeatureRequest
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render, redirect
from .forms import BugForm, FeatureForm
from django.urls import reverse, reverse_lazy



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



class BugCreateView(CreateView):
    model = BugReport
    form_class = BugForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:bugs_list')

class FeatureCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('quality_control:features_list')

class BugUpdateView(UpdateView):
    model = BugReport
    form_class = BugForm
    template_name = 'quality_control/bug_update.html'
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bugs_list')

class FeatureUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureForm
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:features_list')

class BugDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bugs_list')
    template_name = 'quality_control/bug_confirm_delete.html'

class FeatureDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:features_list')
    template_name = 'quality_control/feature_confirm_delete.html'



from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from bboard.models import Bb, Rubric
from bboard.forms import BbForm

def index(request):
    template_name = 'bboard/index.html'
    deals = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'bbs': deals,
        'rubrics': rubrics,
    }
    return render(request, template_name=template_name, context=context)

def by_rubric(request, rubric_id):
    template_name = 'bboard/by_rubric.html'
    deals_by_rubric = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bbs': deals_by_rubric,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
    }
    return render(request, template_name=template_name, context=context)

class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubric'] = Rubric.objects.all()
        return context

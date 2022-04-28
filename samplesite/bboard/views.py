from django.shortcuts import render
from bboard.models import Bb

def index(request):
    template_name = 'bboard/index.html'
    deals = Bb.objects.all()
    context = {'bbs': deals}
    return render(request, template_name=template_name, context=context)

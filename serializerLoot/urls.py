from django.urls import path
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from .views import LootsView, OrderingView, FastOrderingView


urlpatterns = [
    path('', csrf_exempt(TemplateView.as_view(template_name='index.html')), name='index'),
    path('loots/', LootsView.as_view()),
    path('order/', OrderingView.as_view()),	
    path('fastorder/', FastOrderingView.as_view()),	
]
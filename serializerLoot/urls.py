from django.urls import path
from django.views.generic import TemplateView

from .views import LootsView, OrderingView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('loots/', LootsView.as_view()),
		path('order/', OrderingView.as_view()),	
]
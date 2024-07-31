from django.shortcuts import render
from django.views.generic import TemplateView

from journal.models import AboutMe, Publication


# Create your views here.



class HomeView(TemplateView):
    template_name = 'index.html'


class PublicationView(TemplateView):
    template_name = 'publication-detail.html'

    def get_context_data(self, **kwargs):
        context = {
            'publication_list': Publication.objects.all()
        }
        return context

class AboutView(TemplateView):
    template_name = 'about.html'
    def get_context_data(self, **kwargs):
        context = {
            'about_me': AboutMe.objects.first()
        }
        return context
from django.shortcuts import render
from django.views.generic import TemplateView

from journal.models import AboutMe


# Create your views here.



class HomeView(TemplateView):
    template_name = 'index.html'


#class BlogView(TemplateView):
#    template_name = 'blog.html'


class AboutView(TemplateView):
    def get_context_data(self, **kwargs):
        context = {
            'about_me': AboutMe.objects.first()
        }
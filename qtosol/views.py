
from django.shortcuts import render
from django.views.generic import TemplateView



# Create your views here.
class qtosolView(TemplateView):
    pass



qtosol_home_view = qtosolView.as_view(template_name="qtosol/home.html")

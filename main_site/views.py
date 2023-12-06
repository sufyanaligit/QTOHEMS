from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



from django.views.generic import TemplateView

class MainSiteView(TemplateView):
    pass

MainSiteView= MainSiteView.as_view(template_name="site/index.html")

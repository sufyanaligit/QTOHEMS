
from django.shortcuts import render
from django.views.generic import TemplateView



# Create your views here.
class qtosolView(TemplateView):
    pass



qtosol_home_view = qtosolView.as_view(template_name="qtosol/home.html")
qtosol_services_view = qtosolView.as_view(template_name="qtosol/Service.html")
qtosol_contactus_view = qtosolView.as_view(template_name="qtosol/ContactUs.html")
qtosol_sample_view = qtosolView.as_view(template_name="qtosol/Sample.html")
qtosol_quote_view = qtosolView.as_view(template_name="qtosol/Quote.html")
qtosol_aboutus_view = qtosolView.as_view(template_name="qtosol/AboutUs.html")
qtosol_career_view = qtosolView.as_view(template_name="qtosol/Career.html")

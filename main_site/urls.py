from django.urls import path
from main_site.views import (
    MainSiteView
)

app_name = 'main_site'
 
urlpatterns = [
    path("", view =MainSiteView, name="site"),  # Corrected with .as_view()
]


from django.urls import path, re_path
from django.views.static import serve
import os
from dashboards.views import (
    dashboard_view,
    dashboard_analytics_view,
    dashboard_crm_view,
    dashboard_crypto_view,
    dashboard_projects_view,
    dashboard_nft_view,
    dashboard_job_view
)

app_name = 'dashboards'
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
urlpatterns = [
    path('',view =dashboard_view,name=" "),
    # re_path(r'^$', serve, {'document_root': os.path.join(BASE_DIR, 'build'), 'path': 'index.html'}),
    path('dashboard-analytics',view =dashboard_analytics_view,name="dashboard_analytics"),
    path('dashboard-crm', view =dashboard_crm_view,name="dashboard_crm"),
    path('dashboard-crypto', view =dashboard_crypto_view,name="dashboard_crypto"),
    path('dashboard-projects', view =dashboard_projects_view,name="dashboard_projects"),
    path('dashboard-nft', view =dashboard_nft_view,name="dashboard_nft"),    
    path('dashboard-job', view =dashboard_job_view,name="dashboard_job"),    
]



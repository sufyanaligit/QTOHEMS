"""velzon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required
from .views import MyPasswordChangeView, MyPasswordSetView
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path('', include('qtohouse.urls')),
    # path('qtosol/', include('qtosol.urls')),
    
    # path('cart/', include('carts.urls')),
    path('admin/', admin.site.urls),
    # Dashboard
    path('dashboard/',include('dashboards.urls')),
    # Apps
    path('apps/',include('apps.urls')),
    # main_site
    path('Home/',include('main_site.urls')),
    # Layouts
    path('layouts/',include('layouts.urls')),
    # Components
    path('components/',include('components.urls')),
    # Pages
    path('pages/',include('pages.urls')),
    path(
        "account/password/change/",
        login_required(MyPasswordChangeView.as_view()),
        name="account_change_password",
    ),
    path(
        "account/password/set/",
        login_required(MyPasswordSetView.as_view()),
        name="account_set_password",
    ),
    # All Auth 
    path('account/', include('allauth.urls')),
    # reactapppp used for authentication of  React Frontend 
    path('reactapp/', include('reactapp.urls')),
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import redirect
from allauth.account.views import LoginView
from django.contrib.auth import login,logout
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from apps.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.
class qtosolView(TemplateView):
    pass



# qtosol_home_view = qtosolView.as_view(template_name="qtosol/home.html")
def qtosol_home_view(request):
    # Assuming you have a User model and the user is authenticated
    user = request.user
    return render(request, 'qtosol/home.html', {'user': user})
qtosol_services_view = qtosolView.as_view(template_name="qtosol/Service.html")
qtosol_contactus_view = qtosolView.as_view(template_name="qtosol/ContactUs.html")
qtosol_sample_view = qtosolView.as_view(template_name="qtosol/Sample.html")
qtosol_quote_view = qtosolView.as_view(template_name="qtosol/Quote.html")
qtosol_aboutus_view = qtosolView.as_view(template_name="qtosol/AboutUs.html")
qtosol_career_view = qtosolView.as_view(template_name="qtosol/Career.html")
qtosol_Register_view = qtosolView.as_view(template_name="qtosol/Register.html")

# qtosol_login_view = qtosolView.as_view(template_name="qtosol/Login.html")


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # Redirect to the home page
            return redirect('/')
    else:
        form = AuthenticationForm()
    
    return render(request, 'qtosol/Login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('/')









qtosol_blog_view = qtosolView.as_view(template_name="qtosol/Blog.html")
qtosol_CheckOut_view = qtosolView.as_view(template_name="qtosol/CheckOut.html")
qtosol_Cart_view = qtosolView.as_view(template_name="qtosol/Cart.html")
# qtosol_Projects_view = qtosolView.as_view(template_name="qtosol/Projects.html")
# views.py in the app where you want to display projects
@login_required
def qtosol_Projects_view(request):
    projects = Project.objects.all().order_by('-project_id')
    return render(request, "qtosol/Projects.html", {'projects': projects})
@login_required
def project_detail_view(request, pk):
    projects = get_object_or_404(Project, project_id=pk)
    return render(request, "qtosol/ProjectDetail.html", {'projects': projects})




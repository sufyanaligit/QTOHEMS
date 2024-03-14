from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import redirect
from allauth.account.views import LoginView
from django.contrib.auth import login,logout
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from apps.models import Project
from qtosol.models import Cart,CartItem
from django.contrib.auth.decorators import login_required

class qtohouseView(TemplateView):
    pass

def qtohouse_home_view(request):
    user = request.user
    return render(request, 'qtohouse/home.html', {'user': user})

qtohouse_services_view = qtohouseView.as_view(template_name="qtohouse/Service.html")
qtohouse_contactus_view = qtohouseView.as_view(template_name="qtohouse/ContactUs.html")
qtohouse_sample_view = qtohouseView.as_view(template_name="qtohouse/Sample.html")
qtohouse_quote_view = qtohouseView.as_view(template_name="qtohouse/Quote.html")
qtohouse_aboutus_view = qtohouseView.as_view(template_name="qtohouse/AboutUs.html")
qtohouse_career_view = qtohouseView.as_view(template_name="qtohouse/Career.html")
qtohouse_Register_view = qtohouseView.as_view(template_name="qtohouse/Register.html")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()
    
    return render(request, 'qtohouse/Login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

qtohouse_blog_view = qtohouseView.as_view(template_name="qtohouse/Blog.html")
qtohouse_CheckOut_view = qtohouseView.as_view(template_name="qtohouse/CheckOut.html")
qtohouse_Cart_view = qtohouseView.as_view(template_name="qtohouse/Cart.html")

@login_required
def qtohouse_Projects_view(request):
    projects = Project.objects.all().order_by('-project_id')
    return render(request, "qtohouse/Projects.html", {'projects': projects})

@login_required
def project_detail_view(request, pk):
    projects = get_object_or_404(Project, project_id=pk)
    return render(request, "qtohouse/ProjectDetail.html", {'projects': projects})

def cart(request,):
    return render(request, 'qtohouse/Cart.html')

def add_to_cart(request, pk):
    project = get_object_or_404(Project, project_id=pk)
    
    if request.user.is_authenticated:
        user_cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=project, user=request.user, defaults={'quantity': 1})
        
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        return redirect('Cart.html')
    else:
        return redirect('login')

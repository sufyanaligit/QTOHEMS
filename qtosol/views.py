
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.shortcuts import redirect
from allauth.account.views import LoginView
from django.contrib.auth import login,logout
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from apps.models import Project
from .models import Cart,CartItem
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






# cart functions

def cart(request,):
    # tax = 0
    # grand_total = 0
    # try:
    #     if request.user.is_authenticated:
    #         cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    #     else:
    #         cart = Cart.objects.get(cart_id=_cart_id(request))
    #         cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        
    #     for cart_item in cart_items:
    #         total += (cart_item.product.price * cart_item.quantity)
    #         quantity += cart_item.quantity

    #     tax = (2 * total) / 100
    #     grand_total = total + tax
    # except ObjectDoesNotExist:
    #     pass

    # context = {
    #     'total': total,
    #     'quantity': quantity,
    #     'cart_items': cart_items,
    #     'tax': tax,
    #     'grand_total': grand_total,
    # }

    return render(request, 'qtosol/Cart.html')
def add_to_cart(request, pk):
    # Get the project object based on the provided primary key
    project = get_object_or_404(Project, project_id=pk)
    
    # Ensure that the user is authenticated
    if request.user.is_authenticated:
        # Get or create the user's cart
        user_cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Create a cart item associated with the user's cart and the project
        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=project, user=request.user, defaults={'quantity': 1})
        
        # If the cart item already exists, increment the quantity
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        # Redirect the user to the cart page after adding the item
        return redirect('Cart.html')
    else:
        # Handle cases where the user is not authenticated
        # Redirect the user to the login page or display an error message
        return redirect('login')

# def add_to_cart(request, pk):
#     # Get the project object based on the provided primary key
#     project = get_object_or_404(Project, project_id=pk)
    
#     # Get or create the user's cart
#     user_cart, created = Cart.objects.get_or_create(user=request.user)
    
#     # Check if the project is already in the user's cart
#     cart_item = CartItem.objects.filter(cart=user_cart, product=project).first()
    
#     # If the item is already in the cart, increase the quantity
#     if cart_item:
#         cart_item.quantity += 1
#         cart_item.save()
#     else:
#         # If the item is not in the cart, create a new cart item
#         cart_item = CartItem.objects.create(cart=user_cart, product=project, quantity=1)
    
#     return redirect('cart')



from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from apps.models import Project
from .models import Cart, CartItem

# Create your views here.

# def _cart_id(request):
#     cart = request.session.session_key
#     if not cart:
#         cart = request.session.create()
#     return cart

# @login_required(login_url='login')
# def add_cart(request, project_id):
#     current_user = request.user
#     project = Project.objects.get(id=project_id)

#     if current_user.is_authenticated:
#         try:
#             cart_item = CartItem.objects.get(project=project, user=current_user)
#             cart_item.quantity += 1
#             cart_item.save()
#         except CartItem.DoesNotExist:
#             cart_item = CartItem.objects.create(
#                 project=project,
#                 quantity=1,
#                 user=current_user
#             )
#         return redirect('cart')
#     else:
#         try:
#             cart = Cart.objects.get(cart_id=_cart_id(request))
#         except Cart.DoesNotExist:
#             cart = Cart.objects.create(
#                 cart_id=_cart_id(request)
#             )
#             cart.save()

#         try:
#             cart_item = CartItem.objects.get(project=project, cart=cart)
#             cart_item.quantity += 1
#             cart_item.save()
#         except CartItem.DoesNotExist:
#             cart_item = CartItem.objects.create(
#                 project=project,
#                 quantity=1,
#                 cart=cart
#             )
#         return redirect('cart')

# def remove_cart(request, project_id, cart_item_id):
#     project = get_object_or_404(Project, id=project_id)

#     try:
#         if request.user.is_authenticated:
#             cart_item = CartItem.objects.get(project=project, user=request.user, id=cart_item_id)
#         else:
#             cart = Cart.objects.get(cart_id=_cart_id(request))
#             cart_item = CartItem.objects.get(project=project, cart=cart, id=cart_item_id)

#         if cart_item.quantity > 1:
#             cart_item.quantity -= 1
#             cart_item.save()
#         else:
#             cart_item.delete()
#     except:
#         pass
#     return redirect('cart')

# def remove_cart_item(request, project_id, cart_item_id):
#     project = get_object_or_404(Project, id=project_id)

#     if request.user.is_authenticated:
#         cart_item = CartItem.objects.get(project=project, user=request.user, id=cart_item_id)
#     else:
#         cart = Cart.objects.get(cart_id=_cart_id(request))
#         cart_item = CartItem.objects.get(project=project, cart=cart, id=cart_item_id)

#     cart_item.delete()
#     return redirect('cart')

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

# @login_required(login_url='login')
# def checkout(request, total=0, quantity=0, cart_items=None):
#     try:
#         tax = 0
#         grand_total = 0
#         if request.user.is_authenticated:
#             cart_items = CartItem.objects.filter(user=request.user, is_active=True)
#         else:
#             cart = Cart.objects.get(cart_id=_cart_id(request))
#             cart_items = CartItem.objects.filter(cart=cart, is_active=True)

#         for cart_item in cart_items:
#             total += (cart_item.project.price * cart_item.quantity)
#             quantity += cart_item.quantity

#         tax = (2 * total) / 100
#         grand_total = total + tax
#     except ObjectDoesNotExist:
#         pass

#     context = {
#         'total': total,
#         'quantity': quantity,
#         'cart_items': cart_items,
#         'tax': tax,
#         'grand_total': grand_total,
#     }

#     return render(request, 'store/checkout.html', context)

from django.urls import path
from qtohouse.views import(
    qtohouse_home_view,
    qtohouse_aboutus_view,
    qtohouse_services_view,
    qtohouse_contactus_view,
    qtohouse_sample_view,
    qtohouse_quote_view,
    qtohouse_career_view,
    qtohouse_Register_view,

    qtohouse_blog_view,
    qtohouse_CheckOut_view,
    qtohouse_Cart_view,
    qtohouse_Projects_view,



)
from . import views
 
urlpatterns = [
    path("", view=qtohouse_home_view, name="qtohousehome"),
    path("AboutUs", view=qtohouse_aboutus_view, name="qtohouseabout"),
    path("Services", view=qtohouse_services_view, name="qtohouseservices"),
    path("career", view=qtohouse_career_view, name="career"),
    path("ContactUs", view=qtohouse_contactus_view, name="qtohousecontact"),
    path("Sample", view=qtohouse_sample_view, name="qtohousesample"),
    path("quote", view=qtohouse_quote_view, name="qtohousequote"),
    path("Register", view=qtohouse_Register_view, name="qtohouseRegister"),
    
    path("blog", view=qtohouse_blog_view, name="qtohouseblog"),
    path("Cart", view=qtohouse_Cart_view, name="qtohouseCart"),
    path("CheckOut", view=qtohouse_CheckOut_view, name="qtohouseCheckOut"),
    path("Projects", view=qtohouse_Projects_view, name="qtohouseProjects"),
    path('project_detail/<int:pk>/', views.qtohouse_project_detail_view, name='qtohouse_project_detail_view'),



    # path('login/', qtohouseLoginView.as_view(), name='login'),
    path('Login/', views.login_view, name='login'),
    path('Logout/', views.logout_view, name='logout'),


    # Cart paths
    # path('cart/', views.cart, name='cart'),
    # path('add/<int:pk>/', views.add_to_cart, name='add_to_cart'),

   

    # # Horizontal
    # path("horizontal", view=layouts_horizontal_view, name="horizontal"),
    # # Detached
    # path("detached", view=layouts_detached_view, name="detached"),
    # # Two Colomn
    # path("two_colomn", view=layouts_column_view, name="two_colomn"),
    # # Hovered
    # path("hovered", view=layouts_hovered_view, name="hovered"),
    #     # Vertical
    # path("vertical", view=layouts_vertical_view, name="vertical")
]
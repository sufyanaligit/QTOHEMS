from django.urls import path
from qtosol.views import(
    qtosol_home_view,
    qtosol_aboutus_view,
    qtosol_services_view,
    qtosol_contactus_view,
    qtosol_sample_view,
    qtosol_quote_view,
    qtosol_career_view,
    qtosol_Register_view,

    qtosol_blog_view,
    qtosol_CheckOut_view,
    qtosol_Cart_view,
    qtosol_Projects_view,



)
from . import views

urlpatterns = [
    path("", view=qtosol_home_view, name="qtosolhome"),
    path("AboutUs", view=qtosol_aboutus_view, name="qtosolabout"),
    path("Services", view=qtosol_services_view, name="qtosolservices"),
    path("career", view=qtosol_career_view, name="qtosolcareer"),
    path("ContactUs", view=qtosol_contactus_view, name="qtosolcontact"),
    path("Sample", view=qtosol_sample_view, name="qtosolsample"),
    path("quote", view=qtosol_quote_view, name="qtosolquote"),
    path("Register", view=qtosol_Register_view, name="qtosolRegister"),
    
    path("blog", view=qtosol_blog_view, name="qtosolblog"),
    path("Cart", view=qtosol_Cart_view, name="qtosolCart"),
    path("CheckOut", view=qtosol_CheckOut_view, name="qtosolCheckOut"),
    path("Projects", view=qtosol_Projects_view, name="qtosolProjects"),
    path('project_detail/<int:pk>/', views.project_detail_view, name='project_detail_view'),



    # path('login/', QtosolLoginView.as_view(), name='login'),
    path('Login/', views.login_view, name='login'),
    path('Logout/', views.logout_view, name='logout'),


    # Cart paths
    path('cart/', views.cart, name='cart'),
    path('add/<int:pk>/', views.add_to_cart, name='add_to_cart'),

   

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
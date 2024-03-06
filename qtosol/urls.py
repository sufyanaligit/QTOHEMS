from django.urls import path
from qtosol.views import(
    qtosol_home_view,
    qtosol_aboutus_view,
    qtosol_services_view,
    qtosol_contactus_view,
    qtosol_sample_view,
    qtosol_quote_view,
    qtosol_career_view,


)

urlpatterns = [
    path("", view=qtosol_home_view, name="qtosolhome"),
    path("AboutUs", view=qtosol_aboutus_view, name="qtosolabout"),
    path("Services", view=qtosol_services_view, name="qtosolservices"),
    path("career", view=qtosol_career_view, name="qtosolcareer"),
    path("ContactUs", view=qtosol_contactus_view, name="qtosolcontact"),
    path("Sample", view=qtosol_sample_view, name="qtosolsample"),
    path("quote", view=qtosol_quote_view, name="qtosolquote"),

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
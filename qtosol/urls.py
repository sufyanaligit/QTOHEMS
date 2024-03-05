from django.urls import path
from qtosol.views import(
    qtosol_home_view,
)

urlpatterns = [
    path("", view=qtosol_home_view, name="qtosolhome"),

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
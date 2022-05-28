from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.jan),
    # path("feb", views.feb),
    # path("march", views.mar)
    path("",views.index , name="index"),
    # path("<int:month_param>",views.month_caller_by_number_redirect),
    path("<int:month_param>",views.month_caller_by_number_redirect_reverse),
    path("<str:month_param>",views.month_caller, name="my_challenge_function")
]
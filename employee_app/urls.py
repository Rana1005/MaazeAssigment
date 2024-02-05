from .views import AllempView,SearchEmp
from django.urls import path

urlpatterns = [
    path('allemp/',AllempView.as_view()),
    path('findemp/',SearchEmp.as_view())


]
from .views import AllempView,AddEmployeeView
from django.urls import path

urlpatterns = [
    path('allemp/',AllempView.as_view()),
    path('addemployee/',AddEmployeeView.as_view())
    

]
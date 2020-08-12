from django.urls import path
from apps.lhp.views import *

urlpatterns = [
    path('',LoginFormView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout')

]

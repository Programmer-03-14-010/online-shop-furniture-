from django.urls import path

from pages.views import home_page_view, ContactCreateView
from . import views

app_name = "pages"

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('', home_page_view, name='home')
]

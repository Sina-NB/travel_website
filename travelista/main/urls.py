from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index_view, name='index-page'),
    path('about', views.about_view, name='about-page'),
    path('contact', views.contact_view, name='contact-page')
]
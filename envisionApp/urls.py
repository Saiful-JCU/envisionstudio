from django.urls import path
from .views import home, get_message, getJobData, service_detail, blog_cards, blogDetailsView, aboutpage, contactPage, servicePage


urlpatterns = [
    path('', home, name = 'home'),
    path('get-message/', get_message, name='get-message'),
    path('getJobData/', getJobData, name='getjobdata'),
    path("service_detail/<slug:slug>/",service_detail, name="service_detail"),
    path("blog_cards/",blog_cards, name="blog_cards"),
    path("blogDetailsView/<slug:slug>/",blogDetailsView, name="blogDetailsView"),
    path("aboutpage/",aboutpage, name="aboutpage"),
    path("servicePage/",servicePage, name="servicePage"),
    path("contactPage/",contactPage, name="contactPage"),

]

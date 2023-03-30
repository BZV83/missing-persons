from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import faqPageView

urlpatterns = [
    path("", indexPageView, name = "index"),
    path("about/", aboutPageView, name = "about"),
    path("faq/", faqPageView, name = "faq"),
]

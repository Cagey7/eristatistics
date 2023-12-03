from django.urls import path
from macrobulletin.views import *

urlpatterns = [
    path("topics/", TopicAPIList.as_view()),
    path("topics/<int:pk>", TopicAPIDetailView.as_view()),
    path("economic-indices/", EconomicIndexAPIList.as_view()),
    path("economic-indices/<int:pk>", EconomicIndexAPIDetailView.as_view()),
    path("tables/", TableAPIList.as_view()),
    path("tables/<int:pk>", TableAPIDetailView.as_view()),
]

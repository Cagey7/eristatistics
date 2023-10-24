from django.urls import path
from . import views
from macrobulletin.views import TestAPIView

urlpatterns = [
    path('test/', TestAPIView.as_view()),
]

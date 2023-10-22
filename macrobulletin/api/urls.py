from django.urls import path
from . import views
from macrobulletin.api.views import TestAPIView

urlpatterns = [
    path('test/', TestAPIView.as_view()),
]

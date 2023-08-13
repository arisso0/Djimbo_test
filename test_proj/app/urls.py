from django.urls import path
from .views import AllPagesViewSet, DetailPageView

urlpatterns = [
    path('', AllPagesViewSet.as_view()),
    path('<slug>/', DetailPageView.as_view()),
]

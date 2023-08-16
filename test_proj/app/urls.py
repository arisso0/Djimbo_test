from django.urls import path
from .views import AllPagesListView, BlocksPageListView

urlpatterns = [
    path('', AllPagesListView.as_view()),
    path('<slug>/', BlocksPageListView.as_view()),
]

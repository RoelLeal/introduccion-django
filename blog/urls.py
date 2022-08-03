from django.urls import path
from .views import blogListView

app_name = "blog"

urlpatterns = [
      path('', blogListView.as_view(), name="home")
]


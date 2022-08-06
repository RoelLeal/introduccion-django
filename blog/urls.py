from django.urls import path
from .views import blogListView, blogCreateView

app_name = "blog"

urlpatterns = [
      path('', blogListView.as_view(), name="home"),
      path('create/', blogCreateView.as_view(), name="create")
]


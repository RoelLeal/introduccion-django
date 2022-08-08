from django.urls import path
from .views import blogListView, blogCreateView, blogDetailView, blogUpdateView, blogDeleteView

app_name = "blog"

urlpatterns = [
      path('', blogListView.as_view(), name="home"),
      path('create/', blogCreateView.as_view(), name="create"),
      path('<int:pk>/', blogDetailView.as_view(), name="detail"),
      path('<int:pk>/update/', blogUpdateView.as_view(), name="update"),
      path('<int:pk>/delete/', blogDeleteView.as_view(), name="delete")
]


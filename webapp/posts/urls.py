from django.urls import path
# from . import views
from .views import HomeView, ServiceDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, category_view, category_list_view, like_view

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ServiceDetailView.as_view(), name="service-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:categories>/', category_view, name="category"),
    path('category-list/', category_list_view, name="category-list"),
    path('like/<int:pk>', like_view, name='like_post'),
]

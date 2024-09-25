# from rest_framework import routers
from . import views
from .views import get_categories, get_features, index
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('categories/', get_categories, name='categories'),
    path('features/', get_features, name='features'),
]

# router = routers.DefaultRouter()
# router.register(r'category', get_category, basename='category')
# # router.register(r'accounts', AccountViewSet)
# urlpatterns += router.urls
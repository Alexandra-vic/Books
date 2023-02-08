from django.urls import path, include
from . views import CategoryViewSet, TagViewSet

from rest_framework.routers import DefaultRouter 



router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('tag', TagViewSet, basename='tag')

urlpatterns = router.urls
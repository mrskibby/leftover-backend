from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuSectionViewSet, MenuItemViewSet

router = DefaultRouter()
router.register(r'sections', MenuSectionViewSet)
router.register(r'items', MenuItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

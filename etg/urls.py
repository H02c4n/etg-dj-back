from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import TagMVS
router = SimpleRouter()

router.register('tags', TagMVS, basename='tags')

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework.routers import DefaultRouter
from .views import TodoViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
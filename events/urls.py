from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ParticipantViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'participants', ParticipantViewSet)

# Inclure les routes du router dans les urlpatterns de l'application
urlpatterns = [
    path('', include(router.urls)),
]

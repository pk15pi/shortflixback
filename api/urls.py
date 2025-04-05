from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import LoginView, VideoViewSet, FormatChoiceViewSet, GenreChoiceViewSet, PlaybackInfoViewSet, CommentsViewSet, MonetizationViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('videos', VideoViewSet)
router.register('formats', FormatChoiceViewSet)
router.register('genere', GenreChoiceViewSet)
router.register('playbackinfo', PlaybackInfoViewSet)
router.register('comments', CommentsViewSet)
router.register('menetory', MonetizationViewSet)

urlpatterns = [
    # path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls))
]

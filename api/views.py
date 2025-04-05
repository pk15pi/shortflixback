from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Video, FormatChoice, GenreChoice, PlaybackInfo, Comments, Monetization
from .serializers import VideoSerializer, FormatChoiceSerializer, GenreChoiceSerializer, PlaybackInfoSerializer, CommentsSerializer, MonetizationSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('-added_on')
    serializer_class = VideoSerializer
    # permission_classes = [IsAuthenticated]


class FormatChoiceViewSet(viewsets.ModelViewSet):
    queryset = FormatChoice.objects.all()
    serializer_class = FormatChoiceSerializer


class GenreChoiceViewSet(viewsets.ModelViewSet):
    queryset = GenreChoice.objects.all()
    serializer_class = GenreChoiceSerializer


class PlaybackInfoViewSet(viewsets.ModelViewSet):
    queryset = PlaybackInfo.objects.all()
    serializer_class = PlaybackInfoSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class MonetizationViewSet(viewsets.ModelViewSet):
    queryset = Monetization.objects.all()
    serializer_class = MonetizationSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'token': str(refresh.access_token),
                'username': user.username,
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

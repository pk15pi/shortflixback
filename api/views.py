from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Video, FormatChoice, GenreChoice, PlaybackInfo, Comments, Monetization
from .serializers import VideoSerializer, FormatChoiceSerializer, GenreChoiceSerializer, PlaybackInfoSerializer, CommentsSerializer, MonetizationSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 6 

    def get_paginated_response(self, data):
        total_pages = math.ceil(self.page.paginator.count / self.page_size)
        return Response({
            'count': self.page.paginator.count,
            'total_pages': total_pages,
            'current_page': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('-added_on')
    serializer_class = VideoSerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        qs = super().get_queryset()
        params = self.request.GET

        keyword = self.request.query_params.get('keyword')

        # if keyword:
        #     print(keyword, "#######################")
        #     return qs.filter(keyword__in = keyword)
        
        # qs = qs.filter(**params.dict())
        return qs


class FormatChoiceViewSet(viewsets.ModelViewSet):
    queryset = FormatChoice.objects.all()
    serializer_class = FormatChoiceSerializer


class GenreChoiceViewSet(viewsets.ModelViewSet):
    queryset = GenreChoice.objects.all()
    serializer_class = GenreChoiceSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        params = self.request.GET
        qs = qs.filter(**params.dict())
        return qs

class PlaybackInfoViewSet(viewsets.ModelViewSet):
    queryset = PlaybackInfo.objects.all()
    serializer_class = PlaybackInfoSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        params = self.request.GET
        qs = qs.filter(**params.dict())
        return qs

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        params = self.request.GET
        qs = qs.filter(**params.dict())
        return qs

class MonetizationViewSet(viewsets.ModelViewSet):
    queryset = Monetization.objects.all()
    serializer_class = MonetizationSerializer
    
    def get_queryset(self):
        qs = super().get_queryset()
        params = self.request.GET
        qs = qs.filter(**params.dict())
        return qs


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

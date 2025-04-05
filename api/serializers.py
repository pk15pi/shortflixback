from rest_framework import serializers
from .models import Video, FormatChoice, GenreChoice, PlaybackInfo, Comments, Monetization

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class FormatChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormatChoice
        fields = '__all__'

class GenreChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreChoice
        fields = '__all__'

class PlaybackInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaybackInfo
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class MonetizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monetization
        fields = '__all__'

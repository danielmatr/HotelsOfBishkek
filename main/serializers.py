from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from comment.serializers import CommentSerializer
from .models import *


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ('image',)


class SavedSerializer(ModelSerializer):

    class Meta:
        model = Saved
        fields = '__all__'


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ImageSerializer(instance.images.all(), many=True, context=self.context).data
        representation['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        representation['likes'] = Likes.objects.filter(liked_ads=instance).count()
        representation['rating'] = Rating.objects.filter(ads=instance).count()
        return representation


class LikeSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Likes
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        ads = validated_data.get('liked_ads')

        if Likes.objects.filter(author=user, liked_ads=ads):
            return Likes.objects.get(author=user, liked_ads=ads)
        else:
            return Likes.objects.create(author=user, liked_ads=ads)


class CreateRatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ('star', 'ads')

    def create(self, validated_data):
        request = self.context.get('request')
        rating, user = Rating.objects.update_or_create(
            ads=validated_data.get('ads', None),
            author=request.user,
            star=validated_data.get("star", None)
        )
        return rating
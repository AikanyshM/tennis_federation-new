from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NewsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImages
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class GalleryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImages
        fields = "__all__"


class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = "__all__"


class GlobalSearchSerializer(serializers.Serializer):
    def to_native(self, obj):
        if isinstance(obj, Category): 
            serializer = CategorySerializer(obj)
        elif isinstance(obj, Club):
            serializer = ClubSerializer(obj)
        elif isinstance(obj, Trainer):
             serializer = TrainerSerializer(obj)
        elif isinstance(obj, Calendar):
             serializer = CalendarSerializer(obj)
        elif isinstance(obj, Rating):
             serializer = RatingSerializer(obj)
        elif isinstance(obj, News):
             serializer = NewsSerializer(obj)
        elif isinstance(obj, NewsImages):
            serializer = NewsImagesSerializer(obj)
        elif isinstance(obj, Gallery):
             serializer = GallerySerializer(obj)
        elif isinstance(obj, GalleryImages):
             serializer = GalleryImagesSerializer(obj)
        elif isinstance(obj, MainPage):
             serializer = MainPageSerializer(obj)
        else:
            raise Exception("Not found in any instance!")
        return serializer.data
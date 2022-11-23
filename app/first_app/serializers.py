from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from .models import *


class CategorySerializer(TranslatableModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ClubSerializer(TranslatableModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"


class TrainerSerializer(TranslatableModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"


class CalendarSerializer(TranslatableModelSerializer):
    class Meta:
        model = Calendar
        fields = "__all__"


class RatingSerializer(TranslatableModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
        read_only_fields = ('rating', )


class NewsSerializer(TranslatableModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class NewsImagesSerializer(TranslatableModelSerializer):
    class Meta:
        model = NewsImages
        fields = "__all__"


class GallerySerializer(TranslatableModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class GalleryImagesSerializer(TranslatableModelSerializer):
    class Meta:
        model = GalleryImages
        fields = "__all__"


class MainPageSerializer(TranslatableModelSerializer):
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
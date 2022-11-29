from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from .mixins import TranslatedSerializerMixin
from .models import *


class CategorySerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Category)

    class Meta:
        model = Category
        fields = ['translations', ]


class ClubSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Club)

    class Meta:
        model = Club
        fields = ['translations', 'address_link', 'instagram', 'facebook', 'images',  ] 


class TrainerSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Trainer)

    class Meta:
        model = Trainer
        fields = ['translations', 'images', ]


class CalendarSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Calendar)

    class Meta:
        model = Calendar
        fields = ['translations', 'start_date', 'end_date', ]


class RatingSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Rating)
    rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        fields = ['translations', 'rating', 'birth_date', 'number_of_tournaments', 'points', ]
        read_only_fields = ('rating', )

    def get_rating(self, instance):
        all_ratings = Rating.objects.all().order_by('-points').values('id', 'points')
        for index, item in enumerate(all_ratings):
            if item['id'] == instance.id:
                return index + 1


class NewsSerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=News)

    class Meta:
        model = News
        fields = ['translations', 'date', 'main_photo', ]


class NewsImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsImages
        fields = ['news_id', 'photo', ]


class GallerySerializer(TranslatedSerializerMixin, TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Gallery)

    class Meta:
        model = ['translations', 'main_image', 'date_added', ]


class GalleryImagesSerializer(TranslatableModelSerializer):

    class Meta:
        model = GalleryImages
        fields = ['gallery_id', 'images', ]


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



# def save(points):
#     rating = []
#     sorted_list = sorted(points)
#     for index, score in enumerate(sorted_list):
#         if index >= 0: 
#             index += 1
#             rating.append(index)
#     return sorted_list, rating
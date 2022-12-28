from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from .models import *


class CategorySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Category)

    class Meta:
        model = Category
        fields = ['id', 'translations', ]
        read_only_fields = ['id', ]


class ClubSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Club)

    class Meta:
        model = Club
        fields = ['id', 'translations', 'address_link', 'instagram', 'facebook', 'images',  ]
        read_only_fields = ['id', ]


class TrainerSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Trainer)

    class Meta:
        model = Trainer
        fields = ['id', 'translations', 'images', ]
        read_only_fields = ['id', ]


class CalendarSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Calendar)

    class Meta:
        model = Calendar
        fields = ['id', 'translations', 'start_date', 'end_date', 'category_gender', 'category_age', ]
        read_only_fields = ['id', ]


class RatingSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Rating)
    rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        fields = ['id', 'translations', 'rating', 'birth_date', 'number_of_tournaments', 'points', 'category_gender', 'category_age', ]
        read_only_fields = ('rating', 'id', )

    def get_rating(self, instance):
        all_ratings = Rating.objects.all().order_by('-points').values('id', 'points')
        for index, item in enumerate(all_ratings):
            if item['id'] == instance.id:
                return index + 1


class NewsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImages
        fields = ['id', 'news_id', 'photo', ]
        read_only_fields = ['id', ]
        

class NewsSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=News)

    class Meta:
        model = News
        fields = ['translations', 'id', 'date', 'main_photo', ]
        read_only_fields = ['id', ]


class GalleryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImages
        fields = ['id', 'gallery_id', 'images', ]
        read_only_fields = ['id', ]


class GallerySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Gallery)
    gallery_image = GalleryImagesSerializer(many=True)

    class Meta:
        model = Gallery
        fields = ['id', 'translations', 'main_image', 'date_added', 'gallery_image' ]
        read_only_fields = ['id', ]

    def create(self, validated_data):
        gallery_image = validated_data.pop('gallery_image')
        gallery_instance = Gallery.objects.create(**validated_data)
        for image in gallery_image:
            GalleryImages.objects.create(gallery_id=gallery_instance,**image)
        return gallery_instance


class MainPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainPage
        fields = "__all__"


class GlobalSearchSerializer(serializers.Serializer):
    class Meta:      
        model = User
        

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
        else:
            raise Exception("Not found in any instance!")
        return serializer.data
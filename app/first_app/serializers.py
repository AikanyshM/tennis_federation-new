from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from .models import *

class CategorySerializer(TranslatableModelSerializer):  
    translations = TranslatedFieldsField(shared_model=Category)    
    class Meta:
        model = Category
        fields = ['id', 'translations', 'images']
        read_only_fields = ['id', ]

class ClubSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Club)
    images = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Club
        fields = ['id', 'translations', 'address_link', 'instagram', 'facebook', 'images', ]
        read_only_fields = ['id', ]

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.images.url)

class TrainerSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Trainer)
    images = serializers.SerializerMethodField('get_image_url')    
    class Meta:
        model = Trainer
        fields = ['id', 'translations', 'images', ]
        read_only_fields = ['id', ]

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.images.url)

class CalendarSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Calendar)    
    class Meta:
        model = Calendar
        fields = ['id', 'translations', 'start_date', 'end_date', 'category_gender', 'category_age', 'regulations']
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
    photo = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = NewsImages
        fields = ['id', 'news_id', 'photo', ]
        read_only_fields = ['id', ]

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.photo.url)


class NewsSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=News)
    main_photo = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = News
        fields = ['translations', 'id', 'date', 'main_photo', ]
        read_only_fields = ['id', ]

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.main_photo.url)


class GalleryImagesSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField('get_image_url')    
    class Meta:
        model = GalleryImages
        fields = ['id', 'gallery_id', 'images', ]
        read_only_fields = ['id', ]

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.images.url)


class GallerySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Gallery)
    gallery_image = GalleryImagesSerializer(many=True)
    main_image = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Gallery
        fields = ['id', 'translations', 'main_image', 'date_added', 'gallery_image' ]
        read_only_fields = ['id', ]

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.main_image.url)

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

class OfficialPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficialPartner
        fields = "__all__"

class SponsorsAndPartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorsAndPartners
        fields = "__all__"

class InformationalPartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationalPartners
        fields = "__all__"
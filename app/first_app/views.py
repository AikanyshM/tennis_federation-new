from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from rest_framework.authentication import BaseAuthentication, BasicAuthentication, SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend, NumberFilter, FilterSet, ChoiceFilter
from rest_framework import filters
from .permissions import *
from rest_framework.viewsets import ModelViewSet
from django.db.models import Q
from itertools import chain
import json
from django.http import JsonResponse
from django.core import serializers


#About Federations

class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrAny, ]


#About Tennis Clubs

class ClubModelViewSet(ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [IsStaffOrAny, ]


#About trainers

class TrainerModelViewSet(ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = [IsStaffOrAny, ]


class CalendarFilter(FilterSet):
    start_month = NumberFilter(field_name='start_date', lookup_expr='month', distinct=True)
    start_year = NumberFilter(field_name='start_date', lookup_expr='year', distinct=True)
    category_gender = ChoiceFilter(choices=Gender.choices, field_name='category_gender', distinct=True)
    category_age = ChoiceFilter(choices=Age.choices, field_name='category_age', distinct=True)


    class Meta:
        model = Calendar
        fields = ['category_gender', 'category_age', 'start_month', 'start_year',]


class CalendarViewSet(ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter,]
    filterset_class = CalendarFilter
    search_fields = ('translations__name',)
    ordering = ['start_date']
    permission_classes = [IsStaffOrAny,]


class RatingFilter(FilterSet):
    category_gender = ChoiceFilter(choices=Gender.choices, field_name='category_gender', distinct=True)
    category_age = ChoiceFilter(choices=Age.choices, field_name='category_age', distinct=True)


    class Meta:
        model = Rating
        fields = ['category_gender', 'category_age',]


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RatingFilter
    permission_classes = [IsStaffOrAny,]


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.OrderingFilter,]
    ordering = ['date']
    permission_classes = [IsStaffOrAny,]
    

class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    filter_backends = [filters.OrderingFilter,]
    ordering = ['date_added']
    permission_classes = [IsStaffOrAny,]


class NewsImagesViewSet(ModelViewSet):
    queryset = NewsImages.objects.all()
    serializer_class = NewsImagesSerializer
    permission_classes = [IsStaffOrAny,]


class GalleryImagesViewSet(ModelViewSet):
    queryset = GalleryImages.objects.all()
    serializer_class = GalleryImagesSerializer
    permission_classes = [IsStaffOrAny,]


# class GlobalSearchList(TranslatableSlugMixin, ListAPIView):
#     serializer_class = GlobalSearchSerializer

#     def list(self, request):
#         search = self.request.query_params.get('query', None)
#         category = Category.objects.filter(Q(translations__title__icontains=search) | Q(translations__text__icontains=search))
#         club = Club.objects.filter(Q(translations__name__icontains=search) | Q(translations__description__icontains=search) | Q(translations__address__icontains=search) | Q(translations__contacts__icontains=search) | Q(translations__working_hours__icontains=search) | Q(instagram__icontains=search) | Q(facebook__icontains=search))
#         trainer = Trainer.objects.filter(Q(translations__name__icontains=search) | Q(translations__description__icontains=search) | Q(translations__address__icontains=search) | Q(translations__contacts__icontains=search))
#         calendar = Calendar.objects.filter(Q(translations__name__icontains=search) | Q(start_date__icontains=search) | Q(end_date__icontains=search) | Q(translations__location__icontains=search) | Q(category_gender__icontains=search) | Q(category_age__icontains=search))
#         rating = Rating.objects.filter(Q(translations__full_name__icontains=search) | Q(birth_date__icontains=search) | Q(number_of_tournaments__icontains=search) | Q(category_gender__icontains=search) | Q(category_age__icontains=search) | Q(points__icontains=search))
#         news = News.objects.filter(Q(translations__name__icontains=search) | Q(date__icontains=search) | Q(translations__description__icontains=search) | Q(translations__source__icontains=search))
#         gallery = Gallery.objects.filter(Q(date_added__icontains=search) | Q(translations__title__icontains=search))
#         all_results = list(chain(category, club, trainer, calendar, rating, news, gallery))
#         serialize_obj = serializers.serialize('json', all_results)
#         return JsonResponse(json.loads(serialize_obj), safe=False)


def search(request):
    search = request.GET.get("query", None)
    category = Category.objects.all()
    club = Club.objects.all()
    trainer = Trainer.objects.all()
    calendar = Calendar.objects.all()
    rating = Rating.objects.all()
    news = News.objects.all()
    gallery = Gallery.objects.all()


    if search:
        category = category.filter(Q(translations__title__icontains=search) | Q(translations__text__icontains=search))
        club = club.filter(Q(translations__name__icontains=search) | Q(translations__description__icontains=search) | Q(translations__address__icontains=search) | Q(translations__contacts__icontains=search) | Q(translations__working_hours__icontains=search) | Q(instagram__icontains=search) | Q(facebook__icontains=search))
        trainer = trainer.filter(Q(translations__name__icontains=search) | Q(translations__description__icontains=search) | Q(translations__address__icontains=search) | Q(translations__contacts__icontains=search))
        calendar = calendar.filter(Q(translations__name__icontains=search) | Q(start_date__icontains=search) | Q(end_date__icontains=search) | Q(translations__location__icontains=search) | Q(category_gender__icontains=search) | Q(category_age__icontains=search))
        rating = rating.filter(Q(translations__full_name__icontains=search) | Q(birth_date__icontains=search) | Q(number_of_tournaments__icontains=search) | Q(category_gender__icontains=search) | Q(category_age__icontains=search) | Q(points__icontains=search))
        news = news.filter(Q(translations__name__icontains=search) | Q(date__icontains=search) | Q(translations__description__icontains=search) | Q(translations__source__icontains=search))
        gallery = gallery.filter(Q(date_added__icontains=search) | Q(translations__title__icontains=search))

        category = CategorySerializer(category, many=True).data
        club = ClubSerializer(club, many=True).data
        trainer = TrainerSerializer(trainer, many=True).data
        calendar = CalendarSerializer(calendar, many=True).data
        rating = RatingSerializer(rating, many=True).data
        news = NewsSerializer(news, many=True).data
        gallery = GallerySerializer(gallery, many=True).data

        all_results = list(chain(category, club, trainer, calendar, rating, news, gallery))

    return JsonResponse(all_results, safe=False)


class MainPageViewSet(ModelViewSet):
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer
    permission_classes = [IsStaffOrAny,]
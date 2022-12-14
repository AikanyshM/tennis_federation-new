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
from rest_framework.response import Response


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

    def get_serializer_context(self, request):
        context = super().get_serializer_context()
        context.update({"request": request})
        return context


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
        category = category.filter(Q(translations__title__icontains=search) | Q(translations__text__icontains=search)).distinct()
        club = club.filter(Q(translations__name__icontains=search) | Q(translations__description__icontains=search) | Q(translations__address__icontains=search) | Q(translations__contacts__icontains=search) | Q(translations__working_hours__icontains=search) | Q(instagram__icontains=search) | Q(facebook__icontains=search)).distinct()
        trainer = trainer.filter(Q(translations__name__icontains=search) | Q(translations__description__icontains=search) | Q(translations__address__icontains=search) | Q(translations__contacts__icontains=search)).distinct()
        calendar = calendar.filter(Q(translations__name__icontains=search) | Q(start_date__icontains=search) | Q(end_date__icontains=search) | Q(translations__location__icontains=search) | Q(category_gender__icontains=search) | Q(category_age__icontains=search)).distinct()
        rating = rating.filter(Q(translations__full_name__icontains=search) | Q(birth_date__icontains=search) | Q(number_of_tournaments__icontains=search) | Q(category_gender__icontains=search) | Q(category_age__icontains=search) | Q(points__icontains=search)).distinct()
        news = news.filter(Q(translations__name__icontains=search) | Q(date__icontains=search) | Q(translations__description__icontains=search) | Q(translations__source__icontains=search)).distinct()
        gallery = gallery.filter(Q(date_added__icontains=search) | Q(translations__title__icontains=search)).distinct()

    return JsonResponse({"category": CategorySerializer(category, many=True, context = {'request':request}).data,
                        "club": ClubSerializer(club, many=True, context = {'request':request}).data,
                        "trainer": TrainerSerializer(trainer, many=True, context = {'request':request}).data,
                        "calendar": CalendarSerializer(calendar, many=True, context = {'request':request}).data,
                        "rating": RatingSerializer(rating, many=True, context = {'request':request}).data,
                        "news": NewsSerializer(news, many=True, context = {'request':request}).data,
                        "gallery": GallerySerializer(gallery, many=True, context = {'request':request}).data})


class MainPageViewSet(ModelViewSet):
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer
    permission_classes = [IsStaffOrAny,]


class OfficialPartnerViewSet(ModelViewSet):
    queryset = OfficialPartner.objects.all()
    serializer_class = OfficialPartnerSerializer
    permission_classes = [IsStaffOrAny,]


class SponsorsAndPartnersViewSet(ModelViewSet):
    queryset = SponsorsAndPartners.objects.all()
    serializer_class = SponsorsAndPartnersSerializer
    permission_classes = [IsStaffOrAny,]


class InformationalPartnersViewSet(ModelViewSet):
    queryset = InformationalPartners.objects.all()
    serializer_class = InformationalPartnersSerializer
    permission_classes = [IsStaffOrAny,]

    
    
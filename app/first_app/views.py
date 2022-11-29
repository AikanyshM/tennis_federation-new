from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from rest_framework.authentication import BaseAuthentication, BasicAuthentication, SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend, NumberFilter, FilterSet
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
    start_month = NumberFilter(field_name='start_date', lookup_expr='month')
    start_year = NumberFilter(field_name='start_date', lookup_expr='year')
    end_month = NumberFilter(field_name='end_date', lookup_expr='month')
    end_year = NumberFilter(field_name='end_date', lookup_expr='year')

    class Meta:
        model = Calendar
        fields = ['translations__category_gender', 'translations__category_age', 'start_month', 'start_year', 'end_month', 'end_year']


class CalendarViewSet(ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter,]
    filterset_class = CalendarFilter
    search_fields = ('translations__name',)
    ordering_fields = ['start_date', ]
    permission_classes = [IsStaffOrAny,]


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['translations__category_gender', 'translations__category_age']
    permission_classes = [IsStaffOrAny,]


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.OrderingFilter,]
    ordering_fields = ['date', ]
    permission_classes = [IsStaffOrAny,]
    
class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    filter_backends = [filters.OrderingFilter,]
    ordering_fields = ['date_added', ]
    permission_classes = [IsStaffOrAny,]


class NewsImagesViewSet(ModelViewSet):
    queryset = NewsImages.objects.all()
    serializer_class = NewsImagesSerializer
    permission_classes = [IsStaffOrAny,]


class GalleryImagesViewSet(ModelViewSet):
    queryset = GalleryImages.objects.all()
    serializer_class = GalleryImagesSerializer
    permission_classes = [IsStaffOrAny,]


class GlobalSearchList(ListAPIView):
    serializer_class = GlobalSearchSerializer

    def list(self, request, *args, **kwargs):
        search = self.request.query_params.get('query', None)
        category = Category.objects.filter(Q(title__icontains=search) | Q(text__icontains=search))
        club = Club.objects.filter(Q(name__icontains=search) | Q(description__icontains=search) | Q(address__icontains=search) | Q(contacts__icontains=search) | Q(working_hours__icontains=search) | Q(Instagram__icontains=search) | Q(Facebook__icontains=search) | Q(images__icontains=search))
        trainer = Trainer.objects.filter(Q(name__icontains=search) | Q(description__icontains=search) | Q(address__icontains=search) | Q(contacts__icontains=search) | Q(images__icontains=search))
        calendar = Calendar.objects.filter(Q(name__icontains=search) | Q(date__icontains=search) | Q(location__icontains=search) | Q(category_gender__icontains=search) | Q(category_age__icontains=search))
        rating = Rating.objects.filter(Q(number__icontains=search) | Q(full_name__icontains=search) | Q(birth_date__icontains=search) | Q(number_of_tournaments__icontains=search) | Q(category_gender__icontains=search) | Q(category_age__icontains=search) | Q(points__icontains=search))
        news = News.objects.filter(Q(name__icontains=search) | Q(date__icontains=search) | Q(description__icontains=search) | Q(source__icontains=search) | Q(main_photo__icontains=search))
        gallery = Gallery.objects.filter(Q(main_image__icontains=search) | Q(date_added__icontains=search) | Q(title__icontains=search))
        mainpage = MainPage.objects.filter(Q(main_photo__icontains=search) | Q(whatsapp__icontains=search) | Q(facebook__icontains=search) | Q(instagram__icontains=search))
        all_results = list(chain(category, club, trainer, calendar, rating, news, gallery, mainpage))
        serialize_obj = serializers.serialize('json', all_results)
        return JsonResponse(json.loads(serialize_obj), safe=False)


class MainPageViewSet(ModelViewSet):
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer
    permission_classes = [IsStaffOrAny,]
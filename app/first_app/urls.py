from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', CategoryModelViewSet, basename="federation")
router.register(r'club', ClubModelViewSet, basename="club")
router.register(r'trainer', TrainerModelViewSet, basename="trainer")
router.register(r'calendar', CalendarViewSet, basename='calendar')
router.register(r'rating', RatingViewSet, basename='rating')
router.register(r'news', NewsViewSet, basename='news')
router.register(r'news_images', NewsImagesViewSet, basename='news_images')
router.register(r'gallery', GalleryViewSet, basename='gallery')
router.register(r'gallery_photos', GalleryImagesViewSet, basename='gallery_photos')
router.register(r'main_page', MainPageViewSet, basename='main_page')



urlpatterns = [
    path('', include(router.urls)),
    path('search/', GlobalSearchList.as_view(), name='search'),
]



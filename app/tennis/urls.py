from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

schema_view = get_schema_view(
   openapi.Info(
      title="Tennis API",
      default_version='v1-alpha',
      description="Description of Tennis API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="No License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('first_app.urls')),
    path('auth/', include('account.urls')),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
    path('api-json', schema_view.without_ui(cache_timeout=0), name='api-json'),
    path('rosetta/', include('rosetta.urls')),


 ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



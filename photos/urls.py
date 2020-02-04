from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',views.welcome,name='Welcome'),
    url(r'^categories/',views.category,name='category'),
    url(r'^pictures/',views.photos,name='images')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


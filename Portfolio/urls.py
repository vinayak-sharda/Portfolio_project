
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import jobs.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.homepage, name='home'),
    path('', blog.views.homepage, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

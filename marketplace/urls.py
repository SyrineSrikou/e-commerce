from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls', namespace='authentication')),
    path('', include('discover.urls', namespace='discover')),
    path('', include('store.urls', namespace='store')),
    path('', include('dashboard.urls', namespace='user_dashboard')),

]

 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
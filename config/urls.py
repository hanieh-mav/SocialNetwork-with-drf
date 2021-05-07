from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',include('posts.urls')),
    path('account/',include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('postapi.urls')),
    path('api/account/', include('accountapi.urls')),
    path('api-auth/', include('rest_framework.urls'))
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

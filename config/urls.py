from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from dj_rest_auth.views import PasswordResetConfirmView


urlpatterns = [
    path('',include('posts.urls')),
    path('account/',include('accounts.urls')),
    path('story/',include('story.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('postapi.urls')),
    path('api/account/', include('accountapi.urls')),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

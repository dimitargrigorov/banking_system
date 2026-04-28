from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='posts:welcome', permanent=False)),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
    path('bank/', include('bank.urls')),
    path('account/', include('account.urls')),
]

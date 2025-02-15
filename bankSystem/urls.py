from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('about/', views.about),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
    path('bank/', include('bank.urls')),
    path('account/', include('account.urls'))
    
]
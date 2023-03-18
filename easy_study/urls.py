
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('title.urls')),
    #favicon setting
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True))
]

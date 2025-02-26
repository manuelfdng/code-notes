# myproject/urls.py
from django.contrib import admin
from django.urls import path
from gunpla.views import GunplaList, GunplaDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gunplas', GunplaList.as_view()),  # Matches GET/POST /gunplas
    path('gunplas/<int:pk>', GunplaDetail.as_view()),  # Matches GET/PUT/DELETE /gunplas/<pk>
]

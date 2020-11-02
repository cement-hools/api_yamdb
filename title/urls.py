from django.urls import path, include
from rest_framework.routers import DefaultRouter

from title import views, script_for_bd
from title.views import TitlesViewSet

title_router = DefaultRouter()
title_router.register('titles', TitlesViewSet, basename='title')

urlpatterns = [

    path("", views.index, name="index"),
    path("csv", script_for_bd.fill_tables, name="create_category"),
    path('v1/', include(title_router.urls)),

]

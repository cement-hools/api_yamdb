from django.urls import path

from title import views, script_for_bd

urlpatterns = [

    path("", views.index, name="index"),
    path("csv", script_for_bd.fill_tables, name="create_category"),

]

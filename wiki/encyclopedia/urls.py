from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random",views.rando,name='random'),
    path("newpage",views.newpage,name='newpage'),
    path("edit/<str:title>",views.edit,name="edit"),
    path("wiki/<str:text>",views.text,name="text"),
    path("result",views.search,name="search"),
    path("<str:text>",views.text,name="indexx"),
    
]
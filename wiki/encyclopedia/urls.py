from django.urls import path

from . import views
appname = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.view_Title, name ="title"),
    path("wiki/new_entry/", views.New_Page, name ="New_Page"),
    path("wiki/edit_entry/<str:entry>", views.edit_page, name ="edit_Page"),
    path(r'?q=$',views.searchposts,name="search_res")
]

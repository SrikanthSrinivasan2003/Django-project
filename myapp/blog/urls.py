from django.urls import path
from . import views


app_name = "Blogs"

urlpatterns = [
    path("",views.index , name="index"),
    path("post/<str:post_id>",views.detail,name="detail"),
    path("new_something",views.new_url_view , name="new_page_url"),
    path("old_url",views.old_url_redirect , name="old_url")
]
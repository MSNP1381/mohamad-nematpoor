
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from . import views
app_name='blogy'
urlpatterns = [
    path('', views.blogs,name="all_blogs"),
    path('<int:blog_id>/', views.details,name="details"),
]
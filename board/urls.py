from django.urls import path
from django.views.generic import ListView, DetailView
from board.models import Articles
from django.conf.urls import url
from . import views

urlpatterns = [

    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
    template_name="board/posts.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Articles, template_name = "board/post.html"))
]

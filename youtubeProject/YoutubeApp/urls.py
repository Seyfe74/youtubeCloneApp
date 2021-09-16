from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.CommentList.as_view()),
    path('reply/', views.ReplyList.as_view()),
    path('comment/<str:videoId>/', views.CommentDetail.as_view())
]
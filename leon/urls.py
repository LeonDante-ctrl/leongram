from django.urls import path, include
from .views import (
    PostDetailView,
    PostListView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
    
)

app_name = 'leon'

urlpatterns = [
    #local : http://127.0.0.1:8000/
    path('',PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name = 'create'),
    path('<int:id>' , PostDetailView.as_view(), name='post_detail'),
    path('<int:id>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:id>/delete/', PostDeleteView.as_view(), name='post_delete'),
]

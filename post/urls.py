from django.urls import path

from post import views

urlpatterns = [
    path('new_blog/', views.PostCreateView.as_view(), name='new-blog')
]
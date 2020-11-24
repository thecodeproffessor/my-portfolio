from django.urls import path
from core import views
from core.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view()),
    path('portfolio/<int:id>/', views.detail_view, name='detail'),
    path('article/<int:id>/', views.blog, name='blog-view'),
]

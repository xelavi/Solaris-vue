from django.urls import path, include

from character import views

urlpatterns = [
    path('characters/', views.CharactersList.as_view()),
    path('characters/<slug:character_slug>/', views.CharacterDetail.as_view()),
]
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import Http404

from .models import Character

from .serializers import CharacterSerializer

class CharactersList(APIView):
    def get(self, request, format=None):
        characters = Character.objects.all()[0:4]
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)
    

class CharacterDetail(APIView):
    def get_object(self, character_slug):
        try:
            return Character.objects.get(slug = character_slug)
        except Character.DoesNotExist:
            raise Http404
        
    def get(self, request, character_slug, format=None):
        character = self.get_object(character_slug)
        serializer = CharacterSerializer(character)
        return(Response(serializer.data))
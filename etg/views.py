from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tag
from rest_framework.viewsets import ModelViewSet
from .serializers import TagSerializer


class TagMVS(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
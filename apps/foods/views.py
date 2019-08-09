from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ShopInfoSerializer, TagsSerializer
from .models import ShopInfo,Tags



class ShopInfoViewSet(viewsets.ModelViewSet):
    """
    店铺
    """
    queryset = ShopInfo.objects.all()
    serializer_class = ShopInfoSerializer

class TagsViewSet(viewsets.ModelViewSet):
    """
    标签
    """
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
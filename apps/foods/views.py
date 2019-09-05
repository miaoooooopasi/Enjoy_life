# coding=utf-8
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import viewsets, generics, mixins
from .serializers import ShopInfoSerializer, TagsSerializer, UploadImageSerializer, CommentSerializer
from .models import ShopInfo, Tags, UploadImage, Comment


class ShopInfoModelViewSet(viewsets.ModelViewSet):
    """
    店铺
    """
    queryset = ShopInfo.objects.all()
    serializer_class = ShopInfoSerializer


class TagsModelViewSet(viewsets.ModelViewSet):
    """
    标签
    """
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class UploadImageModelViewSet(viewsets.ModelViewSet):

    """图片"""

    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer


class CommentModelViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """评论"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('ShopInfo',)
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import ShopInfo, Tags, UploadImage, Comment


class UploadImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadImage
        fields = "__all__"


class TagsSerializer(serializers.ModelSerializer):
    # click_num = serializers.IntegerField(default=0)

    class Meta:
        model = Tags
        fields = "__all__"


class ShopInfoSerializer(WritableNestedModelSerializer):

    img = UploadImageSerializer()

    class Meta:
        model = ShopInfo
        fields = "__all__"


class CommentSerializer(WritableNestedModelSerializer):

    # ShopInfo = ShopInfoSerializer()

    class Meta:
        model = Comment
        fields = "__all__"

from rest_framework import serializers
from .models import ShopInfo, Tags


class TagsSerializer(serializers.ModelSerializer):
    # click_num = serializers.IntegerField(default=0)

    class Meta:
        model = Tags
        fields = "__all__"


class ShopInfoSerializer(serializers.ModelSerializer):
    click_num = serializers.IntegerField(default=0)
    tags = TagsSerializer()

    class Meta:
        model = ShopInfo
        fields = "__all__"

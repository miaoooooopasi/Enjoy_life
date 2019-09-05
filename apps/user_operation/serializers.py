# 收藏详情
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from foods.serializers import ShopInfoSerializer
from user_operation.models import UserFav, UserLeavingMessage
# from .models import UserFav, UserLeavingMessage


class UserFavDetailSerializer(serializers.ModelSerializer):
    shopinfo = ShopInfoSerializer(many=True)

    class Meta:
        model = UserFav
        fields = ("ShopInfo", "id")


# 用户收藏
class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        # 联合唯一可以在 model 中创建的时候进行操作, 通过 ModelSerializer 自然会帮你完成验证
        # 也可以在这里完成, 注意是在 Meta 中进行设置, 因为这是多字段的处理
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'ShopInfo'),
                message="已经收藏过了"
            )
        ]
        fields = ("user", "ShopInfo", "id")  # 删除的需要因此加上 id, 这样方便删除操作


# 用户留言
class LeavingMessageSerializer(serializers.ModelSerializer):
    # 设置隐藏字段
    user = serializers.HiddenField(
        # 默认值为当前用户
        default=serializers.CurrentUserDefault()
    )
    # 留言的时间不能自己指定, 应该是系统自动根据当前的时间, 因此设置为只读
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserLeavingMessage
        fields = '_all_'

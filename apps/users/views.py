from random import choice

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status, mixins, permissions
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework_jwt.utils import jwt_encode_handler

from Enjoy_life.settings import APIKEY
from users.serializers import SmsSerializer, UserSerializers, UserRegisterSerializer, UserDetailSerializer
from utils.tengxun import TengXun
from .models import VerifyCode, UserProfile

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class SmsCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送短信验证码
    """
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data["mobile"]

        teng_xun = TengXun(APIKEY)

        code = self.generate_code()

        sms_status = teng_xun.send_sms(code=code, mobile=mobile)

        if sms_status["result"] != 0:
            return Response({
                "mobile": sms_status["errmsg"]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            code_record = VerifyCode(code=code, mobile=mobile)
            code_record.save()
            return Response({
                "mobile": mobile,
                'code': code
            }, status=status.HTTP_201_CREATED)


class UserRegisterSerializerModelViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin,
                                         mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户注册
    """
    queryset = UserProfile.objects.all()
    # serializer_class = UserRegisterSerializer

    # 不同的action 不同的序列化
    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return UserRegisterSerializer
        return UserDetailSerializer

    # permission_classes = (permissions.IsAuthenticated, )
    #  因为根据类型的不同权限的认证也不同, 不能再统一设置了
    # get_permissions 的源码在 APIview 中
    def get_permissions(self):
        if self.action == "retrieve":
            return [permissions.IsAuthenticated()]
        if self.action == "update":
            return [permissions.IsAuthenticated()]
        elif self.action == "create":
            return []
        elif self.action == "list":
            return [permissions.IsAdminUser()]
        return []

    # 重写 create 函数来完成注册后自动登录功能
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        # token 的添加只能用此方法, 此方法通过源码阅读查找到位置为
        re_dict["token"] = jwt_encode_handler(payload)
        # 自定义一个字段加入进去
        re_dict["username"] = user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()


class UserProfileModelViewSet(viewsets.ModelViewSet):
    """
    用户
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializers


# 自定义登陆认证
class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 用户名和手机都能登录
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None


# register
def register(request):
    return render(request, 'users/register.html')
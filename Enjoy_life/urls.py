"""Enjoy_life URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, re_path
from django.urls.conf import include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt import views
from django.views.static import serve

import xadmin
from Enjoy_life import settings
from Enjoy_life.settings import MEDIA_ROOT
from apps.foods.views import ShopInfoModelViewSet, UploadImageModelViewSet, CommentModelViewSet, TagsModelViewSet
# from user_operation.views import UserFavViewset, LeavingMessageViewset
from users.views import SmsCodeViewset, UserRegisterSerializerModelViewSet, UserProfileModelViewSet


from users import views as user_views

router = routers.DefaultRouter()
# shoinfo 接口
router.register('ShopInfo', ShopInfoModelViewSet, base_name='ShopInfo')
# tags接口
router.register('Tags', TagsModelViewSet, base_name='Tags')
# UploadImage接口
router.register('UploadImage', UploadImageModelViewSet, base_name='UploadImage')
# Comment接口
router.register('Comment', CommentModelViewSet, base_name='Comment')
# 短信接口
router.register('get_mobile_code', SmsCodeViewset, base_name='get_mobile_code')
# 用户注册接口
router.register('User_RegisterBymoblie', UserRegisterSerializerModelViewSet, base_name='User_RegisterBymoblie')
# 用户接口
# router.register('UserProfile', UserProfileModelViewSet, base_name='UserProfile')

# 用户收藏
# router.register('UserFavView', UserFavViewset, base_name='UserFavView')
# 用户留样 LeavingMessageViewset
# router.register('LeavingMessageView', LeavingMessageViewset, base_name='LeavingMessageView')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('register/', user_views.register, name='register'),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
    path('jwt-auth/', views.obtain_jwt_token),
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='API')),

]

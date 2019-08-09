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
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt import views

import xadmin
from Enjoy_life.settings import MEDIA_ROOT
from apps.foods.views import ShopInfoViewSet,TagsViewSet

router = routers.DefaultRouter()
# shoinfo 接口
router.register('ShopInfo',ShopInfoViewSet,base_name='ShopInfo')
router.register('Tags',TagsViewSet,base_name='Tags')

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # jwt token login
    path('jwt-auth/', views.obtain_jwt_token),
    # drf 注册路由
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='API')),
    # path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
]

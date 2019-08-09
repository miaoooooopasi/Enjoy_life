import xadmin

from .models import ShopInfo, Tags, UploadImage
from xadmin import views


# shoponfo
class ShopInfoAdmin(object):
    # 图标设置
    model_icon = 'fa fa-arrows'
    # 搜索字段
    search_fields = ('name',)
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)


xadmin.site.register(ShopInfo, ShopInfoAdmin)

# tags
class TagsAdmin(object):
    # 图标设置
    model_icon = 'fa fa-home'
    # 搜索字段
    search_fields = ('tag_name',)
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)


xadmin.site.register(Tags, TagsAdmin)

# UploadImage
class UploadImageAdmin(object):
    # 图标设置
    model_icon = 'fa fa-file-text'
    # 搜索字段
    search_fields = ('name',)
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('id',)


xadmin.site.register(UploadImage, UploadImageAdmin)


# 全局设置
class GlobalSetting(object):
    site_title = "好吃一条街"  # 页面左上角title内容
    site_footer = "LEON"       # 页脚内容
    menu_style = 'accordion'   # 左边导航栏 收缩 手风琴


xadmin.site.register(views.CommAdminView, GlobalSetting)

from django.db import models
from datetime import datetime

# Create your models here.
# 标签表
from stdimage.models import StdImageField

# 热搜
class HotSearchWords(models.Model):
    """
    搜索栏下方热搜词
    """
    keywords = models.CharField("热搜词", default="", max_length=20)
    index = models.IntegerField("排序", default=0)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = '热搜排行'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords


class Tags(models.Model):
    """
    标签
    """
    tag_name = models.CharField(max_length=20, verbose_name='标签名')

    class Meta:
        verbose_name = '标签页'
        verbose_name_plural = "标签"

    def __str__(self):
        return self.tag_name


class UploadImage(models.Model):
    """上传图片功能"""
    name = models.CharField(max_length=30, verbose_name="名称", default="")  # 标题
    image = StdImageField(max_length=100,
                          upload_to='path/to',
                          verbose_name=u"传图片",
                          variations={'thumbnail': {'width': 100, 'height': 75}})
    # 时间可编辑
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    def url(self):
        if self.image:
            return self.image.url
        else:
            return "url为空"

    def image_img(self):
        if self.image:
            href = self.image.url  # 点击后显示的放大图片
            src = self.image.thumbnail.url  # 页面显示的缩略图
            # 插入html代码
            image_html = '<a href="%s" target="_blank" title="传图片"><img alt="" src="%s"/>' % (href, src)
            return image_html
        else:
            return '上传图片'

    image_img.short_description = '图片'
    image_img.allow_tags = True  # 列表页显示图片

    class Meta:
        verbose_name = "传图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ShopInfo(models.Model):
    """
    美食店信息表
    """
    # 推荐等级:Recommendation Level
    Recommendation_Level = (
        (1, "一级"),
        (2, "二级"),
        (3, "三级"),
    )

    name = models.CharField('美食店名', default="", max_length=30, help_text="美食店名")
    level = models.IntegerField("等级", choices=Recommendation_Level, help_text="等级")
    desc = models.TextField("等级描述", default="", help_text="等级描述")
    add_time = models.DateTimeField("添加时间", default=datetime.now)
    counts = models.IntegerField("点赞数", default=0, help_text="点赞数")
    tags = models.ManyToManyField(Tags, verbose_name=u'店铺标签', blank=True)
    img = models.ForeignKey(UploadImage, verbose_name=u'封面', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "美食店信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.location_name


# 评论表
class Comment(models.Model):
    """
    评论
    """
    name = models.CharField(max_length=20, default=u'佚名', verbose_name=u'姓名')
    content = models.TextField(verbose_name=u'内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    ShopInfo = models.ForeignKey(ShopInfo, on_delete=models.CASCADE, verbose_name=u'店铺')

    class Meta:
        verbose_name = '评论管理'
        verbose_name_plural = "评论"
        ordering = ['-create_time']

    def __str__(self):
        return self.name




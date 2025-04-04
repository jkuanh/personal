from django.db import models
from wangeditor.fields import WangRichTextField


class Article(models.Model):
    title = models.CharField(verbose_name="标题", max_length=100)
    author = models.CharField(verbose_name="作者", max_length=50)
    description = models.TextField(verbose_name="摘要")
    content = WangRichTextField(verbose_name="内容")
    views = models.IntegerField(verbose_name="浏览量", default=0)
    publish_time = models.DateTimeField(verbose_name="发布时间", auto_now_add=True)

    class Meta:
        db_table = "tb_article"
        verbose_name = "文章列表"
        verbose_name_plural = verbose_name


class Image(models.Model):
    title = models.CharField(verbose_name="标题", max_length=100)
    image = models.ImageField(verbose_name="上传图片", upload_to="")
    description = models.TextField(verbose_name="简介")
    views = models.IntegerField(verbose_name="浏览量", default=0)
    publish_time = models.DateTimeField(verbose_name="上传时间", auto_now_add=True)

    class Meta:
        db_table = "tb_image"
        verbose_name = "图片列表"
        verbose_name_plural = verbose_name

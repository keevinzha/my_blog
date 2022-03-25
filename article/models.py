from django.db import models

# Create your models here.
# django内建User模型
from django.contrib.auth.models import User
from django.utils import timezone

# 文章数据模型
class ArticlePost(models.Model):

    # 作者，级联删除
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 文章标题
    title = models.CharField(max_length=100)
    # 文章正文，保存大量文本
    body = models.TextField()
    # 文章创建时间
    created = models.DateTimeField(default=timezone.now())
    # 修改时间，auto_now=True自动写入每次更新时间
    updated = models.DateTimeField(auto_now=True)

    # 定义元数据
    class Meta:
       # 模型返回的数据按创建时间倒序排列
        ordering = ('-created',)
    def __str__(self):
        # 返回文章的标题
        return self.title


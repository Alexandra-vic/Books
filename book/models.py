from django.db import models
from category.models import Category, Tag
from user.models import User


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='название')
    category_id = models.ManyToManyField(Category, related_name='category', verbose_name='категории')
    author_id = models.ForeignKey(User, on_delete= models.CASCADE, related_name='author', verbose_name='автор')
    tags = models.ManyToManyField(Tag, related_name='tags', verbose_name='тэг')

    def __str__(self):
        return self.name

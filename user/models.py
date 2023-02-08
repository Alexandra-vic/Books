from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=50, blank=False, verbose_name='имя')
    # books = models.ForeignKey()

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import AbstractUser, Group

###########--- CUSTOMER ---###########
class User(models.Model):
    name = models.CharField("name", max_length=255, blank=True)
    document = models.CharField("document", max_length=20, blank=False)
    email = models.CharField("e-mail", max_length=255, blank=False)
    password = models.CharField("password", max_length=255, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "user"
        db_table = "user"
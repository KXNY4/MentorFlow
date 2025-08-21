from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..topic.models import Topic


class User(AbstractUser):
    is_mentor = models.BooleanField(default=False, verbose_name=_("ментор?"))
    bio = models.TextField(blank=True, verbose_name=_("биография"))
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name=_("аватарка"))
    expertise = models.ManyToManyField(Topic, blank=True, verbose_name=_("тематика"))

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")
        ordering = ["-date_joined"]
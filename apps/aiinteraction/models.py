from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from ..topic.models import Topic

User = get_user_model()


class AIinteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, verbose_name=_("Тематика"))
    prompt = models.TextField(verbose_name=_("Подсказка"))
    response = models.TextField(verbose_name=_("Ответ"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Создано"))
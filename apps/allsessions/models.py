from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices

from ..topic.models import Topic


User = get_user_model()

SESSION_TYPE = Choices(
    ("mentoring", _("Mentoring")),
    ("interview", _("Interview"))
)

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessions', verbose_name=_("Пользователь"))
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentored_sessions', verbose_name=_("Ментор"))
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, verbose_name=_("Тематика"))
    schedulet_at = models.DateTimeField(verbose_name=_("Запланировано"))
    duration_minutes = models.PositiveIntegerField(default=30, verbose_name=_("Продолжительность"))
    type = models.CharField(max_length=20, choices=SESSION_TYPE, default=SESSION_TYPE.mentoring, verbose_name=_("Тип сессии"))
    is_completed = models.BooleanField(default=False, verbose_name=_("Закончен"))
    feedback = models.TextField(blank=True, verbose_name=_("Обратная связь"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Создано"))

    class Meta:
        verbose_name = _("Сессия")
        verbose_name_plural = _("Сессий")
        ordering = ["-created_at"]


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    title = models.CharField(max_length=255, verbose_name=_("Заголовок"))
    description = models.TextField(blank=True, verbose_name=_("Описание"))
    is_completed = models.BooleanField(default=False, verbose_name=_("Достигнут"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Создано"))
    deadline = models.DateField(null=True, blank=True, verbose_name=_("Срок"))

    class Meta:
        verbose_name = _("Цель")
        verbose_name_plural = _("Цели")
        ordering = ["-created_at"]


class MentorReview(models.Model):
    session = models.OneToOneField(Session, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Оценка")
        verbose_name_plural = _("Оценки")
        ordering = ["-created_at"]


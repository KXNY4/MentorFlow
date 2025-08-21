from django.db import models
from django.utils.translation import gettext_lazy as _


class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("имя"))
    description = models.TextField(blank=True, verbose_name=_("описание"))

    def __str__(self):
        return str(_(self.name))
    
    class Meta:
        verbose_name = _("Тема")
        verbose_name_plural = _("Темы")
        ordering = ["-name"]

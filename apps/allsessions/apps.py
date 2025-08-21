from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AllsessionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.allsessions"
    verbose_name = _("Сессий")

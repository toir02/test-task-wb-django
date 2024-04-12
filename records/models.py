from django.db import models


class Record(models.Model):
    data = models.JSONField(verbose_name="Данные для записи")

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"

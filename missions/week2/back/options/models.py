from django.db import models
from core import models as core_models


class Color(core_models.TimeStampedModel):

    color = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "색상"
        verbose_name = "색상"

    def __str__(self) -> str:
        return self.color


class size(core_models.TimeStampedModel):

    size = models.CharField(max_length=10)

    class Meta:
        abstract = True

    def __str__(self):
        return self.size


class size_upper(size):
    class Meta:
        verbose_name_plural = "사이즈(상의)"
        verbose_name = "사이즈"


class size_outer(size):
    class Meta:
        verbose_name_plural = "사이즈(아우터)"
        verbose_name = "사이즈"


class size_onepiece(size):
    class Meta:
        verbose_name_plural = "사이즈(원피스)"
        verbose_name = "사이즈"

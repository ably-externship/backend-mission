from django.db import models
from core import models as core_models


class Uppers_photo(core_models.TimeStampedModel):

    clothes = models.ForeignKey(
        "Upper",
        related_name="upper_photos",
        on_delete=models.CASCADE,
        verbose_name="상품명",
    )

    file = models.ImageField(upload_to="upper")

    class Meta:
        verbose_name_plural = "상의사진"


class Outers_photo(core_models.TimeStampedModel):

    clothes = models.ForeignKey(
        "Outers",
        related_name="outers_photos",
        on_delete=models.CASCADE,
        verbose_name="상품명",
    )

    file = models.ImageField(upload_to="outer")

    class Meta:
        verbose_name_plural = "아우터 사진"


class Onepieces_photo(core_models.TimeStampedModel):

    clothes = models.ForeignKey(
        "Onepieces",
        related_name="onepieces_photos",
        on_delete=models.CASCADE,
        verbose_name="상품명",
    )

    file = models.ImageField(upload_to="onepiece")

    class Meta:
        verbose_name_plural = "원피스 사진"


class clothes(core_models.TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name="상품명")
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(verbose_name="가격")

    class Meta:
        abstract = True


class Upper(clothes):

    host = models.ForeignKey(
        "users.User", related_name="upper", on_delete=models.CASCADE
    )

    colors = models.ManyToManyField(
        "options.Color", related_name="upper", verbose_name="색상", blank=True
    )

    size_upper = models.ManyToManyField(
        "options.size_upper", related_name="upper", verbose_name="사이즈", blank=True
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "상의"


class Outers(clothes):

    host = models.ForeignKey(
        "users.User", related_name="outers", on_delete=models.CASCADE
    )

    colors = models.ManyToManyField(
        "options.Color", related_name="outers", verbose_name="색상", blank=True
    )

    size_outer = models.ManyToManyField(
        "options.size_outer", related_name="outers", verbose_name="사이즈", blank=True
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "아우터"


class Onepieces(clothes):

    host = models.ForeignKey(
        "users.User", related_name="onepieces", on_delete=models.CASCADE
    )

    colors = models.ManyToManyField(
        "options.Color", related_name="onepieces", verbose_name="색상", blank=True
    )

    size_onepiece = models.ManyToManyField(
        "options.size_onepiece",
        related_name="onepieces",
        verbose_name="사이즈",
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "원피스"

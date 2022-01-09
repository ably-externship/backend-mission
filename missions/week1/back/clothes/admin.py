from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe


class upper_photo(admin.TabularInline):
    model = models.Uppers_photo


class outer_photo(admin.TabularInline):
    model = models.Outers_photo


class onepiece_photo(admin.TabularInline):
    model = models.Onepieces_photo


@admin.register(models.Uppers_photo, models.Outers_photo, models.Onepieces_photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "clothes",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "썸네일"


@admin.register(models.Upper)
class UpperAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Clothes Info",
            {
                "fields": (
                    "name",
                    "description",
                    "colors",
                    "price",
                    "size_upper",
                    "host",
                ),
            },
        ),
    )
    filter_horizontal = ("size_upper", "colors")
    list_display = (
        "name",
        "color",
        "price",
        "host",
    )
    search_fields = ("name", "colors")
    raw_id_fields = ("host",)
    inlines = [
        upper_photo,
    ]

    def color(self, obj):
        c = obj.colors.all()
        color_list = []
        for co in c:
            color_list.append(co)
        return color_list if len(color_list) < 5 else color_list[:5]

    color.short_description = "색상"


@admin.register(models.Outers)
class OutersAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Clothes Info",
            {
                "fields": (
                    "name",
                    "description",
                    "colors",
                    "price",
                    "size_outer",
                    "host",
                ),
            },
        ),
    )
    filter_horizontal = ("size_outer", "colors")
    list_display = (
        "name",
        "color",
        "price",
        "host",
    )
    search_fields = ("name", "colors")
    raw_id_fields = ("host",)
    inlines = [
        outer_photo,
    ]

    def color(self, obj):
        c = obj.colors.all()
        color_list = []
        for co in c:
            color_list.append(co)
        return color_list if len(color_list) < 5 else color_list[:5]

    color.short_description = "색상"


@admin.register(models.Onepieces)
class OnepiecesAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Clothes Info",
            {
                "fields": (
                    "name",
                    "description",
                    "colors",
                    "price",
                    "size_onepiece",
                    "host",
                ),
            },
        ),
    )
    filter_horizontal = ("size_onepiece", "colors")
    list_display = (
        "name",
        "color",
        "price",
        "host",
    )
    search_fields = ("name", "colors")
    raw_id_fields = ("host",)
    inlines = [
        onepiece_photo,
    ]

    def color(self, obj):
        c = obj.colors.all()
        color_list = []
        for co in c:
            color_list.append(co)
        return color_list if len(color_list) < 5 else color_list[:5]

    color.short_description = "색상"


@admin.register(models.Upper_comment)
class UpperCommentAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Clothes Info",
            {
                "fields": (
                    "upper",
                    "content",
                    "Author",
                ),
            },
        ),
    )
    list_display = ("Author", "content", "created")
    raw_id_fields = ("Author",)


@admin.register(models.Outer_comment)
class OuterCommentAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Clothes Info",
            {
                "fields": (
                    "outer",
                    "content",
                    "Author",
                ),
            },
        ),
    )
    list_display = ("Author", "content", "created")
    raw_id_fields = ("Author",)


@admin.register(models.Onepiece_comment)
class OnepieceCommentAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Clothes Info",
            {
                "fields": (
                    "onepiece",
                    "content",
                    "Author",
                ),
            },
        ),
    )
    list_display = ("Author", "content", "created")
    raw_id_fields = ("Author",)

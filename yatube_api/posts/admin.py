from django.contrib import admin

from .models import Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "text",
        "pub_date",
        "author",
        "group",
    )
    list_editable = ("group",)
    list_filter = ("pub_date",)
    search_fields = ("text",)
    empty_value_display = "-пусто-"


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)

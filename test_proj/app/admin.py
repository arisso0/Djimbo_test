from django.contrib import admin
from .models import Page, Block, PageBlock


class PageBlockInline(admin.TabularInline):
    model = PageBlock


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "position", "updated", "created"]
    inlines = [PageBlockInline]


@admin.register(Block)
class PageAdmin(admin.ModelAdmin):
    list_display = ["name", "video_url", "shows_number", "updated", "created"]


from django.contrib import admin
from MessageBoard.models import Profile, Post

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "text",
        "publish_date",
        "published"
    )
    list_filter = (
        "published",
        "publish_date"
    )
    list_editable = (
        "publish_date",
        "published"
    )
    search_fields = (
        "text",
    )
    date_hierarchy = "publish_date"
    save_on_top = True
from django.contrib import admin
from app.models import Skills, Location, Author, JobPost

# Register your models here.


class LocationAdmin(admin.ModelAdmin):
    list_display = ("country", "state", "city", "street", "zip")
    search_fields = ("country", "state", "city", "street", "zip")
    search_help_text = "Search for Location"


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("__str__", "company", "designation")
    search_fields = ("name", "company")
    search_help_text = "Search for author by name, company"


class JobAdmin(admin.ModelAdmin):
    list_display = ("__str__", "title", "date", "salary", "location", "author")
    list_filter = ("title", "date", "types")
    search_fields = ("title", "description")
    search_help_text = "Search for jobs by title or description."
    fieldsets = [
        ("Basic Information", {
            "fields": [("title", "description"), "expiry", "salary"],
        }),
        ("More Information", {
            "fields": [("location", "author"), ("skills", "types")],
            "classes": ["wide", "collapse"]
        })
    ]


admin.site.register(Skills)
admin.site.register(Location, LocationAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(JobPost, JobAdmin)

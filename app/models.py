from django.db import models
from django.utils.text import slugify

# Create your models here.


class Skills(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Location(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country}, {self.zip}"


class Author(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class JobPost(models.Model):
    JOB_TYPE_CHOICES = [
        ("Full time", "Full time"),
        ("Part time", "Part time")
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    expiry = models.DateField(null=True)
    salary = models.IntegerField()
    slug = models.SlugField(unique=True, max_length=40, null=True)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    skills = models.ManyToManyField(Skills)
    types = models.CharField(max_length=200, choices=JOB_TYPE_CHOICES)

    def __str__(self) -> str:
        return f"{self.title} with salary {self.salary}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost, self).save(*args, **kwargs)

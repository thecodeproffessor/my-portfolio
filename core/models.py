from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class AboutME(models.Model):
    intro_text = models.CharField(max_length=100)
    strong_text = models.CharField(max_length=50)
    br_text = models.CharField(max_length=50)
    first_paragraph = models.CharField(max_length=150)
    second_paragraph = models.CharField(max_length=150)

    def __str__(self):
        return self.intro_text

    class Meta:
        verbose_name_plural = "About me"


class Experience(models.Model):
    skill_companyname = models.CharField(max_length=100)
    company_username = models.CharField(max_length=50)
    duration = models.CharField(max_length=100, null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    company_description = models.TextField()

    def __str__(self):
        return self.skill_companyname

class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonial_imgs')
    testimonial = models.CharField(max_length=100)
    founder_name = models.CharField(max_length=50)
    founder_title = models.CharField(max_length=50)

    def __str__(self):
        return self.founder_name

# Category


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Category name")

    def __str__(self):
        return self.title


class CategoryList(models.Model):
    categories = models.ManyToManyField(Category)


class Portfolios(models.Model):
    name = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='portfolio_imgs')
    date_posted = models.DateTimeField(default=timezone.now)
    client = models.CharField(max_length=50)
    completion = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    description = models.TextField()
    website_link = models.URLField(default="enter link", max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})


class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog-img')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    author_img = models.ImageField(upload_to='author-img')
    categories = models.ManyToManyField(Category)
    content = HTMLField()
    summary_text = models.CharField(max_length=100)

    def __str__(self):
        return self.title

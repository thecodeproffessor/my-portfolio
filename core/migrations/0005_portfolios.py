# Generated by Django 3.1.3 on 2020-11-23 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_category_categorylist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='portfolio_imgs')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', models.CharField(max_length=50)),
                ('completion', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('website_link', models.URLField(max_length=150)),
                ('categories', models.ManyToManyField(to='core.Category')),
            ],
        ),
    ]

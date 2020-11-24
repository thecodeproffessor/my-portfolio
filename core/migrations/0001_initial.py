# Generated by Django 3.1.3 on 2020-11-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutME',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro_text', models.CharField(max_length=100)),
                ('strong_text', models.CharField(max_length=50)),
                ('br_text', models.CharField(max_length=50)),
                ('first_paragraph', models.CharField(max_length=150)),
                ('second_paragraph', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name_plural': 'About me',
            },
        ),
    ]
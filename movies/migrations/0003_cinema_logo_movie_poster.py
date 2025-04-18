# Generated by Django 5.1.5 on 2025-02-01 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_remove_movie_day_remove_movie_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="cinema",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to="cinema_logos/"),
        ),
        migrations.AddField(
            model_name="movie",
            name="poster",
            field=models.ImageField(blank=True, null=True, upload_to="movie_posters/"),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-17 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('popularity', models.FloatField()),
                ('profile_path', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('popularity', models.FloatField()),
                ('profile_path', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('original_title', models.CharField(max_length=50)),
                ('poster_path', models.TextField(blank=True, null=True)),
                ('backdrop_path', models.TextField(blank=True, null=True)),
                ('overview', models.TextField()),
                ('release_date', models.CharField(max_length=50)),
                ('popularity', models.FloatField()),
                ('runtime', models.IntegerField(null=True)),
                ('tagline', models.TextField()),
                ('video', models.TextField()),
                ('vote_average', models.CharField(max_length=50)),
                ('vote_count', models.CharField(max_length=50)),
                ('actors', models.ManyToManyField(blank=True, to='movies.actor')),
                ('directors', models.ManyToManyField(blank=True, to='movies.director')),
                ('like_movie', models.ManyToManyField(related_name='liked_movies', to=settings.AUTH_USER_MODEL)),
                ('save_movie', models.ManyToManyField(related_name='saved_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('score', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

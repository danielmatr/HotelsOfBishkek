# Generated by Django 3.2.7 on 2022-02-21 11:16

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('text', models.TextField(default='more...')),
                ('min_price', models.PositiveSmallIntegerField(default=70)),
                ('wi_fi', models.CharField(choices=[('free Wi-Fi', 'free Wi-Fi'), ('No Wi-Fi', 'No Wi-Fi')], default='free Wi-Fi', max_length=20)),
                ('city', models.CharField(choices=[('Osh', 'Osh'), ('Bishkek', 'Bishkek'), ('Talas', 'Talas'), ('Batken', 'Batken'), ('Djalal-Abad', 'Djalal-Abad'), ('Naryn', 'Naryn'), ('I-K', 'I-K')], default='Bishkek', max_length=20)),
                ('star', models.CharField(choices=[('Star: 1', 'Star: 1'), ('Star: 2', 'Star: 2'), ('Star: 3', 'Star: 3'), ('Star: 4', 'Star: 4'), ('Star: 5', 'Star: 5')], default=1, max_length=20)),
                ('address', models.TextField(default='Bishkek')),
            ],
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='value')),
            ],
            options={
                'verbose_name': 'Rating Star',
                'verbose_name_plural': 'Rating Stars',
                'ordering': ['-value'],
            },
        ),
        migrations.CreateModel(
            name='Saved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved', to='main.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_p', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='main.post')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to=settings.AUTH_USER_MODEL)),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='main.ratingstar')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_likes', to=settings.AUTH_USER_MODEL)),
                ('liked_ads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads_likes', to='main.post')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.post')),
            ],
        ),
    ]

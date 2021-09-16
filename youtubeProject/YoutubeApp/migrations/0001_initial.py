# Generated by Django 3.2.7 on 2021-09-16 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoId', models.TextField(default=None, max_length=20)),
                ('content', models.TextField(max_length=50)),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replies', models.TextField(max_length=100)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YoutubeApp.comment')),
            ],
        ),
    ]

# Generated by Django 4.2 on 2024-04-07 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techcrunch', '0002_imagepost_remove_postcategorynewpost_is_scraped_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FailedSearchedPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=127)),
                ('error_text', models.TextField(blank=True)),
                ('searched_new_posts', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='faild_posts', to='techcrunch.searchedpostbykeyword')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 4.2 on 2024-04-09 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techcrunch', '0004_alter_author_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchedkeyword',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
# Generated by Django 4.2 on 2024-04-07 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techcrunch', '0001_initial'),
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
                ('searched_new_posts', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='failed_posts', to='techcrunch.searchedpostbykeyword')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImagePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('image_order', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=127)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostDailySearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='postcategorynewpost',
            name='category_new_posts',
        ),
        migrations.RemoveField(
            model_name='postcategorynewpost',
            name='post',
        ),
        migrations.RemoveField(
            model_name='postimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='postimage',
            name='post',
        ),
        migrations.RemoveField(
            model_name='category',
            name='post_count',
        ),
        migrations.RemoveField(
            model_name='dailysearch',
            name='new_post_count',
        ),
        migrations.RemoveField(
            model_name='dailysearch',
            name='scraped_post_count',
        ),
        migrations.RemoveField(
            model_name='failedcategorynewposts',
            name='category_new_posts',
        ),
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='dailysearch',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dailysearch',
            name='title',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='failedcategorynewposts',
            name='daily_search',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='failed_posts', to='techcrunch.dailysearch'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagefile',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagefile',
            name='is_scraped',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='imagefile',
            name='post_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postcategory',
            name='title',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='json',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='tech_crunch_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imagefile',
            name='local_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='techcrunch.author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='posts_thumbnail', to='techcrunch.imagefile'),
        ),
        migrations.DeleteModel(
            name='CategoryNewPosts',
        ),
        migrations.DeleteModel(
            name='PostCategoryNewPost',
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
        migrations.AddField(
            model_name='postdailysearch',
            name='daily_search',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='techcrunch.dailysearch'),
        ),
        migrations.AddField(
            model_name='postdailysearch',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_new_posts', to='techcrunch.post'),
        ),
        migrations.AddField(
            model_name='imagepost',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='techcrunch.imagefile'),
        ),
        migrations.AddField(
            model_name='imagepost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='images', to='techcrunch.post'),
        ),
    ]
# Generated by Django 5.1.4 on 2025-01-17 11:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogAuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=128, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=128, verbose_name='last_name')),
                ('avatar', models.ImageField(upload_to='blogs/authors/', verbose_name='avatar')),
            ],
            options={
                'verbose_name': 'blog author',
                'verbose_name_plural': 'blog authors',
            },
        ),
        migrations.CreateModel(
            name='BlogTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128, verbose_name='title')),
            ],
            options={
                'verbose_name': 'blog tag',
                'verbose_name_plural': 'blog tags',
            },
        ),
        migrations.AlterModelOptions(
            name='blogmodel',
            options={'verbose_name': 'blog', 'verbose_name_plural': 'blogs'},
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='description',
            field=models.TextField(default=1, verbose_name='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(default='', upload_to='blogs', verbose_name='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='title',
            field=models.CharField(max_length=128, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='authors',
            field=models.ManyToManyField(related_name='blogs', to='blogs.blogauthormodel', verbose_name='authors'),
        ),
        migrations.CreateModel(
            name='BlogCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='blogs.blogcategorymodel', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'blog category',
                'verbose_name_plural': 'blog categories',
            },
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='categories',
            field=models.ManyToManyField(related_name='blogs', to='blogs.blogcategorymodel', verbose_name='categories'),
        ),
        migrations.CreateModel(
            name='BlogCommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.CharField(max_length=128, verbose_name='comment')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.blogmodel', verbose_name='blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'blog comment',
                'verbose_name_plural': 'blog comments',
            },
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='blogs.blogtagmodel', verbose_name='tags'),
        ),
    ]

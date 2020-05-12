# Generated by Django 3.0.6 on 2020-05-10 15:11

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_category', models.CharField(default='杂记', max_length=20, verbose_name='文章类别')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='无标题名', max_length=100, null=True, verbose_name='标题')),
                ('cover', models.ImageField(blank=True, default='/cover_img/default.jpg', null=True, upload_to=post.models.modify_path, verbose_name='封面')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(default='文章内容', verbose_name='文章内容')),
                ('is_publish', models.BooleanField(default=False)),
                ('is_comment', models.BooleanField(default=False)),
                ('total_views', models.PositiveIntegerField(default=0, verbose_name='文章浏览量')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='post.Category')),
            ],
        ),
    ]
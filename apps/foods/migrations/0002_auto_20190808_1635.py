# Generated by Django 2.2.4 on 2019-08-08 16:35

import datetime
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='名称')),
                ('image', stdimage.models.StdImageField(upload_to='path/to', verbose_name='传图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '传图片',
                'verbose_name_plural': '传图片',
            },
        ),
        migrations.RenameField(
            model_name='shopinfo',
            old_name='zan',
            new_name='counts',
        ),
        migrations.AddField(
            model_name='shopinfo',
            name='img',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foods.UploadImage', verbose_name='封面'),
        ),
    ]

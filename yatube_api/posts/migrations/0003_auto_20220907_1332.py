# Generated by Django 2.2.16 on 2022-09-07 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220831_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='posts/images/'),
        ),
    ]

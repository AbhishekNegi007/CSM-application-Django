# Generated by Django 4.1.7 on 2023-05-05 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0004_post_is_public'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='post',
            new_name='post_id',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='user',
            new_name='user_id',
        ),
    ]

# Generated by Django 3.0.4 on 2020-05-03 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='SOME STRING', max_length=250),
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_remove_comment_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

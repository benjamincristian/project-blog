# Generated by Django 4.1.7 on 2023-03-29 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_alter_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
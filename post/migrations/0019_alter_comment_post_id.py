# Generated by Django 4.1.7 on 2023-03-28 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_alter_comment_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.post'),
        ),
    ]

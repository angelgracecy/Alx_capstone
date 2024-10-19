# Generated by Django 5.1.2 on 2024-10-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_created_date_blogpost_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

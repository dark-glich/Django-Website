# Generated by Django 3.2 on 2021-05-16 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_commentsection_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsection',
            name='comment',
            field=models.CharField(max_length=1000),
        ),
    ]

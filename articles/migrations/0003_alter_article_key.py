# Generated by Django 4.2.11 on 2024-05-06 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='key',
            field=models.CharField(default='Qe1nCnyD8A1', max_length=11, unique=True),
        ),
    ]

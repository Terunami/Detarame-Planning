# Generated by Django 2.1.2 on 2020-07-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200706_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='user',
            field=models.TextField(blank=True, null=True, verbose_name='作成者'),
        ),
    ]

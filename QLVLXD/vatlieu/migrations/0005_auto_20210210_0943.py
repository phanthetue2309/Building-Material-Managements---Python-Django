# Generated by Django 3.1.6 on 2021-02-10 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vatlieu', '0004_auto_20210209_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='count',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]

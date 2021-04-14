# Generated by Django 3.1.6 on 2021-02-09 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vatlieu', '0003_auto_20210209_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailinputbill',
            name='input_bill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vatlieu.inputbill'),
        ),
        migrations.AlterField(
            model_name='detailinputbill',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vatlieu.product'),
        ),
    ]

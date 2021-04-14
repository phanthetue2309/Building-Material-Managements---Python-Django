# Generated by Django 3.1.6 on 2021-02-09 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vatlieu', '0002_auto_20210209_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailinputbill',
            name='input_bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_bills', to='vatlieu.inputbill'),
        ),
        migrations.AlterField(
            model_name='detailinputbill',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='vatlieu.product'),
        ),
    ]

# Generated by Django 5.0.1 on 2024-04-14 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_order_email_alter_order_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='zipcode',
            field=models.CharField(max_length=6),
        ),
    ]

# Generated by Django 4.1.3 on 2024-01-12 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangazonapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='admin_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='bangazonapi.adminuser'),
        ),
    ]

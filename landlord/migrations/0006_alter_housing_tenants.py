# Generated by Django 4.2.11 on 2024-06-04 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0004_swipe_remove_match_partner_remove_match_tenant'),
        ('landlord', '0005_rename_square_feet_house_square_meters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housing',
            name='tenants',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.swipe'),
        ),
    ]

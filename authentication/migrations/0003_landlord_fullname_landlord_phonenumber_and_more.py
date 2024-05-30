# Generated by Django 4.2.11 on 2024-05-30 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_landlord_nohouses_alter_tenant_about_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='landlord',
            name='fullName',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='landlord',
            name='phoneNumber',
            field=models.CharField(max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='fullName',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='phoneNumber',
            field=models.CharField(max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='roommate',
            field=models.BooleanField(default=False, null=True),
        ),
    ]

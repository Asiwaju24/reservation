# Generated by Django 5.2 on 2025-04-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_contact_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='contact',
            name='reservation_datetime',
            field=models.DateTimeField(),
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_alter_agenda_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='checkout',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

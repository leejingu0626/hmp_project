# Generated by Django 2.1.5 on 2019-01-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myplot', '0002_columninfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='columninfo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
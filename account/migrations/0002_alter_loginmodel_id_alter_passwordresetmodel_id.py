# Generated by Django 5.1.1 on 2024-09-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='passwordresetmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

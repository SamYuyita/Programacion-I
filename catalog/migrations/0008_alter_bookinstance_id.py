# Generated by Django 4.2.6 on 2023-11-24 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_bookinstance_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

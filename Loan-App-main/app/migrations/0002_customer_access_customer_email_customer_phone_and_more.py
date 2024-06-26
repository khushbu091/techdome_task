# Generated by Django 5.0.4 on 2024-05-03 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='access',
            field=models.CharField(choices=[('General', 'General'), ('Admin', 'Admin')], default='General', max_length=10),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(default=None, max_length=10, verbose_name='Contact No.'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
    ]

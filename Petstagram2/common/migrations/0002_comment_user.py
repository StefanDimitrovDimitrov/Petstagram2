# Generated by Django 3.2.4 on 2021-07-09 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_profile_picture'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile'),
            preserve_default=False,
        ),
    ]

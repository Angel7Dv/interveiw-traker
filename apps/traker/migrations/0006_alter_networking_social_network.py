# Generated by Django 4.0.4 on 2022-05-29 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traker', '0005_remove_networking_interviewer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networking',
            name='social_network',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='networking', to='traker.socialnetworks'),
        ),
    ]
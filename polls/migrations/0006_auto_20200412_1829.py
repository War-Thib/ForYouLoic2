# Generated by Django 3.0.5 on 2020-04-12 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_pharmacie_pharmacie_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacie',
            name='pharmacie_ville',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
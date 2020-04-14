# Generated by Django 3.0.5 on 2020-04-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pharmacie',
            name='id',
        ),
        migrations.AddField(
            model_name='pharmacie',
            name='pharmacie_adress',
            field=models.CharField(default='DEFAULT_VALUE', max_length=30),
        ),
        migrations.AddField(
            model_name='pharmacie',
            name='pharmacie_commune',
            field=models.CharField(choices=[('ixelles', 'Ixelles'), ('eterbeek', 'Eterbeek'), ('uccle', 'Uccle')], default='DEFAULT_VALUE', max_length=15),
        ),
        migrations.AlterField(
            model_name='pharmacie',
            name='pharmacie_name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 3.0.5 on 2020-04-15 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_message_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message_mail',
            name='messag_text',
        ),
        migrations.AddField(
            model_name='message_mail',
            name='message_text',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]

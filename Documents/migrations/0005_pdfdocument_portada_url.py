# Generated by Django 4.1.3 on 2024-04-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Documents', '0004_alter_pdfdocument_archivo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfdocument',
            name='portada_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
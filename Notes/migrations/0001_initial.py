# Generated by Django 4.1.3 on 2024-04-21 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Documents', '0005_pdfdocument_portada_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=255)),
                ('fecha_Creacion', models.DateTimeField(auto_now_add=True)),
                ('highlight_areas', models.JSONField(default=list)),
                ('idDocumento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Documents.pdfdocument')),
            ],
        ),
    ]

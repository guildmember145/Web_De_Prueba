# Generated by Django 3.2.6 on 2021-08-23 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.TextField(verbose_name='Categoria de la pregunta')),
                ('nombre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Quiz.pregunta')),
            ],
        ),
    ]
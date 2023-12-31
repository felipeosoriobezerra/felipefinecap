# Generated by Django 4.2.5 on 2023-09-10 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Stand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("localizacao", models.TextField(max_length=150)),
                ("valor", models.FloatField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="Reserva",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_empresa", models.TextField(max_length=150)),
                ("categoria_empresa", models.TextField(max_length=150)),
                ("cnpj", models.CharField(max_length=11)),
                ("quitado", models.BooleanField(default=False)),
                (
                    "stand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="stands.stand"
                    ),
                ),
            ],
        ),
    ]

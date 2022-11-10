# Generated by Django 4.1.3 on 2022-11-10 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tarefa",
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
                ("descricao", models.CharField(max_length=400)),
                ("criacao", models.DateTimeField(auto_now_add=True)),
                (
                    "categoria",
                    models.CharField(
                        choices=[
                            ("urgente", "Urgente"),
                            ("importante", "Importante"),
                            ("precisa ser feito", "Precisa ser feito"),
                        ],
                        default="importante",
                        max_length=25,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("concluido", "Concluido"),
                            ("pendente", "Pendente"),
                            ("adiado", "Adiado"),
                        ],
                        max_length=25,
                    ),
                ),
            ],
        ),
    ]
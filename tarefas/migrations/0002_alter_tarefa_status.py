# Generated by Django 4.1.3 on 2022-11-10 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tarefas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tarefa",
            name="status",
            field=models.CharField(
                choices=[
                    ("concluido", "Concluido"),
                    ("pendente", "Pendente"),
                    ("adiado", "Adiado"),
                ],
                default="pendente",
                max_length=25,
            ),
        ),
    ]
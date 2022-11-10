from django.db import models

# Create your models here.
class Tarefa(models.Model):
    OPCOES_STAUD = (
        ("concluido", "Concluido"),
        ("pendente", "Pendente"),
        ("adiado", "Adiado"),
    )
    OPCOES_CATEGORIAS = (
        ("urgente", "Urgente"),
        ("importante", "Importante"),
        ("precisa ser feito", "Precisa ser feito"),
    )
    descricao = models.CharField(max_length=400)
    criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(
        max_length=25, choices=OPCOES_CATEGORIAS, default="importante"
    )
    status = models.CharField(
        max_length=25, choices=OPCOES_STAUD, default="pendente"
    )

    def __str__(self):
        return f"{self.descricao} | {self.status}"

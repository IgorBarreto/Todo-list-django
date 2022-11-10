from django.urls import path
from . import views

urlpatterns = [
    path("", views.tarefas_pendentes_list, name="tarefas_pendentes_list"),
    path("<int:id>/concluir/", views.concluir_tarefa, name="concluir_tarefa"),
]

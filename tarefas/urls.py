from django.urls import path

from . import views

urlpatterns = [
    path("", views.tarefas_pendentes_list, name="tarefas_pendentes_list"),
    path("<int:id>/concluir/", views.concluir_tarefa, name="concluir_tarefa"),
    path("<int:id>/excluir/", views.excluir_tarefa, name="excluir_tarefa"),
    path("<int:id>/adiar/", views.adiar_tarefa, name="adiar_tarefa"),
    path("<int:id>/editar/", views.editar_tarefa, name="editar_tarefa"),
    path(
        "concluidas/",
        views.tarefas_concluidas_list,
        name="tarefas_concluidas_list",
    ),
    path(
        "adiadas/",
        views.tarefas_adiadas_list,
        name="tarefas_adiadas_list",
    ),
    path(
        "<int:id>/mover-para-lista-de-tarefas/",
        views.mover_para_tarefas,
        name="mover_para_tarefas",
    ),
]

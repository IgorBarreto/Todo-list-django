from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AdicionarTarefa, EditarTarefaForm
from .models import Tarefa

# Create your views here.


def tarefas_pendentes_list(request: HttpRequest):
    tarefas_pendentes = Tarefa.objects.filter(status="pendente")

    if request.method == "POST":
        form = AdicionarTarefa(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("tarefas_pendentes_list")
    else:
        form = AdicionarTarefa()
    return render(
        request,
        "tarefas_pendentes.html",
        {"tarefas_pendentes": tarefas_pendentes, "form": form},
    )


def concluir_tarefa(request: HttpRequest, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.status = "concluido"
    tarefa.save()

    return redirect("tarefas_pendentes_list")


def excluir_tarefa(request: HttpRequest, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect("tarefas_pendentes_list")


def adiar_tarefa(request: HttpRequest, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.status = "adiado"
    tarefa.save()

    return redirect("tarefas_pendentes_list")


def editar_tarefa(request: HttpRequest, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == "POST":
        form = EditarTarefaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            tarefa.descricao = cd["tarefa"]
            tarefa.categoria = cd["categoria"]
            tarefa.save()
            return redirect("tarefas_pendentes_list")

    else:
        form = EditarTarefaForm(
            initial={"tarefa": tarefa.descricao, "categoria": tarefa.categoria}
        )
        return render(
            request, "editar_tarefa.html", {"tarefa": tarefa, "form": form}
        )


def tarefas_concluidas_list(request: HttpRequest):
    tarefas = Tarefa.objects.filter(
        Q(status="concluido") | Q(status="Concluido")
    )
    return render(
        request, "tarefas_concluidas.html", {"tarefas_concluidas": tarefas}
    )


def tarefas_adiadas_list(request: HttpRequest):
    tarefas = Tarefa.objects.filter(status="adiado")
    print(tarefas)
    return render(
        request, "tarefas_adiadas.html", {"tarefas_adiadas": tarefas}
    )


def mover_para_tarefas(request: HttpRequest, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.status = "pendente"
    tarefa.save()
    return redirect("tarefas_pendentes_list")

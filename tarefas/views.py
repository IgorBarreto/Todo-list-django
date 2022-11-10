from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Tarefa
from .forms import AdicionarTarefa

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
    tarefa.status = "Concluido"
    tarefa.save()

    return redirect("tarefas_pendentes_list")

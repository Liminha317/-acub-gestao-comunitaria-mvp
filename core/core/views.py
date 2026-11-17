from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import FamiliaBeneficiada, ItemEstoque, MovimentacaoEstoque


@login_required
def painel_inicial(request):
    cesta = ItemEstoque.objects.filter(nome_item__icontains="Cesta").first()
    total_familias = FamiliaBeneficiada.objects.filter(status="ativo").count()
    return render(
        request,
        "core/painel.html",
        {"cesta": cesta, "total_familias": total_familias},
    )


@login_required
def consultar_fila(request):
    termo = request.GET.get("q", "").strip()
    competencia_atual = date.today().strftime("%Y-%m")
    familias = FamiliaBeneficiada.objects.filter(status="ativo")
    if termo:
        familias = familias.filter(
            Q(nome_responsavel__icontains=termo) | Q(nif_documento__icontains=termo)
        )
    resultados = []
    for fam in familias[:20]:
        ja_retirou = MovimentacaoEstoque.objects.filter(
            familia=fam,
            tipo_movimentacao="SAIDA",
            competencia_mes=competencia_atual,
        ).exists()
        resultados.append({"familia": fam, "ja_retirou": ja_retirou})
    return render(
        request,
        "core/fila.html",
        {"resultados": resultados, "termo": termo, "competencia": competencia_atual},
    )


@login_required
@transaction.atomic
def confirmar_entrega(request, familia_id):
    if request.method == "POST":
        familia = get_object_or_404(FamiliaBeneficiada, id=familia_id, status="ativo")
        item = get_object_or_404(ItemEstoque, id=request.POST.get("item_id"))
        competencia_atual = date.today().strftime("%Y-%m")

        ja_retirou = MovimentacaoEstoque.objects.filter(
            familia=familia,
            item=item,
            tipo_movimentacao="SAIDA",
            competencia_mes=competencia_atual,
        ).exists()

        if ja_retirou:
            messages.error(request, "Família já recebeu cesta básica neste mês.")
            return redirect("consultar_fila")

        if item.quantidade_atual < 1:
            messages.error(request, "Saldo insuficiente em estoque para realizar entrega.")
            return redirect("consultar_fila")

        MovimentacaoEstoque.objects.create(
            tipo_movimentacao="SAIDA",
            quantidade=1,
            competencia_mes=competencia_atual,
            item=item,
            familia=familia,
        )
        item.quantidade_atual -= 1
        item.save()
        messages.success(
            request, f"Entrega registrada com sucesso para {familia.nome_responsavel}."
        )
    return redirect("estoque_alertas")

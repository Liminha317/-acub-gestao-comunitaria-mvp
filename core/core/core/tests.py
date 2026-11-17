import pytest
from core.models import FamiliaBeneficiada, ItemEstoque, MovimentacaoEstoque


@pytest.mark.django_db
def test_alerta_estoque_baixo():
    item = ItemEstoque.objects.create(
        nome_item="Cesta Básica Fechada",
        categoria="Alimentos",
        quantidade_atual=14,
        estoque_minimo=15,
    )
    assert item.estoque_baixo is True


@pytest.mark.django_db
def test_bloqueio_entrega_duplicada_mesmo_mes():
    familia = FamiliaBeneficiada.objects.create(
        nome_responsavel="Ana Clara Souza",
        nif_documento="123.456.789-00",
        endereco_bairro="Rua das Flores, 45",
        qtd_membros=4,
    )
    item = ItemEstoque.objects.create(
        nome_item="Cesta Básica Fechada",
        categoria="Alimentos",
        quantidade_atual=20,
        estoque_minimo=15,
    )
    MovimentacaoEstoque.objects.create(
        tipo_movimentacao="SAIDA",
        quantidade=1,
        competencia_mes="2026-11",
        item=item,
        familia=familia,
    )
    duplicada = MovimentacaoEstoque.objects.filter(
        familia=familia, item=item, tipo_movimentacao="SAIDA", competencia_mes="2026-11"
    ).exists()
    assert duplicada is True

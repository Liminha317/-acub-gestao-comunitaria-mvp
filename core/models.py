from django.db import models
from django.core.validators import MinValueValidator


class FamiliaBeneficiada(models.Model):
    STATUS_CHOICES = [
        ("ativo", "Ativo"),
        ("inativo", "Inativo"),
    ]

    nome_responsavel = models.CharField("Nome do Responsável", max_length=150)
    nif_documento = models.CharField("NIF / CPF", max_length=20, unique=True)
    telefone = models.CharField("Telefone", max_length=20, blank=True)
    endereco_bairro = models.CharField("Endereço no Bairro", max_length=200)
    qtd_membros = models.PositiveIntegerField(
        "Quantidade de Membros", validators=[MinValueValidator(1)]
    )
    status = models.CharField(
        "Status", max_length=15, choices=STATUS_CHOICES, default="ativo"
    )
    data_cadastro = models.DateTimeField("Data de Cadastro", auto_now_add=True)

    def __str__(self):
        return f"{self.nome_responsavel} ({self.nif_documento})"


class ItemEstoque(models.Model):
    nome_item = models.CharField("Nome do Item", max_length=100)
    categoria = models.CharField("Categoria", max_length=50)
    unidade_medida = models.CharField("Unidade", max_length=20, default="unidade")
    quantidade_atual = models.PositiveIntegerField("Saldo Atual", default=0)
    estoque_minimo = models.PositiveIntegerField("Estoque Mínimo", default=15)
    data_atualizacao = models.DateTimeField("Última Atualização", auto_now=True)

    @property
    def estoque_baixo(self):
        return self.quantidade_atual <= self.estoque_minimo

    def __str__(self):
        return f"{self.nome_item}: {self.quantidade_atual} {self.unidade_medida}"


class MovimentacaoEstoque(models.Model):
    TIPO_CHOICES = [
        ("ENTRADA", "Entrada de Doação"),
        ("SAIDA", "Saída / Entrega"),
    ]

    tipo_movimentacao = models.CharField("Tipo", max_length=10, choices=TIPO_CHOICES)
    quantidade = models.PositiveIntegerField(
        "Quantidade", validators=[MinValueValidator(1)]
    )
    data_movimentacao = models.DateTimeField("Data", auto_now_add=True)
    competencia_mes = models.CharField("Competência (AAAA-MM)", max_length=7)
    item = models.ForeignKey(
        ItemEstoque, on_delete=models.PROTECT, related_name="movimentacoes"
    )
    familia = models.ForeignKey(
        FamiliaBeneficiada,
        on_delete=models.PROTECT,
        related_name="entregas",
        null=True,
        blank=True,
    )

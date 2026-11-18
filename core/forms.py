import re
from django import forms
from django.core.exceptions import ValidationError
from .models import FamiliaBeneficiada, ItemEstoque


class FamiliaBeneficiadaForm(forms.ModelForm):
    class Meta:
        model = FamiliaBeneficiada
        fields = [
            "nome_responsavel",
            "nif_documento",
            "telefone",
            "endereco_bairro",
            "qtd_membros",
        ]

    def clean_nome_responsavel(self):
        nome = self.cleaned_data.get("nome_responsavel", "").strip()
        if len(nome) < 3:
            raise ValidationError("Informe o nome completo do responsável (mínimo 3 caracteres).")
        return nome

    def clean_nif_documento(self):
        nif = re.sub(r"[^0-9A-Za-z.-]", "", self.cleaned_data.get("nif_documento", "").strip())
        if len(nif) < 5:
            raise ValidationError("Informe um NIF ou CPF válido para evitar duplicidade.")
        return nif


class EntradaEstoqueForm(forms.Form):
    item = forms.ModelChoiceField(queryset=ItemEstoque.objects.all(), label="Item de Estoque")
    quantidade = forms.IntegerField(min_value=1, label="Quantidade Recebida")

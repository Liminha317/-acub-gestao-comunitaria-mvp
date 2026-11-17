# -acub-gestao-comunitaria-mvp
MVP Web Responsivo para Gestão de Famílias e Estoque de Doações da Associação Comunitária Unidos pelo Bairro (ACUB) - ODS 2

# ACUB — Sistema de Gestão Comunitária (MVP)

Aplicação web responsiva leve desenvolvida para a **Associação Comunitária "Unidos pelo Bairro" (ACUB)**, com o objetivo de substituir controles manuais em papel e planilhas por um fluxo digital ágil, seguro e acessível para o cadastro único de famílias beneficiadas e gestão de estoque de doações (alinhado ao **ODS 2 — Fome Zero e Agricultura Sustentável**).

## Tecnologias e Arquitetura
* **Padrão Arquitetural:** Arquitetura Monolítica em Camadas (**Model-View-Template — MVT**)
* **Linguagem:** Python 3.12
* **Framework Web:** Django 5.1
* **Interface Responsiva e Acessível:** Bootstrap 5.3
* **Banco de Dados:** PostgreSQL 16 (com suporte local via SQLite para testes rápidos)
* **Testes Automatizados:** Pytest 8.3

## Funcionalidades do MVP
* **RF01 — Cadastro Único de Famílias:** Registro de responsáveis com validação de unicidade por NIF/CPF.
* **RF02 — Consulta Rápida na Fila:** Busca instantânea por nome ou NIF com indicador visual de elegibilidade mensal.
* **RF03 — Entrada de Doações:** Registro de mantimentos recebidos com atualização automática de saldo.
* **RF04 — Saída de Cestas Básicas e Alertas:** Baixa transacional no estoque, bloqueio de entrega duplicada no mesmo mês e alerta visual multimodal de estoque mínimo.

## Estrutura Inicial do Projeto
```text
acub-gestao-comunitaria-mvp/
├── gestao_acub/         # Configurações principais do projeto Django (settings, urls, wsgi)
├── core/                # App principal (models, views, forms, templates e testes)
├── requirements.txt     # Dependências fixadas do projeto
└── README.md            # Documentação técnica e funcional
```

## Como Executar Localmente
1. Clone o repositório: `git clone https://github.com`
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute os testes automatizados: `pytest`

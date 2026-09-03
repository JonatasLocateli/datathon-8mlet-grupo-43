# Datathon - Grupo 43 - FIAP MLET

## Visão do Problema

Uma instituição financeira digital precisa decidir, em diferentes canais, qual
oferta apresentar para cada cliente elegível. Este projeto implementa uma
plataforma de experimentação adaptativa (multi-armed bandit) para essa decisão,
comparando-a contra uma abordagem de regra fixa (baseline).

**Abordagem escolhida:** Thompson Sampling, com os braços do bandit representando
três ofertas fictícias de produto:

- **Depósito Turbo** — produto padrão
- **Depósito Turbo+** — variação com incentivo
- **Consultoria Invest** — abordagem consultiva

**Base de dados:** [Bank Marketing (Kaggle)](https://www.kaggle.com/datasets/henriqueyamahata/bank-marketing)
— campanhas de telemarketing de um banco português, usada como proxy de
propensão à conversão.

> Nota sobre dados: nenhum dado real de cliente é utilizado. A base é pública
> e anonimizada, e as ofertas simuladas são construídas sobre ela apenas para
> fins de demonstração técnica.

## Como executar

### Pré-requisitos
- Python 3.10+

### Instalação
\`\`\`bash
git clone https://github.com/JonatasLocateli/datathon-8mlet-grupo-43.git
cd datathon-8mlet-grupo-43
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
\`\`\`

### Estrutura do projeto
\`\`\`
notebooks/   → EDA e experimentação (Etapas 1-4)
src/api/     → serviço FastAPI (Etapa 5)
src/bandit/  → implementação do Thompson Sampling
data/        → dados locais (não versionados - baixar via link acima)
\`\`\`

## Status do projeto

- [x] Etapa 0 — Organização do projeto
- [ ] Etapa 1 — Base Kaggle e EDA
- [ ] Etapa 2 — Preparação da Base
- [ ] Etapa 3 — Baseline e estratégia algorítmica
- [ ] Etapa 4 — Avaliação e Casos de Teste
- [ ] Etapa 5 — Serviço ou interface demonstrável
- [ ] Etapa 6 — Arquitetura-alvo em Nuvem
- [ ] Etapa 7 — Ciclo de vida MLOps
- [ ] Etapa 8 — Apresentação Final
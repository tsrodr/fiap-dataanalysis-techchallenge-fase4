# Projeto: Dashboard e Forecasting do Preço do Petróleo Brent

## Descrição Geral

Este projeto foi desenvolvido para atender à necessidade de análise e previsão do preço do petróleo Brent, fornecendo ferramentas interativas e insights estratégicos para a tomada de decisão. A solução inclui um **dashboard interativo**, um **modelo preditivo de Machine Learning** e um plano de **deploy em produção**, garantindo eficiência e escalabilidade.

---

## Soluções Desenvolvidas

### 1. **Dashboard Interativo**
Um dashboard foi criado para apresentar uma análise detalhada e interativa dos dados históricos do preço do petróleo Brent. Ele possibilita:

- **Visualização histórica**: Acompanhamento da evolução do preço ao longo do tempo.
- **Insights estratégicos**: Identificação de padrões e impactos de eventos externos, como:
  - **Crises econômicas**.
  - **Eventos geopolíticos**.
  - **Oscilações no câmbio**.
  - **Mudanças na demanda energética global**.
- **Acessibilidade**: Disponível via **Streamlit** para consultas dinâmicas e interações diretas, e um dashboard complementar no **Power BI** para análises mais robustas e integradas.

### 2. **Modelo Preditivo**
Foi implementado um modelo de Machine Learning para previsão diária do preço do petróleo. Detalhes técnicos:

- **Modelo selecionado**: **AutoARIMA**, escolhido pela sua precisão e capacidade de lidar com sazonalidades em séries temporais.
- **Performance**: Avaliado com métricas como RMSE e MAPE, garantindo previsões confiáveis.
- **Processamento de Dados**: Utilização de **Apache Spark** para manipulação de grandes volumes de dados com eficiência e escalabilidade.
- **Escalabilidade**: O modelo pode ser ajustado automaticamente para incorporar novos dados.

### 3. **Plano de Deploy**
Um plano foi elaborado para garantir a operação contínua do modelo e do dashboard:

- **Dados dinâmicos**: O script de web scraping atualiza os dados semanalmente a partir da fonte oficial do [IPEA](https://www.ipea.gov.br/).
- **Infraestrutura**:
  - Banco de dados **PostgreSQL** hospedado na **AWS**, garantindo alta disponibilidade e segurança dos dados.
  - Hospedagem do dashboard em ambiente web utilizando **Streamlit** e exportação de arquivos para o Power BI.
  - Processamento em **Apache Spark** para manipulação e preparação de dados em larga escala.
- **Automação**: Processos automatizados para extração, limpeza e carregamento de dados.

---

## Atualização dos Dados

A atualização dos dados e do modelo preditivo é simples e pode ser feita executando o script principal do projeto. Basta rodar o arquivo `main.py`, que realizará os seguintes passos:

1. **Web Scraping**:
   - Coleta os dados mais recentes do preço do petróleo Brent a partir da fonte oficial.

2. **Limpeza e Preparação**:
   - Processa os dados coletados, preparando-os para análise e modelagem.

3. **Treinamento do Modelo**:
   - Atualiza o modelo preditivo com os dados mais recentes.

4. **Carga no Banco de Dados**:
   - Insere os novos dados no banco de dados PostgreSQL hospedado na AWS.

5. **Conexão com o Banco pelo Power BI**:
   - O Power BI se conecta diretamente ao banco de dados **PostgreSQL** hospedado na **AWS RDS** para buscar os dados mais recentes.
   - Isso elimina a necessidade de exportação manual de arquivos.


Para executar a atualização, utilize o seguinte comando no terminal:
```bash
python main.py
```
---

## Benefícios do Projeto

1. **Insights Estratégicos**:
   - Identificação de tendências de preços com base em eventos históricos e contextos econômicos.
   - Capacidade de prever flutuações futuras e planejar estratégias com base em previsões confiáveis.

2. **Tomada de Decisão Baseada em Dados**:
   - Ferramentas que auxiliam no planejamento de ações empresariais e na avaliação de riscos relacionados ao mercado de petróleo.

3. **Escalabilidade e Atualização Contínua**:
   - Um sistema automatizado para atualização de dados e previsões, garantindo relevância e precisão contínuas.

---

## Tecnologias Utilizadas

- **Linguagem e Bibliotecas**:
  - Python: Pandas, Statsforecast (AutoARIMA), Matplotlib, Plotly, Streamlit.
- **Processamento de Dados**:
  - Apache Spark: Manipulação de grandes volumes de dados.
- **Banco de Dados**:
  - PostgreSQL: Armazenamento e integração de dados, hospedado na AWS.
- **Ferramentas de Visualização**:
  - Streamlit: Dashboard interativo e MVP do modelo.
  - Power BI: Dashboard complementar com análises avançadas.
- **Infraestrutura**:
  - AWS: Hospedagem do banco de dados e suporte à escalabilidade da solução.
  - GitHub: Versionamento e compartilhamento do código.

---

## Acesso às Ferramentas

1. **Dashboard Interativo**:
   - Disponível em [Streamlit](#insira-o-link-aqui).
2. **Dashboard Complementar**:
   - Disponível em [Power BI](#insira-o-link-aqui).

---

## Considerações Finais

Este projeto oferece uma solução completa e integrada para análise e previsão de preços do petróleo Brent, contribuindo diretamente para decisões estratégicas baseadas em dados. Caso tenha dúvidas ou deseje mais informações, entre em contato conosco.

---


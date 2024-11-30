import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Análise",
    layout="wide",
    initial_sidebar_state="expanded",
)
plotly_conf = {'template': 'ggplot2', 'color_sequence': ['#3d183d']}


def main():
    df_ipea = pd.read_csv('./output/sor/ipeadata.csv')
    df_ipea = df_ipea.rename(columns={'valdata': 'data', 'valvalor': 'preco'})
    df_ipea = df_ipea[df_ipea['data'] >= '2005-01-01']
    df_ipea['data'] = pd.to_datetime(df_ipea['data'])
    df_forecast = pd.read_csv('./output/sor/forecast.csv')
    st.sidebar.title("Menu de Navegação")

    pages = [
        "Início",
        "Sobre o Negócio",
        "Evolução dos Preços",
        "Projeção de Preços",
        "Análise com Power BI"
    ]

    page = st.sidebar.radio("Navegue pelo Projeto", pages)

    if page == "Início":
        show_home()
    elif page == "Sobre o Negócio":
        show_negocio()
    elif page == "Evolução dos Preços":
        show_historico(df_ipea)
    elif page == "Projeção de Preços":
        show_previsao(df_forecast)
    elif page == "Análise com Power BI":
        show_powerbi()


def show_home():
    st.title("O Projeto")
    st.markdown(
        '''
        Este projeto tem como objetivo entregar um **dashboard interativo** que gere insights relevantes sobre o mercado de petróleo Brent, auxiliando na tomada de decisões estratégicas. Além disso, incluiu a criação de um **modelo de Machine Learning** para previsão dos preços, utilizando séries temporais.

        - Criado um **dashboard interativo** integrado a um **storytelling** com **4 insights relevantes**.
        - Um **modelo preditivo** foi desenvolvido e sua performance avaliada com base em métricas confiáveis.
        - Um **MVP funcional** foi implementado utilizando **Streamlit**, acompanhado de um plano para o **deploy** do modelo em produção.

        ## Benefícios para o Negócio

        - **Decisões Baseadas em Dados**:
        - O dashboard interativo fornece uma visão clara e abrangente das tendências do mercado de petróleo Brent, permitindo a identificação de padrões e correlações que suportam decisões estratégicas.

        - **Previsão Confiável de Preços**:
        - O modelo preditivo oferece estimativas diárias precisas dos preços do petróleo, permitindo o planejamento proativo e a mitigação de riscos relacionados à volatilidade do mercado.

        - **Insights Estratégicos**:
        - O storytelling integrado destacou eventos geopolíticos, crises econômicas e oscilações na demanda global de energia, facilitando a compreensão do impacto desses fatores no mercado.

        - **Escalabilidade e Automação**:
        - Com o plano de deploy proposto, o modelo pode ser integrado a sistemas de produção, garantindo atualizações contínuas e escalabilidade para lidar com volumes maiores de dados no futuro.

        Esta aplicação representa um **MVP (Minimum Viable Product)**.

        ''',
        unsafe_allow_html=True
    )


def show_negocio():
    st.title("Sobre o Mercado de Petróleo Brent")
    st.markdown(
        '''
        **Petróleo Brent**, uma das principais referências globais para o mercado de petróleo. O Brent é extraído de campos localizados no Mar do Norte e comercializado na Bolsa de Londres, servindo como um indicador importante para os mercados da Europa, Ásia e Oriente Médio. Sua cotação reflete as dinâmicas de oferta e demanda no mercado internacional, sendo expressa em dólares por barril.

        ## Por que o Petróleo Brent é Relevante?

        O petróleo Brent destaca-se por ser amplamente utilizado como benchmark no mercado global, devido a fatores como:

        - **Logística eficiente**: Extraído em campos marítimos, o Brent é mais acessível e econômico de transportar, especialmente em comparação com outros tipos de petróleo.
        - **Representatividade global**: Sua cotação reflete as condições de mercado em regiões economicamente importantes, como Europa e Ásia.
        - **Qualidade elevada**: Classificado como leve e doce, o Brent exige menor processamento, tornando-o mais valorizado.

        ## Dinâmica de Preços

        O preço do petróleo Brent é influenciado por diversos fatores que afetam sua oferta e demanda. Alguns dos principais incluem:

        - **Oscilações no dólar**: Alterações na moeda impactam diretamente a cotação do petróleo, que é negociado globalmente em dólares.
        - **Políticas da OPEC**: Decisões da Organização dos Países Exportadores de Petróleo, como cortes ou aumentos na produção, têm efeitos significativos no mercado.
        - **Conflitos geopolíticos**: Eventos como sanções, conflitos armados ou mudanças em acordos internacionais podem alterar drasticamente o preço do petróleo.
        - **Produção e estoques**: Níveis de estoque elevados ou restrições inesperadas na produção criam volatilidade no mercado.

        ## Negociação: Mercado à Vista e Futuros

        O petróleo Brent é negociado de duas formas principais:

        1. **Mercado à Vista**: Transações baseadas no preço atual, com liquidação quase imediata.
        2. **Mercado Futuro**: Contratos baseados em expectativas futuras do preço, permitindo a gestão de riscos e a especulação por parte de investidores.

        ## Benefícios da Previsibilidade com IA

        Focar no petróleo Brent permite abordar uma referência crítica para a economia global, e nosso projeto contribui com insights e previsões para ajudar na tomada de decisão estratégica. Por meio de modelos avançados de **Inteligência Artificial**, geramos previsões de curto prazo baseadas em séries temporais e dados históricos, trazendo maior previsibilidade para um mercado historicamente volátil.

        Com essas ferramentas, empresas e investidores podem antecipar flutuações, gerenciar riscos e aproveitar oportunidades de forma mais eficaz, maximizando seus resultados em um ambiente competitivo e dinâmico.

        ''',
        unsafe_allow_html=True
    )


def show_historico(df_ipea):

    fig = px.line(
        data_frame=df_ipea,
        x=df_ipea.data,
        y=df_ipea.preco,
        template=plotly_conf['template'],
        color_discrete_sequence=plotly_conf['color_sequence'],
        labels={
            'preco': 'Preço (US$)',
            'data': 'Data'
        }
    )
    fig.update_layout(
        title='Preço do Petróleo Brent (US$)',
        xaxis_title='Período',
        yaxis_title='Preço (US$)'
    )

    st.plotly_chart(fig, use_container_width=True)
    st.markdown(
        '''

                O gráfico acima apresenta a série histórica do preço do barril de petróleo Brent desde o ano de 2005. É possível identificar quatro grandes oscilações negativas na série, que tiveram início em 2007, 2010, 2020 e 2022, refletindo os impactos de eventos econômicos e geopolíticos significativos ao longo do período.

                # Fatores que Influenciaram os Valores do Petróleo Brent

                O preço do petróleo Brent é altamente sensível a eventos geopolíticos e econômicos. Grandes crises e acontecimentos globais alteram significativamente a dinâmica de oferta e demanda no mercado, refletindo diretamente nos valores dessa commodity. Abaixo, destacamos quatro eventos históricos que influenciaram os preços do petróleo Brent:

                ---

                ## Crise Financeira Global (2007-2008)

                A Crise Financeira Global foi um dos eventos econômicos mais impactantes do século XXI, iniciada pelo colapso do mercado imobiliário nos Estados Unidos. Este evento teve implicações globais, afetando a demanda por petróleo de várias formas:

                - **Queda na demanda global**: A desaceleração econômica em escala mundial reduziu o consumo de energia, diminuindo a demanda por petróleo.
                - **Desvalorização do petróleo**: O preço do Brent caiu drasticamente, de cerca de **143 USD por barril em julho de 2008** para menos de **33 USD por barril em dezembro do mesmo ano**.
                - **Incertezas no mercado**: A instabilidade econômica levou a flutuações de preço, com investidores retraídos e incertezas sobre a recuperação econômica.

                ---

                ## Primavera Árabe (2010-2012)

                A Primavera Árabe foi uma onda de protestos e revoluções que afetou vários países do Oriente Médio e Norte da África, regiões responsáveis por grande parte da produção mundial de petróleo. Este evento teve impacto direto na oferta do Brent:

                - **Instabilidade política**: Países produtores como Líbia, Egito e Síria sofreram com conflitos e mudanças de governo, reduzindo sua capacidade de produção.
                - **Interrupção da oferta**: A diminuição na produção gerou escassez no mercado global, aumentando os preços.
                - **Altas históricas**: Durante o auge das tensões, os preços do Brent atingiram **128 USD por barril em 2012**, refletindo a preocupação com a continuidade do fornecimento.

                ---

                ## Pandemia de COVID-19 (2020-2023)

                A pandemia de COVID-19 trouxe desafios inéditos para o mercado de petróleo, com impactos severos tanto na oferta quanto na demanda:

                - **Queda abrupta na demanda**: Com restrições de mobilidade, lockdowns e redução nas viagens, o consumo de petróleo despencou.
                - **Colapso histórico dos preços**: Em abril de 2020, os preços do petróleo Brent chegaram a **menos de 9 USD por barril**, um dos níveis mais baixos da história.
                - **Recuperação gradual**: À medida que as economias reabriam, a demanda retornava, mas ainda enfrentava dificuldades devido à volatilidade do mercado e incertezas com novas variantes do vírus.

                ---

                ## Conflito Rússia-Ucrânia (2022-presente)

                O conflito entre Rússia e Ucrânia, iniciado em fevereiro de 2022, teve um impacto significativo nos mercados de energia, especialmente na Europa:

                - **Redução na oferta russa**: A Rússia é um dos maiores exportadores de petróleo e gás natural. Sanções econômicas e restrições reduziram sua capacidade de exportar para mercados globais.
                - **Aumento nos preços globais**: A incerteza gerada pela guerra levou os preços do Brent a ultrapassarem **120 USD por barril em 2022**, refletindo temores de escassez de energia.
                - **Mudanças nos fluxos de energia**: Países europeus buscaram alternativas ao petróleo russo, aumentando a demanda por outras fontes, incluindo o Brent, e contribuindo para a elevação dos preços.

                ---

                ## Conclusão

                Os preços do petróleo Brent são altamente influenciados por fatores externos, como crises econômicas, conflitos geopolíticos e eventos globais inesperados. Esses eventos ressaltam a volatilidade do mercado de energia e a importância de ferramentas analíticas para prever flutuações e auxiliar na tomada de decisões estratégicas. Este projeto utiliza essas análises como base para prever tendências futuras, permitindo maior previsibilidade em um mercado tão dinâmico.

        ''',
        unsafe_allow_html=True
    )


def show_previsao(df_forecast):
    fig_previsao = px.line(
        data_frame=df_forecast,
        x=df_forecast.data,
        y=df_forecast.preco_previsto_brent,
        template=plotly_conf['template'],
        color_discrete_sequence=plotly_conf['color_sequence'],
        labels={
            'preco_previsto_brent':'Preço previsto (US$)',
            'data':'Data'
        }
    )
    fig_previsao.update_layout(
        title='Preço Previsto do Petróleo Brent (US$)',
        xaxis_title='Período',
        yaxis_title='Preço Previsto (US$)'
    )
    st.plotly_chart(fig_previsao, use_container_width=True)
    st.markdown(
        """
        O gráfico acima apresenta o forecast para as próximas 10 cotações do barril de petróleo Brent,
        gerado com o modelo AutoARIMA implementado. 

        A projeção foi limitada a 10 dias devido a fatores críticos relacionados à confiabilidade e precisão das previsões em séries temporais financeiras:

        - **Alta volatilidade do mercado**: Eventos geopolíticos e econômicos podem gerar mudanças súbitas e imprevisíveis no mercado de petróleo, reduzindo a precisão de previsões de longo prazo.
        - **Redução da acurácia em horizontes maiores**: Embora o modelo tenha uma acurácia superior a 90% em curtos períodos, a incerteza aumenta significativamente à medida que o horizonte de previsão se expande.
        - **Foco na tomada de decisão prática**: Previsões de curto prazo são mais úteis para decisões estratégicas imediatas, como gestão de estoque, contratos futuros e ajustes de orçamento.
        - **Evitar overfitting e especulações irreais**: Projeções mais longas podem gerar resultados menos confiáveis, levando a interpretações errôneas.

        O uso de um horizonte de previsão de 10 dias garante um equilíbrio ideal entre confiabilidade e aplicabilidade prática, permitindo que os tomadores de decisão utilizem as informações de forma eficaz em um mercado dinâmico.
        """
    )


def show_powerbi():
    st.title("Dashboard Integrado do Power BI")

    # URL do relatório do Power BI (substitua pela URL do seu relatório embed)
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiYjcxNGZlNmYtMDI4OS00NmJiLTk3Y2EtMWMyZWEyZWJmMTA4IiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9"

    # Embeber o relatório usando um iframe
    st.components.v1.html(
        f"""
        <iframe width="100%" height="900" src="{power_bi_url}" frameborder="0" allowFullScreen="true"></iframe>
        """,
        height=900,
    )


# Executar a aplicação
if __name__ == "__main__":
    main()

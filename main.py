import streamlit as st
import pandas as pd

def main():
    st.title("Dashboard de Vulnerabilidades (CVE)")

    # Solicitar upload do arquivo CSV
    uploaded_file = st.file_uploader("Faça upload do arquivo CSV", type=["csv"])

    if uploaded_file is not None:
        # Carregar o arquivo CSV
        df = pd.read_csv(uploaded_file)

        # Verificar se o arquivo CSV foi carregado corretamente
        if df is not None:
            # Agrupar pelos valores do campo "CVE"
            agrupado_por_cve = df.groupby('cve').size().reset_index(name='contagem')

            # Exibir o dashboard agrupado por "CVE"
            st.write("## Dashboard Agrupado por CVE")
            st.write("Número de ocorrências de vulnerabilidade para cada CVE: ")
            st.write(agrupado_por_cve)
        else:
            st.error("Erro ao carregar o arquivo CSV")

if __name__ == "__main__":
    main()




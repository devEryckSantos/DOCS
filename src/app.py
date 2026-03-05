import streamlit as st

def configure_interface():
    st.title("Upload de Arquivo DIO - Desafio 1 - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        fileName = uploaded_file.name

        blobUrl = ""
        if blobUrl:
            st.success(f"Arquivo '{fileName}' enviado com sucesso para o Azure Blob Storage!")
            credit_card_info = "" # chamar funcao de deteccao de informacoes de cartao de credito
            show_image_and_validation(blobUrl, credit_card_info)
        else:
            st.error(f"Erro ao enviar o arquivo '{fileName}' para o Azure Blob Storage.")

def show_image_and_validation(blobUrl, credit_card_info):
    st.image(blobUrl, caption='Imagem enviada', use_column_width=True)
    st.write("Resultado da validação:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {credit_card_info['card_name']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de Validade: {credit_card_info['expiration_date']}")
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write("Este não é um cartão de crédito válido.")

if __name__ == "__main__":
    configure_interface()
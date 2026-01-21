import streamlit as st

st.set_page_config(page_title="Cadastro de Produtos", page_icon="📝", layout="centered")

# Ocultar sidebar
hide_pages_style = """
<style>
section[data-testid="stSidebar"] { display: none; }
</style>
"""
st.markdown(hide_pages_style, unsafe_allow_html=True)

# Lista de produtos cadastrados
if "produtos" not in st.session_state:
    st.session_state["produtos"] = []

# Função para limpar os campos (executada antes da renderização)
def limpar_campos():
    st.session_state.update({
        "codigo": "",
        "marca": "",
        "tipo": "",
        "categoria": "",
        "preco_unitario": "",
        "custo": "",
        "obs": "",
    })

    #Serve para o botão de enviar
def salvar_produto():
        if st.session_state["codigo"] and st.session_state["marca"] and st.session_state["tipo"] and st.session_state["categoria"] and st.session_state["preco_unitario"] and st.session_state["custo"]:
        
            novo_produto = {
            "Código": st.session_state["codigo"],
            "Marca": st.session_state["marca"],
            "Tipo": st.session_state["tipo"],
            "Categoria": st.session_state["categoria"],
            "Preço Unitário": st.session_state["preco_unitario"],
            "Custo": st.session_state["custo"],
            "Obs": st.session_state["obs"]
        }
            st.session_state["produtos"].append(novo_produto)
            limpar_campos()
            st.session_state["mensagem"] = "ok"

        else:
            st.session_state["mensagem"] = "erro"
            

# Estilo
st.markdown("""
<style>
    .title {
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        margin-bottom: -10px;
    }
    .sub {
        text-align: center;
        margin-bottom: 30px;
        color: #555;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">Cadastro de Produtos</p>', unsafe_allow_html=True)
st.markdown('<p class="sub">Preencha os dados do produto abaixo</p>', unsafe_allow_html=True)

# Inputs com keys
codigo = st.text_input("Código", key="codigo")
marca = st.text_input("Marca", key="marca")
tipo = st.text_input("Tipo", key="tipo")
categoria = st.text_input("Categoria", key="categoria")
preco_unitario = st.text_input("Preço Unitário", key="preco_unitario")
custo = st.text_input("Custo", key="custo")
obs = st.text_area("Observações (opcional)", key="obs")

col1,col2,col3 = st.columns(3)

# Botão enviar
with col1:
    st.button("Enviar", on_click=salvar_produto)
    if st.session_state.get("mensagem") == "ok":
        st.success("Produto cadastrado com sucesso!")
    elif st.session_state.get("mensagem") == "erro":
        st.error("Complete todos os campos")

     
        # Botão cadastrar outro — usa callback correto! -Descarte
        #with col2: -Descarte
             #st.button("Cadastrar outro", on_click=limpar_campos) -Descarte

# Botão limpar tudo — mesma lógica
with col3:
    def limpar_tudo():
        st.session_state["produtos"] = []
        limpar_campos()

    st.button("Limpar tudo", on_click=limpar_tudo)

st.write("---")
st.subheader("📦 Produtos cadastrados nesta sessão(não tem um banco de dados):")

if len(st.session_state["produtos"]) > 0:
    st.table(st.session_state["produtos"])
else:
    st.info("Nenhum produto cadastrado ainda.")

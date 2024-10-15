import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
st.set_page_config(layout="wide")
st.title("Titulo")
st.write("Texto")





def main():

    ####Desabilitar tela de login
    #st.session_state['logged_in'] = True
    ####
    
    # Verificar se o usuário está logado
    if not is_user_logged_in():
        show_login_page()
    else:
        run_main_program()

def is_user_logged_in():
    # Verificar se o usuário está logado
    return st.session_state.get('logged_in', False)

def show_login_page():
    st.title("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    login_button = st.button("Login")

    if login_button:
        if username == "admin" and password == "admin":
            st.session_state['logged_in'] = True
            st.experimental_rerun()  # Re-executar o aplicativo para atualizar a tela
        else:
            st.error("Invalid username or password")

def run_main_program():

    st.title("Logado")
    
    texto= st.checkbox('Apresentar Texto')
    if texto:
        st.write("Texto")

    with st.sidebar:
        st.write("Texto")



    a = 1
    button = st.button("botão")

    if button:
        a=2
    st.write(a)

    num1= st.text_input("número")
    st.write(num1)

    def pag1():
        st.title("Página 1")
    def pag2():
        st.title("Página 2")
    def pag3():
        st.title("Página 3")

    with st.sidebar:
                selecao = option_menu(
                    "Menu",
                    ["Página 1", "Página 2", "Página 3"],
                    icons=['1-circle', '2-circle', '3-circle'],
                    menu_icon="cast",
                    default_index=0,
                )
    if selecao == 'Página 1':
        pag1()
    elif selecao == 'Página 2':
        pag2()
    elif selecao == 'Página 3':
        pag3()


    file_path = r"C:\Users\12115138660\Downloads\dados.xlsx"

    df = pd.read_excel(file_path)

    with st.sidebar:
        linhas = st.slider("Quantidade de linhas", 1, 20)
    df = df.head(linhas)
    st.write(df)


    col1, col2 = st.columns(2)
    with col1:
        st.write(df)
            
    with col2:
        st.write(df.head(linhas))

if __name__ == "__main__":
    main()
    



import streamlit as st
import pandas as pd

st.title("Relatório de Aula")

@st.cache
def load_data():
    return pd.read_csv('data/emotions.csv')


def is_authenticated(password):
    return password == "182916f6-756d-40d6-95fc-3283ba5efdf8"


def generate_login_block():
    block1 = st.empty()
    block2 = st.empty()

    return block1, block2


def clean_blocks(blocks):
    for block in blocks:
        block.empty()


def login(blocks):
    return blocks[1].text_input('ID da Aula')

def main():

    st.balloons()

login_blocks = generate_login_block()
password = login(login_blocks)

st.sidebar.text("Menu Lateral")
st.sidebar.button("Relatório por Aluno")
st.sidebar.button("Top 10 emoções")
st.sidebar.button("Melhores momentos da aula")

if is_authenticated(password):
    clean_blocks(login_blocks)
    main()
elif password:
    st.info("Aula não encontrada. Por favor, insira um ID válido.")

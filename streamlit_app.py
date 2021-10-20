import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time 

st.title("Relatório de Aula")
df = pd.read_csv('data/emocoes.csv')
agg = pd.read_csv('data/agg.csv')

Engajado = df[df['emocao'] == 'Engajado']
Engajado_agg = Engajado.groupby(['emocao', 'pessoa']).size().reset_index(name='size')
Engajado_agg = Engajado_agg.sort_values(by=['size'], ascending=False)

emotions_count = df.value_counts('emocao').reset_index()


def is_authenticated(password):
    return password == "182916f6-756d-40d6-95fc-3283ba5efdf8"


def generate_time_agg_graph():
    fig = px.line(agg, x="tempo", y="size", labels= { 'tempo': 'tempo (s)',
                                                      'size': 'número de alunos' }, color='emocao', title='Emoções ao longo do tempo')
    st.plotly_chart(fig, use_container_width=True)

    
def generate_top_students():
    st.markdown('<br/>', unsafe_allow_html=True)
    st.markdown("<center style='font-size:2em'=>Alunos Mais Engajados</center>", unsafe_allow_html=True)
    top_three = Engajado_agg.head(3).to_numpy()
    for row in top_three:
        st.markdown(f"<center><span style='color:#00FF00;font-size:1.5em'>{row[1]}</span></center>", unsafe_allow_html=True)
    st.markdown('<br/>', unsafe_allow_html=True)


def generate_bottom_students():
    st.markdown("<center style='font-size:2em'>Alunos Menos Engajados</center>", unsafe_allow_html=True)
    bottom_three = np.flip(Engajado_agg.tail(3).to_numpy(), 0)
    for row in bottom_three:
        st.write(f"<center><span style='color:red;font-size:1.5em'>{row[1]}</span></center>", unsafe_allow_html=True)
    st.markdown('<br/> <br/>', unsafe_allow_html=True)


def generate_emotions_pizza():
    fig = px.pie(emotions_count, values=emotions_count.index, names='emocao', title='Predominância de Emoções')
    st.plotly_chart(fig, use_container_width=True)
    
def generate_login_block():
    block1 = st.empty()
    block2 = st.empty()

    return block1, block2


def clean_blocks(blocks):
    for block in blocks:
        block.empty()


def graph_columns():
    generate_time_agg_graph()
    generate_top_students()
    generate_bottom_students()
    generate_emotions_pizza()


def login(blocks):
    return blocks[1].text_input('ID da Aula')

login_blocks = generate_login_block()
password = login(login_blocks)
drive_block = st.empty()
google_drive = drive_block.text_input('Link da aula para processamento', '')
id_block = st.empty()

if google_drive != '':
    drive_block.empty()
    with st.spinner('Aguarde enquanto processamos sua aula.'):
        time.sleep(5)
        st.success('Pronto! ID da Aula processada: 182916f6-756d-40d6-95fc-3283ba5efdf8')
    google_drive = ''

if is_authenticated(password):
    id_block.empty()
    drive_block.empty()
    clean_blocks(login_blocks)
    st.balloons()
    graph_columns()
elif password:
    st.info("Aula não encontrada. Por favor, insira um ID válido.")

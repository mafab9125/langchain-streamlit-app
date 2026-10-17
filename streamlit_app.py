import streamlit as st
from langchain_openai import ChatOpenAI

# Título de la página
st.title('🦜🔗 Quickstart App')

# Caja en la barra lateral para que el usuario pegue su API key
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Función que le manda el texto al modelo y muestra la respuesta
def generate_response(input_text):
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        api_key=openai_api_key
    )
    respuesta = llm.invoke(input_text)
    st.info(respuesta.content)

# Formulario con área de texto y botón
with st.form('my_form'):
    text = st.text_area(
        'Enter text:',
        'What are the three key pieces of advice for learning how to code?'
    )
    submitted = st.form_submit_button('Submit')

    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')

    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)


# Explicación línea por línea:

# import streamlit as st → trae Streamlit para construir la web.
# from langchain_openai import ChatOpenAI → trae la clase de LangChain que se conecta con los modelos de OpenAI. (El tutorial usaba from langchain.llms import OpenAI, que ya no existe.)
# st.title(...) → pone el título grande arriba.
# st.sidebar.text_input(..., type='password') → crea una caja en la barra lateral; type='password' oculta lo que escribes con puntitos (mejora de seguridad sobre el tutorial).
# ChatOpenAI(model=..., temperature=0.7, api_key=...) → crea el “cerebro”. temperature controla qué tan creativa es la respuesta (0 = precisa, 1 = creativa). Si gpt-4o-mini no aparece en tu cuenta, cámbialo por cualquier modelo que veas disponible en tu panel de OpenAI.
# llm.invoke(input_text) → envía la pregunta y espera la respuesta. (El tutorial usaba llm(input_text), forma antigua.)
# respuesta.content → el texto de la respuesta.
# st.info(...) → muestra la respuesta en un recuadro azul.
# st.form(...) → agrupa el área de texto y el botón, para que la app solo se ejecute al presionar Submit.
# if not openai_api_key.startswith('sk-') → si la key no empieza por sk-, muestra una advertencia amarilla.
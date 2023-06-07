from model_handler import return_ai_response, initialize_model
from lookups import LLM_MODEL_TYPE
# from streamlit_html import html_code

# from streamlit_handler import kill_st
import streamlit as st


st.markdown(
    """
    <h1 style="color: white;">Chat LAU</h1>
    """,
    unsafe_allow_html=True
)
# st.title('<div class="title">ChatLAU</div>', unsafe_allow_html=True)

# st.markdown(html_code, unsafe_allow_html=True)
# st.text_input("Enter your text", value=component_value, key='text_input')

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://reemsbucket.s3.us-west-2.amazonaws.com/background.jpeg");
             background-attachment: fixed;
             background-size: cover
             color: white;  /* Set text color to white */
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

st.markdown(
    """
    <style>
    .text-input-label {
        color: white; /* Set text color to white */
        margin-bottom: 0; /* Remove bottom margin */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write('<p class="text-input-label">Tell me something...</p>', unsafe_allow_html=True)
question = st.text_input('', value='', key=None, type='default', help=None)

llm_model = initialize_model(LLM_MODEL_TYPE.DAVINCI)
response = return_ai_response(llm_model, question)


st.markdown(
    """
    <style>
    .text-container {
        background-color: rgba(255, 255, 255, 0.9); /* Opaque white background */
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        color: rgba(50, 50, 50, 1.0);
    }
    </style>
    """,
    unsafe_allow_html=True
)

if question:
    st.write(f'<div class="text-container"><span style="color: black;">You:</span> {question}</div>', unsafe_allow_html=True)
    st.write(f'<div class="text-container"><span style="color: black;">ChatLAU:</span> {response}</div>', unsafe_allow_html=True)

 

    # if question=='exit':
    #     kill_st()

# conversation = ConversationChain(
#     llm=llm, 
#     verbose=True, 
#     memory=ConversationBufferMemory()
# )
# conversation.predict(question)
from model_handler import return_ai_response, initialize_model
from lookups import LLM_MODEL_TYPE
# from streamlit_html import html_code

# from streamlit_handler import kill_st
import streamlit as st

st.markdown(
    """
    <style>
    .title {
        color: white; /* Set text color to white */
        font-size: 75px; /* Set font size */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<h1 class="title">ChatLAU</h1>', unsafe_allow_html=True)
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
        font-size: 18px; /* Set font size to 18 pixels */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write('<p class="text-input-label">Tell me something...</p>', unsafe_allow_html=True)
question = st.text_input('', value='', key=None, type='default', help=None)

llm_model = initialize_model(LLM_MODEL_TYPE.DAVINCI)
response = return_ai_response(llm_model, question)


css = '''
    <style>
        .text-container {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 10px;
            margin-bottom: 10px;
        }
        .text-container span {
            color: black;
        }
    </style>
'''

st.markdown(css, unsafe_allow_html=True)

if question:
    st.markdown(f'<div class="text-container"><span>You:</span> {question}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="text-container"><span>ChatLAU:</span> {response}</div>', unsafe_allow_html=True) 
    

 

    # if question=='exit':
    #     kill_st()

# conversation = ConversationChain(
#     llm=llm, 
#     verbose=True, 
#     memory=ConversationBufferMemory()
# )
# conversation.predict(question)
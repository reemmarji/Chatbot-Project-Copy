import os
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# print(OPENAI_API_KEY)

memory_list = list()    


def initialize_model(model_type):
    llm = OpenAI(model_name=model_type.value, openai_api_key=OPENAI_API_KEY)
    return llm

def return_ai_response(llm,input_question):
    template = "Answer the question as an expert on LAU only. Question: {question}."
    prompt = PromptTemplate(template=template, input_variables=["question"])
    output = prompt.format(question=input_question)
    llm = OpenAI(model_name="text-davinci-003", openai_api_key=OPENAI_API_KEY)
    llm_chain = LLMChain(llm=llm, prompt=prompt) 
    response = llm_chain.run(question = output)
    return response

def add_to_memory(item):
    memory_list.append(item)
    
def return_memory():
    return memory_list


# def intialize_prompt(template):
#     prompt = PromptTemplate(template=template, input_variables=['question'])
#     return prompt

# def intialize_chain(llm, prompt):
#     chain = LLMChain(llm=llm, prompt=prompt)   
#     return chain 
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv

load_dotenv()

def get_model():
    return ChatOpenAI(model="gpt-4o-mini")

def invoking_model(input, prompt=None, temperature=0):
  try:
    model = ChatOpenAI(model= "gpt-4o-mini",temperature=temperature)
    
    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=input)
    ]

    response = model.invoke(messages)

    return response.content
  except Exception as e:
    return f"Desculpe, ocorreu um erro ao processar sua solicitação. Por favor, tente novamente mais tarde. Erro: {e}"

def invoking_model_with_structured_output(input, structured_output, prompt=None):
  try:
    model = ChatOpenAI(model= "gpt-4o-mini").with_structured_output(structured_output)

    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=input)
    ]

    response = model.invoke(messages)
    return response
  
  except Exception as e:
    
    return f"Desculpe, ocorreu um erro ao processar sua solicitação. Por favor, tente novamente mais tarde. Erro: {e}"

def invoke_model_with_few_shot_prompt_and_structured_output(input, few_shot_prompt, system_prompt=None, structured_output=None):
  try:
    model = ChatOpenAI(model= "gpt-4o-mini").with_structured_output(structured_output)
    chat_prompt = ChatPromptTemplate.from_messages([
      ("system", system_prompt),
      (few_shot_prompt),
      ("user", "{input}")
    ])
    
    chain = chat_prompt | model
    response = chain.invoke({"input": input})

    return response.next_route
  
  except Exception as e:
    
    return f"Desculpe, ocorreu um erro ao processar sua solicitação. Por favor, tente novamente mais tarde. Erro: {e}"

def invoking_model_with_messages_placeholder(messages, prompt, temperature=0):
  try:
    model = ChatOpenAI(model= "gpt-4o-mini",temperature=temperature)
    chat_prompt = ChatPromptTemplate.from_messages([
      ("system", prompt),
      ('placeholder', "{messages}")
    ])
    
    chain = chat_prompt | model
    response = chain.invoke({"messages": messages}  )
    
    return response.content
  
  except Exception as e:
    
    return f"Desculpe, ocorreu um erro ao processar sua solicitação. Por favor, tente novamente mais tarde. Erro: {e}"
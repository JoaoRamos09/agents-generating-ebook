from graph.models.state.State import State
from graph.utils.openai_utils import invoking_model

def get_subject(state: State):
    
    prompt = """"
    Você é um especialista na venda de produtos digitais, mais precisamente na venda de ebooks.
    
    Sua função é avaliar o tema proposto pelo usuário e retornar somente o tema. Você tem a liberdade de escolher o tema mais adequado para o usuário se entender que ele terá sucesso na venda do produto.
    
    """
    
    subject = invoking_model(input=state["input_user"], prompt=prompt)
    
    state["subject"] = subject
    
    return state

from graph.models.state.State import State
from graph.utils.openai_utils import invoking_model_with_structured_output
from graph.models.responses.StructuringEbook import StructuringEbookResponse

def structuring_ebook(state: State):
    
    system_prompt = """
    Você é um especialista na estruturação dos capítulos de ebooks.
    
    Cada capítulo deve ter um título, um resumo e o número do capítulo.
    
    Sua função é estruturar o ebook de acordo com o tema, as palavras chaves e o número de páginas definidas pelo usuário.
    
    """
    human_prompt = f"""
    O tema do ebook é: {state['subject']}
    
    O máximo de capitulos que o ebook pode ter é: {state['max_chapters']}
    """

    structuring_ebook = invoking_model_with_structured_output(input=human_prompt, structured_output=StructuringEbookResponse, prompt=system_prompt)
    
    state["resume_chapters"] = structuring_ebook.chapters
    
    return state
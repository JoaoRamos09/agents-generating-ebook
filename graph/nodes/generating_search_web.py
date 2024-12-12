from graph.models.state.State import State
from graph.utils.openai_utils import invoking_model_with_structured_output
from graph.models.responses.StructuringWebSearchChapter import StructuringWebSearchChapterResponse
def generating_search_web(state: State):
    
    system_prompt = """
    Você é um especialista sobre buscas na internet e palavras chaves.
    
    Sua principal função será formatar uma busca na internet de acordo com cada capítulo do ebook, avalie o titulo, o resumo e as palavras chaves de cada capítulo e defina qual é a melhor frase para realizar a busca na internet sobre o assunto.
    
    Retorne a busca na internet e o número do capítulo.
    
    """
    
    human_prompt = f"""
    O tema principal do ebook é: {state["subject"]}
    
    Os capítulos do ebook são: {get_chapters_string(state['resume_chapters'])}
    """
    
    search = invoking_model_with_structured_output(input=human_prompt, structured_output=StructuringWebSearchChapterResponse, prompt=system_prompt)
    
    state["search_chapters"] = search.web_search_chapters
    
    return state

def get_chapters_string(chapters):
    return "\n".join([f"Título: {chapter.title}\nResumo: {chapter.resume}\nPalavras chaves: {chapter.tags}\nNúmero do capítulo: {chapter.number_chapter}" for chapter in chapters])
    
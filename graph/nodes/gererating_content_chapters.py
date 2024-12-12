from graph.utils.openai_utils import invoking_model

def generate_content_chapters(state):
    
    for number_chapter in range(state["max_chapters"]):
        content = get_content(state["resume_chapters"][number_chapter],state["search_chapters"][number_chapter])
        state["resume_chapters"][number_chapter].content = content
        
    return state

def get_content(resume_chapter, web_content):
    
    return invoking_model(input=get_user_prompt(resume_chapter, web_content), prompt=get_system_prompt())
     
def get_system_prompt():
    return "Você é um especialista em gerar conteúdos para capitulos especificos de livros. Você receberá as informações do capitulo e você deverá gerar o conteúdo TODO O CONTEÚDO DO CAPITULO. Retorne somente o conteúdo do capítulo, não retorne o título."

def get_user_prompt(resume_chapter, web_content):
    return f"""
O título do capítulo é: {resume_chapter.title} 
O resume do capítulo é: {resume_chapter.resume}
As principais palavras chaves do capítulo são: {resume_chapter.tags}
O conteúdo encontrado na web para esse capítulo é: {web_content.content}
"""

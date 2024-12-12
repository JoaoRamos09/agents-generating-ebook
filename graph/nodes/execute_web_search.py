from langchain_community.tools.tavily_search import TavilySearchResults
from graph.models.responses.SearchChapter import SearchChapterResponse
from time import sleep

def processes_web_search(state):
    chapters: list[SearchChapterResponse] = []
    
    for web_search_chapter in state["search_chapters"]:
        web_content = execute_web_search(web_search_chapter.web_search)
        web_search_chapter.content = web_content
        chapters.append(web_search_chapter)
        
    state["search_chapters"] = chapters
    return state

def execute_web_search(web_search):
    
    content = ""
    
    search = TavilySearchResults(min_results=4)
    results = search.invoke(input = web_search)
    
    return get_content_from_results(results)
    
def get_content_from_results(results):
    content = ""
    for result in results:
        content += f"\n O conteúdo encontrado foi: {result['content']}"
    return content

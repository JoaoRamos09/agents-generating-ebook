
from langgraph.graph import END,StateGraph
from graph.models.state.State import State
from graph.nodes.get_subject import get_subject
from graph.nodes.generating_search_web import generating_search_web
from graph.nodes.structuring_ebook import structuring_ebook
from graph.nodes.execute_web_search import processes_web_search   
from graph.nodes.gererating_content_chapters import generate_content_chapters

def graph():
    
    graph = StateGraph(State)
    
    graph.add_node("get_subject", get_subject)
    graph.add_node("structuring_ebook", structuring_ebook)
    graph.add_node("generating_search_web", generating_search_web)
    graph.add_node("processes_web_search", processes_web_search)
    graph.add_node("generate_content_chapters", generate_content_chapters)
    
    graph.set_entry_point("get_subject")
    
    graph.add_edge("get_subject", "structuring_ebook")
    graph.add_edge("structuring_ebook", "generating_search_web")
    graph.add_edge("generating_search_web", "processes_web_search")
    graph.add_edge("processes_web_search", "generate_content_chapters")
    graph.add_edge("generate_content_chapters", END)
    
    return graph.compile()


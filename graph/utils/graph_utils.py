from graph.graph import graph


def invoke_graph(input_user: str, max_chapters: int):
    
    graph_model = graph()

    response = graph_model.invoke({"input_user": input_user, "max_chapters": max_chapters})
    
    return response



from graph.utils.graph_utils import invoke_graph


result = invoke_graph(input_user="Como montar um cronograma de estudo efetivo para passar em concursos públicos", max_chapters=6)

print(result["resume_chapters"])




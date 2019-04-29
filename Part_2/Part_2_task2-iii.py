from Part_2 import graph_module as gr


def main():
    test = gr.Graph()
    test.text_input('../test_data/test_graph.txt')
    print(test.adjacency_list)
    print(test.edges)
    print(test.vertices)
    print(*test.min_path('1', '2'))

    print()
    test1 = gr.UndirectedGraph()
    test1.adj_list_input({'1': ['0', '2'], '2': ['0', '1'], '0': ['1', '2'], '4': []})
    test1.text_input('../test_data/test_graph.txt')
    print(test1.adjacency_list)
    print(test1.edges)
    print(test1.vertices)
    print(test1.check_completeness())
    print(test1.vertex_degree('0'))
    test1.print_graph()
    print(test1.get_comp_num())
    print(test1.check_bipartite())
    print(test1.check_connectivity())


main()

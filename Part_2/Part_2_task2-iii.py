import graph_module as gr


def main():
    test = gr.UndirectedGraph(1, [4, 5])
    test.print_graph()

    print(test.get_edges())
    print(test.check_completeness())
    test.remove_edge(1, 2)
    test.remove_edge(2, 0)
    test.print_graph()

    print("min path:", *test.min_distance(1, 2))
    print(test.comp_number())
    print(test.check_connectivity())
    print(test.check_completeness())
    test.print_graph()

    print(test.vertex_degree(0))
    print(test.get_edges())

main()

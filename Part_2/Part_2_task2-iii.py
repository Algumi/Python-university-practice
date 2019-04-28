from Part_2 import graph_module as gr


def main():
    test = gr.Graph()
    test.text_input('../test_data/test_graph.txt')
    print(test.adjacency_list)
    print(test.edges)
    print(test.vertices)


main()

from Part_2 import graph_module as gr


def main():
    test = gr.Graph()
    test.text_input('../test_data/test_graph.txt')
    print(test.adjacency_list)
    print(test.edges)
    print(test.vertices)
    print(test.min_path('1', '2'))

    print("Неориентированный граф:")
    test1 = gr.UndirectedGraph()
    test1.text_input('../test_data/test_graph.txt')
    print(test1.adjacency_list)
    print(test1.edges)
    print(test1.vertices)

    print("Функция нахождения минимального пути:")
    print(test1.min_path('1', '2'))

    print("Вывод графа:")
    test1.print_graph()

    print("Проверка на связность:")
    print(test1.check_connectivity())

    print("Проверка на полноту:")
    print(test1.check_completeness())

    print("Проверка функции нахождения дополнения:")
    test_addition = test1.addition_graph()
    test_addition.print_graph()

    print("Проверка на двудольность:")
    print(test1.check_bipartite())

    print("Нахождение степени вершины:")
    print(test1.vertex_degree('0'))

    print("Нахождение количества компонент связности:")
    print(test1.get_comp_num())

    test2 = gr.DirectedGraph()
    test2.adj_list_input({'1': ['0'], '2': ['1'], '0': ['2'], '4': ['3'], '3': []})
    print("Ориентированный граф:")
    print("Функция нахождения минимального пути:")
    print(test2.min_path('0', '3'))

    print("Вывод графа:")
    test2.print_graph()

    print("Проверка на слабую связность:")
    print(test2.check_weak_connection())

    print("Проверка на сильную связность:")
    print(test2.check_strong_connection())

    test3 = gr.WeightedGraph()
    test3.weighted_text_input('../test_data/test_graph_weighted.txt')
    print(test3.weights)
    print(test3.adjacency_list)
    test3.print_weighted_graph()
    print(test3.min_path('0', '3'))
    print(*test3.min_path_weighted('0', '3'))
    test3.min_spanning_tree().print_weighted_graph()


main()

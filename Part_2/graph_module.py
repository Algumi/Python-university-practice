class Graph:
    adjacency_list = {}
    edges = set()
    vertices = set()
    oriented_graph = False

    def __init__(self, arg_list=dict()):
        self.adjacency_list = arg_list

    def adj_list_input(self, a_list):
        self.adjacency_list = a_list

    def text_input(self, file):
        input_data = open(file, 'r')
        for line in input_data:
            inp = line.split()
            self.adjacency_list.update({inp[0] : inp[1:]})
        self.generate_info()

    def generate_info(self):
        self.vertices = set(self.adjacency_list.keys())
        self.get_edges()

    def get_edges(self):
        for v, lst in self.adjacency_list.items():
            self.edges.update([(v, x) for x in lst])


class DirectedGraph(Graph):
    def __init__(self, arg_list):
        Graph.__init__(self, arg_list)
        self.oriented_graph = True


class UndirectedGraph(Graph):
    def __init__(self, arg_list):
        Graph.__init__(self, arg_list)
        self.oriented_graph = False


class WeightedGraph(UndirectedGraph):
    def __init__(self, arg_list):
        UndirectedGraph.__init__(self, arg_list)

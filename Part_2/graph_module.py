import copy

class Graph:
    graph_list = {}
    vertex_num = 0
    oriented_graph = False

    def __init__(self, constructor_type, arg_list):
        self.graph_list = {}

        # creates fully connected graph (constructor_type = 1)
        # arguments - [orientation, number of vertices, default value in vertex]
        if constructor_type == 1:
            self.vertex_num = arg_list[0]
            vertex_type = arg_list[1]
            for i in range(self.vertex_num):
                self.graph_list.update({i: [[(i, 0) for i in range(self.vertex_num)],
                                            vertex_type + i, 0]})
                self.graph_list[i][0].remove((i, 0))

        # creates a graph, reading info from the file (constructor_type = 2)
        # arguments - [file name]
        elif constructor_type == 3:
            input_data = open(arg_list[0], 'r')

            # reads orientation and weight mode
            self.oriented_graph = bool(int(input_data.readline()[13:-1]))
            weight = bool(int(input_data.readline()[7:-1]))

            # reads the vertices
            vertex_list = input_data.readline()
            vertex_list = vertex_list[:-1].split("__")
            for vert in vertex_list:
                self.add_vertex(vert)

            # reads the edges
            for line in input_data:
                edge = line.split()
                if not weight:
                    edge.append(0)
                self.add_edge(int(edge[0]), int(edge[1]), int(edge[2]))

        # creates transposed graph
        elif constructor_type == 5:
            graph_info = arg_list[0].get_info()
            self.__graph_list = copy.deepcopy(graph_info[0])
            self.__oriented_graph = copy.deepcopy(graph_info[2])
            # cleans the adj list
            for vert in self.__graph_list.values():
                vert[0] = []
            # creates inverted edges
            for vert in graph_info[0].items():
                for item in vert[1][0]:
                    self.__graph_list[item[0]][0].append((vert[0], 0))

    def get_info(self):
        return [self.graph_list, self.vertex_num, self.oriented_graph]

    def print_list(self):
        print()
        print(len(self.graph_list))
        for item in self.graph_list:
            print("Vertex ", item, self.graph_list[item])

    def add_vertex(self, value):
        if not self.find_vertex_id(value):
            # 0 - white, 1 - gray, 2 - black
            color = 0
            self.graph_list.update({self.vertex_num: [[], value, color]})
            self.vertex_num += 1
        else:
            print("Vertex with this value already exist")
            return False

    def add_edge(self, vertex1, vertex2, weight=0):
        self.graph_list[vertex1][0].append((vertex2, weight))
        if not self.oriented_graph:
            self.graph_list[vertex2][0].append((vertex1, weight))

    def remove_edge(self, vertex1, vertex2):
        was_find = False
        for item in self.graph_list[vertex1][0]:
            if item[0] == vertex2:
                self.graph_list[vertex1][0].remove(item)
                was_find = True
        if not self.oriented_graph:
            for item in self.graph_list[vertex2][0]:
                if item[0] == vertex1:
                    self.graph_list[vertex2][0].remove(item)
                    was_find = True
        if not was_find:
            return False

    def remove_vertex_id(self, vertex_num):
        if vertex_num in self.graph_list:
            del self.graph_list[vertex_num]
            for vert in self.graph_list:
                for item in self.graph_list[vert][0]:
                    if item[0] == vertex_num:
                        self.graph_list[vert][0].remove(item)
        else:
            print("Remove failed. There is no such vertex")
            return False
        return True

    def find_vertex_id(self, value):
        for vertex in self.graph_list.items():
            if vertex[1][1] == value:
                return vertex[0]
        return False

    def remove_vertex_value(self, value, first_try=True):
        vert_del_id = self.find_vertex_id(value)

        if not vert_del_id and first_try:
            print("Remove failed. There is no such vertex")
            return False
        elif vert_del_id:
            self.remove_vertex_id(vert_del_id)
            self.remove_vertex_value(value, False)
            return True

    # Returns minimal path between vertices s and t
    def min_distance(self, s, t):
        queue = [s]
        path = []
        parent = dict()
        vertex = s

        while queue and vertex != t:
            vertex = queue.pop(0)
            if vertex not in path:
                near = [x[0] for x in self.graph_list[vertex][0]]
                if t in near:
                    parent[t] = vertex
                    path.append(t)
                    queue = []
                else:
                    path.append(vertex)
                    new = (set(near) - set(path) - set(parent.keys()))
                    for v in new:
                        parent[v] = vertex
                    queue.extend(new)

        if path[-1] == t:
            ans = []
            while t != s:
                ans.append(t)
                t = parent[t]
            ans.append(s)
            return reversed(ans)
        else:
            return []

    def get_adjacency_matrix(self):
        matr = []
        for vert in self.graph_list.items():
            tmp_matr = [float("inf") for i in range(len(self.graph_list))]
            tmp_matr[vert[0]] = 0
            for edge in vert[1][0]:
                tmp_matr[edge[0]] = edge[1]
            matr.append(tmp_matr)
        return matr

    # makes the color of all vertices = white
    def reset_color(self):
        for vert in self.graph_list.items():
            vert[1][2] = 0

    # finds all the components(returns them in format {vert : comp} and makes graph_list[vert_num][3] = comp_num
    def find_comp(self):
        self.reset_color()
        self.add_comp_field()
        for vert in self.graph_list.items():
            if vert[1][2] == 0:
                self.dfs_for_comp(vert[0], vert[0])
        comp = {}
        for vert in self.graph_list.items():
            comp.update({vert[0]: vert[1][3]})
        return comp

    # needed for finding components in graph
    def dfs_for_comp(self, vert, start):
        self.graph_list[vert][2] = 1
        for item in self.graph_list[vert][0]:
            if self.graph_list[item[0]][2] == 0:
                self.dfs_for_comp(item[0], start)
        self.graph_list[vert][2] = 2
        self.graph_list[vert][3] = start

    # returns all edges in graph (without repeats)
    def get_edges(self):
        edges = {}
        for vert in self.graph_list.items():
            for connect in vert[1][0]:
                edges.update({(min(vert[0], connect[0]), max(vert[0], connect[0])) : connect[1]})
        return edges

    # adds field that will be used for info about component
    def add_comp_field(self):
        for vert in self.graph_list.items():
            vert[1].append(vert[0])

    def get_adjency_list(self):
        ans = {}
        for vert in self.graph_list.items():
            ans_list = []
            for item in vert[1][0]:
                ans_list.append(self.graph_list[item[0]][1])
            ans.update({vert[1][1]: ans_list})
        return ans

    def dfs_traversal(self):
        # makes the color of all vertices = white
        self.reset_color()
        for vert in self.graph_list.items():
            if vert[1][2] == 0:
                self.dfs(vert[0])

    def dfs(self, vert):
        self.graph_list[vert][2] = 1
        for item in self.graph_list[vert][0]:
            if self.graph_list[item[0]][2] == 0:
                self.dfs(item[0])
        self.graph_list[vert][2] = 2

    # checks that all vertices have same color
    def check_color(self, color):
        for vert in self.graph_list.values():
            if vert[2] != color: return False
        return True

    def print_graph(self):
        print("\nGraph Values:")
        lst = self.get_adjency_list()
        for v in lst.items():
            print("vertex value %d :" % v[0], *v[1])
        print("Graph id:")
        for v in lst.items():
            v_id = self.find_vertex_id(v[0])
            print("vertex id %d :" % v_id, *[x[0] for x in self.graph_list[v_id][0]])


class DirectedGraph(Graph):
    def __init__(self, constructor_type, arg_list):
        Graph.__init__(self, constructor_type, arg_list)
        self.oriented_graph = True

    def check_strong_connection(self):
        self.reset_color()
        self.dfs(self.vertex_num - 1)
        for vert in self.graph_list.values():
            if vert[2] == 0: return False
        self.reset_color()
        trans_graph = Graph(5, [self])
        trans_graph.dfs(self.vertex_num - 1)
        return trans_graph.check_color(2)


class UndirectedGraph(Graph):
    def __init__(self, constructor_type, arg_list):
        Graph.__init__(self, constructor_type, arg_list)
        self.oriented_graph = False

    def check_connectivity(self):
        return self.comp_number() == 1

    def comp_number(self):
        return len(set(self.find_comp().values()))

    def check_completeness(self):
        for v in self.graph_list.values():
            if len(v[0]) != self.vertex_num - 1:
                return False
        return True

    def vertex_degree(self, v_id):
        return len(self.graph_list[v_id][0])

    def addition_graph(self):
        ans = UndirectedGraph(0)


class WeightedGraph(UndirectedGraph):
    def min_spanning_tree(self):
        # creates a new graph - copy
        new_graph = Graph(0, [])
        components = {}
        min_edge = {}
        vertex_num = 0
        old_edges = self.get_edges()
        added_edges = []
        # preparations for creating tree
        # new_graph = { vert_num : [[list], value, color, comp] }
        for vert in self.graph_list.items():
            vertex_num += 1
            new_graph.add_vertex(vert[1][1])
            components.update({vert[0]: vert[0]})
            # min edges - {comp_id : [edge, wight]}
            min_edge.update({vert[0]: [(0, 0), 0]})
        new_graph.add_comp_field()

        # main cycle of work
        while len(added_edges) < vertex_num - 1:
            for k in components.keys():
                min_edge[k][1] = float("inf")
            components = new_graph.find_comp()
            # finds edges with min weight for every component
            for edge in old_edges.keys():
                if components[edge[0]] != components[edge[1]]:
                    if (min_edge[components[edge[0]]][1]) > old_edges[edge]:
                        min_edge[components[edge[0]]][0] = edge
                        min_edge[components[edge[0]]][1] = old_edges[edge]
                    if (min_edge[components[edge[1]]][1]) > old_edges[edge]:
                        min_edge[components[edge[1]]][0] = edge
                        min_edge[components[edge[1]]][1] = old_edges[edge]
            # adds min edges in graph
            for k in components.keys():
                new_elem = (min_edge[k][0][0], min_edge[k][0][1])
                if added_edges.count(new_elem) == 0:
                    new_graph.add_edge(new_elem[0], new_elem[1], old_edges[new_elem])
                    added_edges.append(new_elem)
        return new_graph

    def dijkstra(self, s):
        d = self.get_adjacency_matrix()
        n = len(d[0])
        valid = [True] * n
        weight = [float('inf')] * n
        weight[s] = 0
        for k in range(n):
            min_weight = float('inf')
            id_min_weight = -1
            for i in range(n):
                if valid[i] and weight[i] < min_weight:
                    min_weight = weight[i]
                    id_min_weight = i
            for i in range(n):
                if weight[id_min_weight] + d[id_min_weight][i] < weight[i]:
                    weight[i] = weight[id_min_weight] + d[id_min_weight][i]
            valid[id_min_weight] = False
        return weight

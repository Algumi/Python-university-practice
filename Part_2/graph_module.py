from copy import deepcopy


class Graph:
    adjacency_list = {}
    edges = set()
    vertices = set()
    oriented_graph = False

    def __init__(self, arg_list=None):
        if arg_list:
            self.adjacency_list = deepcopy(arg_list)
            self.generate_info()

    def adj_list_input(self, a_list):
        self.adjacency_list = deepcopy(a_list)
        self.generate_info()

    # file: lines of adjacency_list (first element of line - vertex value, other - connected vertices)
    # Format: <vertex> <connected vertex 1> <connected vertex 2> ... (and so for all vertices)
    def text_input(self, file):
        input_data = open(file, 'r')
        self.adjacency_list = dict()
        for line in input_data:
            inp = line.split()
            self.adjacency_list.update({inp[0]: inp[1:]})
        self.generate_info()

    def generate_info(self):
        self.vertices = set(self.adjacency_list.keys())
        self.get_edges()

    def get_edges(self):
        self.edges = set()
        for v, lst in self.adjacency_list.items():
            self.edges.update([(v, x) for x in lst])

    def min_path(self, s, t):
        queue, visited, path, ans = [s], set(), dict(), []
        while queue:
            v = list.pop(queue)
            visited.add(v)
            if v != t:
                new = set(self.adjacency_list[v]) - visited - path.keys()
                path.update([(x, v) for x in new])
                queue.extend(new)
            else:
                queue = []
        if t in path.keys():
            while t != s:
                ans.append(t)
                t = path[t]
            return list(reversed(ans + [s]))
        return []

    def print_graph(self):
        for v, lst in self.adjacency_list.items():
            print(v, ':', *lst)


class DirectedGraph(Graph):
    def __init__(self, arg_list=None):
        Graph.__init__(self, arg_list)

    def check_weak_connection(self):
        isolated = self.vertices - set([x[0] for x in self.edges]) - set([x[1] for x in self.edges])
        return len(isolated) == 0

    def check_strong_connection(self):
        transposed_adj = dict([(x, []) for x in self.vertices])
        for v, lst in self.adjacency_list.items():
            for item in lst:
                if v not in self.adjacency_list[item]:
                    transposed_adj[item].append(v)
        transposed_graph = DirectedGraph(transposed_adj)
        return self.check_traversal() and transposed_graph.check_traversal()

    def check_traversal(self):
        visited = set()
        
        def dfs(s):
            visited.add(s)
            for v in self.adjacency_list[s]:
                if v not in visited:
                    dfs(v)
        dfs(self.vertices.copy().pop())
        return visited == self.vertices

    def get_income_degree(self, v):
        return len([x for x in self.edges if x[1] == v])

    def get_outcome_degree(self, v):
        return len([x for x in self.edges if x[0] == v])


class UndirectedGraph(Graph):
    bipartite_col = dict()
    vert_colors = dict()
    is_bipartite = -1

    def __init__(self, arg_list=None):
        Graph.__init__(self, arg_list)
        self.generate_info()

    def generate_info(self):
        Graph.generate_info(self)
        self.vert_colors = dict([(x, 0) for x in self.vertices])
        self.bipartite_col = dict([(x, 0) for x in self.vertices])
        self.is_bipartite = -1
        self.calculate_comp_num()

    def check_completeness(self):
        n = len(self.vertices)
        return n * (n - 1) / 2 == len(self.edges) / 2

    def vertex_degree(self, v):
        return len(self.adjacency_list[v])

    def calculate_comp_num(self):
        for v in self.vertices:
            if self.vert_colors[v] == 0:
                self.dfs_special(v, len(set(self.vert_colors.values())), -1)
        if self.is_bipartite == -1:
            self.is_bipartite = True

    def get_comp_num(self):
        return len(set(self.vert_colors.values()))

    def dfs_special(self, s, col, bip_col):
        self.vert_colors[s] = col
        if self.bipartite_col[s] == 0:
            self.bipartite_col[s] = bip_col
        for v in self.adjacency_list[s]:
            if self.bipartite_col[v] == bip_col:
                self.is_bipartite = False
            if self.vert_colors[v] == 0:
                self.dfs_special(v, col, bip_col * -1)

    def check_bipartite(self):
        return self.is_bipartite

    def check_connectivity(self):
        return self.get_comp_num() == 1

    def addition_graph(self):
        def neg(lst): return list(self.vertices - set(lst))
        return UndirectedGraph(dict([(x, neg(lst)) for x, lst in self.adjacency_list.items()]))


class WeightedGraph(UndirectedGraph):
    weights = dict()
    min_paths = dict()

    def __init__(self, arg_list=None):
        UndirectedGraph.__init__(self, arg_list)

    def add_weights(self, w=None):
        if w:
            self.weights = deepcopy(w)
        else:
            for e in self.edges:
                self.weights[e] = 0

    def weighted_text_input(self, file):
        input_data = open(file, 'r')
        self.adjacency_list, self.weights = dict(), dict()
        for line in input_data:
            if line[-1] == '\n':
                line = line[:-1]
            inp = line.split(" ")
            vert_l = [x[1:] for x in inp[1::2]]
            w = [x[:-1] for x in inp[2::2]]
            for i, v in enumerate(vert_l):
                self.weights[(inp[0], v)] = int(w[i])
            self.adjacency_list[inp[0]] = vert_l
        self.generate_info()

    def text_input(self, file):
        UndirectedGraph.text_input(self, file)
        self.add_weights()

    def print_weighted_graph(self):
        for v, lst in self.adjacency_list.items():
            local_w = [str(self.weights[(v, x)]) for x in lst]
            print(v, ":", *["(" + x + " " + local_w[i] + ")" for i, x in enumerate(lst)])

    def min_path_weighted(self, s, t):
        e = [[x[0], x[1], val] for x, val in self.weights.items()]
        n, m = len(self.vertices), len(e)
        d, p = dict([(x, float('inf')) for x in self.vertices]), dict()
        d[s] = 0
        for i in range(n):
            for j in range(m):
                if d[e[j][1]] > d[e[j][0]] + e[j][2]:
                    d[e[j][1]] = int(d[e[j][0]]) + e[j][2]
                    p[e[j][1]] = e[j][0]
                if d[e[j][0]] > d[e[j][1]] + e[j][2]:
                    d[e[j][0]] = int(d[e[j][1]]) + e[j][2]
                    p[e[j][0]] = e[j][1]
        path, v = [], t
        if v in p.keys():
            while v != s:
                path.append(v)
                v = p[v]
            return d[t], list(reversed(path + [s]))
        return float("inf"), []

    def min_spanning_tree(self):
        g = [[val, x[0], x[1]] for x, val in self.weights.items()]
        n, m = len(self.vertices), len(self.edges)
        g.sort()
        tree = dict([(str(x), i) for i, x in enumerate(self.vertices)])
        ans = dict((x, []) for x in self.vertices)
        for i in range(m):
            a, b = g[i][1], g[i][2]
            if tree[a] != tree[b]:
                ans[a].append(b)
                ans[b].append(a)
                old_tree, new_tree = tree[b], tree[a]
                for j in range(n):
                    if tree[str(j)] == old_tree:
                        tree[str(j)] = new_tree
        result = WeightedGraph(ans)
        result.add_weights(self.weights)
        return result

# towns
# route -> travel time
from faker import Faker

# Set the seed value of the shared `random.Random` object
# across all internal generators that will ever be created
Faker.seed(0)

CONFIG = {

}


# fastest routh to reach two points

# graph theorem -> weighted

class Node(object):
    def __init__(self, name, min_connections=3):
        self.name = name
        self.connections = {
            name: Path(0, name, name)  # connection with himself # key is destination
        }
        self.min_connections = min_connections
        pass

    def is_completed(self):
        return len(self.connections.keys()) == self.min_connections

    def is_connected(self, target_node):
        return target_node.name not in self.connections

    def add_connection(self, path):
        if self.is_completed():
            return -1  # is already completed
        elif self.is_connected(path.dst_node):
            return -2  # already exist
        else:
            self.connections[path.dst_node.name] = path
            return 0  # success

    def __str__(self):
        return self.name

    pass


class Path(object):
    def __init__(self, weight, src_node=None, dst_node=None):
        self.weight = weight
        self.src_node = src_node
        self.dst_node = dst_node
        pass

    def set_path(self, src_node, dst_node):
        self.src_node = src_node
        self.dst_node = dst_node
        pass

    def __str__(self):
        return (self.src_node.name, self.dst_node.dst_name, self.weight)

    pass


class Dijkstra(object):

    def __init__(self, dataset, start_node, finish_node):
        self.start_node = start_node
        self.finish_node = start_node
        pass

    def generate_dataset(self):
        pass

    def update_estimates(self):
        pass

    def choose_next_vertex(self):
        pass


if __name__ == "__main__":
    # generate nodes
    # generate weight
    # generate connections
    fake = Faker()
    population = 40
    bridges = 100
    src_node = 1 % population
    dst_node = 90 % population
    connections = 2

    numbers = [fake.random_int() for i in range(bridges)]  # generate connection paths
    countries = [fake.country() for _ in range(population)]  # generate nodes

    # generate graph of two islands
    # graph = {
    #     countries[src_node]: [None],
    #     countries[dst_node]: [None]
    # }

    nodes = [Node(name=_) for _ in countries]
    print('generated: ', len(nodes), ' nodes')
    for n in nodes: print(n)
    used_path = []
    complete_n = {}
    # make connections each node should at least have two connections each
    while len(nodes) != 0 or len(numbers) != 0:
        n = nodes.pop()  # make each node completed until no more nodes remain
        while len(numbers) != 0:
            weigth = numbers.pop()
            loop_n = 0
            while loop_n < len(nodes):
                d = nodes[loop_n]
                if n.is_connected(d):  # if already connected try next n
                    loop_n += 1
                    continue
                # if not already connected make connection
                p = Path(weigth, src_node=n, dst_node=d)
                used_path.append(p)
                r = n.add_connection(path=p)
                if r == 0:
                    loop_n += 1  # successfully added > add another
                    continue
                elif r == -1:  # already completed # lazy check
                    complete_n[n.name] = n
                    break
                    pass
                elif r == -2:  # already exist or key collision
                    loop_n += 1
                    continue

        pass
    # print(graph)
    # nodes = {Node()}
    # for n in nodes: print(n)
    #
    # paths = set(Path(numbers.pop(), nodes))
    #
    # algo = Dijkstra(src_node, dst_node)
    #
    # while algo.choose_next_vertex():
    #     pass
    pass

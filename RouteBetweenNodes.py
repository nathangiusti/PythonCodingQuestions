""" Given a map as a list of node connections, find whether or not any two nodes are connected """


def does_route_exist(link_map, node1, node2, visited=[]):
    link_list = []
    visited.append(node1)
    for x, y in link_map:
        if x == node1 and y not in link_list:
            link_list.append(y)
        elif y == node1 and x not in link_list:
            link_list.append(x)
    for node in link_list:
        if node == node2:
            return True
        if node not in visited:
            if does_route_exist(link_map, node, node2, visited):
                return True
    return False


def main():
    map = [(1, 2), (3, 4), (5, 6), (1, 6), (3, 5), (7, 8), (8, 9)]
    assert does_route_exist(link_map=map, node1=2, node2=5) is True
    assert does_route_exist(link_map=map, node1=1, node2=8) is False
    print("Test passed")

main()





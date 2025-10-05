import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="#A0C4FF"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Binary Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show(block=False)
    plt.pause(1.5)  
    plt.close()


def build_tree_from_array(arr):
    if not arr:
        return None
    
    def build(index=0):
        if index >= len(arr):
            return None
        node = Node(arr[index])
        node.left = build(2 * index + 1)
        node.right = build(2 * index + 2)
        return node
    return build(0)


def generate_color(step, total_steps):
    start = (1, 100, 150)    
    end = (160, 190, 210)     
    r = int(start[0] + (end[0] - start[0]) * (step / total_steps))
    g = int(start[1] + (end[1] - start[1]) * (step / total_steps))
    b = int(start[2] + (end[2] - start[2]) * (step / total_steps))
    return f"#{r:02X}{g:02X}{b:02X}"


def dfs_traversal(root):
    stack = [root]
    visited = []
    step = 0
    total = count_nodes(root)
    while stack:
        node = stack.pop()
        if node and node not in visited:
            visited.append(node)
            node.color = generate_color(step, total)
            step += 1
            draw_tree(root, title=f"DFS step {step}: visited {node.val}")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


def bfs_traversal(root):
    queue = deque([root])
    visited = []
    step = 0
    total = count_nodes(root)
    while queue:
        node = queue.popleft()
        if node and node not in visited:
            visited.append(node)
            node.color = generate_color(step, total)
            step += 1
            draw_tree(root, title=f"BFS step {step}: visited {node.val}")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)



arr = [10, 6, 15, 3, 8, 12, 18]
tree_root = build_tree_from_array(arr)

print("DFS")
dfs_traversal(tree_root)

tree_root = build_tree_from_array(arr)
print("BFS")
bfs_traversal(tree_root)

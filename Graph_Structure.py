import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class graph_structure:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        """เพิ่มเส้นเชื่อมระหว่าง node และ neighbor"""
        if node not in self.graph:
            self.graph[node] = []
        if neighbor not in self.graph:
            self.graph[neighbor] = []
        self.graph[node].append(neighbor)
        self.graph[neighbor].append(node)

    def show_graph(self):
        """แสดงกราฟแบบข้อความ"""
        for node, neighbors in self.graph.items():
            print(f"{node} -> {neighbors}")

    def plot_graph(self, highlight_nodes=None, current_node=None, title="Graph Structure"):
        """แสดงกราฟแบบต่อเนื่องในหน้าต่างเดียว"""
        G = nx.Graph(self.graph)
        pos = nx.spring_layout(G, seed=42)
        plt.clf()  # ล้างหน้าจอเก่า ไม่ต้องเปิดใหม่

        node_colors = []
        for n in G.nodes():
            if current_node == n:
                node_colors.append("tomato")       # โหนดที่กำลังเยี่ยมชม
            elif highlight_nodes and n in highlight_nodes:
                node_colors.append("lightcoral")   # โหนดที่เยี่ยมชมแล้ว
            else:
                node_colors.append("skyblue")

        nx.draw(
            G, pos,
            with_labels=True,
            node_color=node_colors,
            node_size=1200,
            font_size=12,
            font_weight='bold',
            edge_color='gray'
        )
        plt.title(title)
        plt.pause(0.7)  # หน่วงเวลาให้เห็นการเปลี่ยนแปลง

    def bfs(self, start):
        """Breadth-First Search แบบต่อเนื่อง"""
        visited = set()
        queue = deque([start])

        plt.ion()  # เปิดโหมดโต้ตอบ
        print("\nBFS Traversal Order:")
        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                self.plot_graph(highlight_nodes=visited, current_node=node, title=f"BFS Visiting: {node}")
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        print("\nTraversal complete!")
        plt.ioff()
        plt.show()

    def dfs(self, start):
        """Depth-First Search แบบต่อเนื่อง"""
        visited = set()
        stack = [start]

        plt.ion()
        print("\nDFS Traversal Order:")
        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                self.plot_graph(highlight_nodes=visited, current_node=node, title=f"DFS Visiting: {node}")
                for neighbor in reversed(self.graph[node]):  # reversed เพื่อให้ลำดับเหมือน recursion
                    if neighbor not in visited:
                        stack.append(neighbor)
        print("\nTraversal complete!")
        plt.ioff()
        plt.show()


if __name__ == "__main__":
    g = graph_structure()
    g.add_edge('A','B')
    g.add_edge('A','C')
    g.add_edge('B','D')
    g.add_edge('C','D')
    g.add_edge('D','E')

    print("Graph Structure")
    g.show_graph()

    g.bfs('A')
    g.dfs('A')

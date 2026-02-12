import networkx as nx

class ContextGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_user(self, user_id, role):
        self.graph.add_node(user_id, type="user", role=role)

    def add_goal(self, goal_id, description):
        self.graph.add_node(goal_id, type="goal", description=description)

    def link_user_goal(self, user_id, goal_id):
        self.graph.add_edge(user_id, goal_id, relation="HAS_GOAL")

    def add_deadline(self, goal_id, deadline):
        self.graph.add_node(deadline, type="deadline")
        self.graph.add_edge(goal_id, deadline, relation="HAS_DEADLINE")

    def set_screen(self, user_id, screen):
        self.graph.add_node(screen, type="screen")
        self.graph.add_edge(user_id, screen, relation="VIEWING")

    def get_user_context(self, user_id):
        context = {}
        for neighbor in self.graph.neighbors(user_id):
            edge = self.graph.get_edge_data(user_id, neighbor)
            context[neighbor] = edge["relation"]
        return context
    
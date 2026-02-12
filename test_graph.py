from context_graph import ContextGraph

cg = ContextGraph()

cg.add_user("student_1", "student")
cg.add_goal("ml_assignment", "Finish ML assignment")
cg.link_user_goal("student_1", "ml_assignment")
cg.add_deadline("ml_assignment", "Friday")
cg.set_screen("student_1", "assignment_page")

print(cg.get_user_context("student_1"))

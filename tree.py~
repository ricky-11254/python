class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)

root = TreeNode("Root")
child1 = TreeNode("Child1")
child2 = TreeNode("Child2")
root.add_child(child1)
root.add_child(child2)
print(root.value)
for child in root.children:
    print(f"-->{child.value}")

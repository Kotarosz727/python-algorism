class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

def insert(node: Node, value: int) -> Node:
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)            
    else:
        node.right = insert(node.right, value)
    return node

def inOrder(node: Node) -> None:
    if node is not None:
        inOrder(node.left)
        print(node.value)
        inOrder(node.right)
    return    

def search(node: Node, value) -> bool:
    if node is None:
        return False
        
    if value == node.value:
        return True
    elif value < node.value:
        return search(node.left, value)
    else:
        return search(node.right, value)    
                


root = None
root = insert(root, 3)
root = insert(root, 6)        
root = insert(root, 5)        
root = insert(root, 1)        
root = insert(root, 2)        
root = insert(root, 7)        
root = insert(root, 8)        
root = insert(root, 10)   
# inOrder(root)     
res = search(root, 11)
print(res)
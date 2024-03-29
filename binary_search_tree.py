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

def min_val(node: Node) -> None:
    current = node
    if current.left is None:
        return current
    return min_val(current.left)    

def remove(node: Node, value:int) -> None:
    if node is None:
        return node

    if value < node.value:
        node.left = remove(node.left, value)
    elif value > node.value:
        node.right = remove(node.right, value)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        temp = min_val(node.right)
        node.value = temp.value
        node.right = remove(node.right, temp.value)   
    return node    

root = None
root = insert(root, 3)
root = insert(root, 6)
root = insert(root, 5)        
root = insert(root, 7)    
root = insert(root, 1)        
root = insert(root, 10)    
root = insert(root, 2)      
root = remove(root, 6)
inOrder(root)
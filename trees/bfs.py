def level_order_traversal(root):
    if root == None:
        return None
    answer = []
    q = Queue()
    q.put(root)
    while q.empty() == False:
        level = []
        level_node_count = q.qsize()
        for i in range(level_node_count):
            node = q.get()
            level.append(node.value)
            if node.left != None:
                q.put(node.left)
            if node.right != None:
                q.put(node.right)
        answer.append(level)
    return answer
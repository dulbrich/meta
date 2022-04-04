class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values_per_level = []
        
        if not root:
            return values_per_level

        nodes_to_visit_queue = deque([root])
        
        while nodes_to_visit_queue:
            cur_level_num_nodes = len(nodes_to_visit_queue)
            cur_level_nodes_values = []

            for _ in range(cur_level_num_nodes):
                cur_visited_node = nodes_to_visit_queue.popleft()
                cur_level_nodes_values.append(cur_visited_node.val)

                if cur_visited_node.left:
                    nodes_to_visit_queue.append(cur_visited_node.left)
                if cur_visited_node.right:
                    nodes_to_visit_queue.append(cur_visited_node.right)  

            values_per_level.append(cur_level_nodes_values)

        return values_per_level
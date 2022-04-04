class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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

                for child in cur_visited_node.children:
                    nodes_to_visit_queue.append(child)

            values_per_level.append(cur_level_nodes_values)

        return values_per_level       
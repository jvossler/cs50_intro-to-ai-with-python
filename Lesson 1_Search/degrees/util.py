class Node():
    """_summary_
    """
    
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    """_summary_
    """
    
    def __init__(self):
        """_summary_
        """
        self.frontier = []

    def add(self, node):
        """_summary_

        Args:
            node (_type_): _description_
        """
        self.frontier.append(node)

    def contains_state(self, state):
        """_summary_

        Args:
            state (_type_): _description_

        Returns:
            _type_: _description_
        """
        return any(node.state == state for node in self.frontier)

    def empty(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        
        return len(self.frontier) == 0

    def remove(self):
        """_summary_

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """
        
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):
    """_summary_

    Args:
        StackFrontier (_type_): _description_
    """

    def remove(self):
        """

        Raises:
            Exception: _description_

        Returns:
            _type_: _description_
        """
        
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

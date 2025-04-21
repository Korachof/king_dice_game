# File for Player classes and their functions

class Player:
    def __init__(self, name, support_pool, rank):
        self._name = name
        self._support_pool = support_pool
        self._rank = rank
        self._health_status = 2     #2 for healthy. 1 Sick. 0 Dying. -1+ Dead.

# GETTERS
    def get_name(self) -> str:
        return self._name
    
    def get_support_pool(self) -> int:
        return self._support_pool
    
    def get_rank(self) -> int:
        return self._rank
    
# SETTERS
    def set_name(self, new_name) -> str:
        self._name = new_name
        return self._name
    
    def set_support_pool(self, new_pool) -> int:
        self._support_pool = new_pool
        return self._support_pool
    
    def set_rank(self, new_rank) -> int:
        self._rank = new_rank
        return self._rank
    
# VARY FUNCTIONS
    def increment_support_pool(self, amount) -> int:
        self._support_pool += amount
        return self._support_pool
    
    def increment_rank(self, amount) -> int:
        self._rank += amount
        return self._rank


    

    


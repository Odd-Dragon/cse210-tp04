from game.casting.actor import Actor


class Mineral(Actor):
    """
    
    The responsibility of an Mineral is to be caught and give (or take) wealth.
    """
    def __init__(self):
        super().__init__()
        self._points = 1
        
    def get_points(self):
        """Gets the mineral's point value.
        
        Returns:
            int: the points
        """
        return self._points
    
    def set_points(self, mineral_type, mineral_number):
        """ Assign points based on image.
        
        Args:
            points (int): The appropriate number of points.
        """
        if mineral_type == 1:
            if mineral_number == 1:
                self._points = 1
            elif mineral_number == 2:
                self._points = 10
            elif mineral_number == 3:
                self._points = 3
        elif mineral_type == 2:
            if mineral_number == 1:
                self._points = -1
            elif mineral_number == 2:
                self._points = -3
            elif mineral_number == 3:
                self._points = -10
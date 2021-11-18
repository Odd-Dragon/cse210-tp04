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
    
    def set_points(self):
        """ Assign points based on image.
        
        Args:
            points (int): The appropriate number of points.
        """
        if self.get_image == "gem.jpg":
            self._points = 1
        elif self.get_image == "gem2.jpg":
            self._points = 10
        elif self.get_image == "gem3.jpg":
            self._points = 3
        elif self.get_image == "rock1.jpg":
            self._points = -1
        elif self.get_image == "rock2.jpg":
            self._points = -3
        elif self.get_image == "rock3.jpg":
            self._points = -10
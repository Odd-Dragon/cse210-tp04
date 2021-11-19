from game.casting.mineral import Mineral
from game.shared.point import Point
from game.shared.color import Color
import time
from random import randint as rd
SPAWN_INTERVAL = 2

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._last_spawn = time.time()

        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the gold_digger.
        
        Args:
            cast (Cast): The cast of actors.
        """
        gold_digger = cast.get_first_actor("gold_digger")
        velocity = self._keyboard_service.get_direction()
        gold_digger.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the gold_digger's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        score = cast.get_first_actor("score")
        gold_digger = cast.get_first_actor("gold_digger")
        

        
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        gold_digger.move_next(max_x, max_y)
        
        if time.time() - self._last_spawn >= SPAWN_INTERVAL:
            x = rd(int(max_x / 8), int(max_x - max_x / 8))
            y = 0
            gem_type = rd(1, 3)
            position = Point(x,y)
            mineral = Mineral()
            mineral.set_position(position)
            mineral.set_image(f"data/images/gem{gem_type}.png")
            mineral.set_velocity(Point(0,3))
            cast.add_actor("minerals", mineral)
            self._last_spawn = time.time()

        for actor in cast.get_all_actors():
            actor.move_next(max_x, max_y)




        minerals = cast.get_actors("minerals")
        for mineral in minerals:
            if gold_digger.get_position().equals(mineral.get_position()):
                points = mineral.get_points()
                score.add_points(points)
                cast.remove_actor("minerals", mineral)
        

        
                
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.draw_actors_image(actors)
        self._video_service.flush_buffer()

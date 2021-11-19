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

    def __init__(self, keyboard_service, video_service, physics_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._physics_service = physics_service
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
        
        
        if time.time() - self._last_spawn >= SPAWN_INTERVAL:
            x = rd(int(max_x / 8), int(max_x - max_x / 8))
            y = 0
            position = Point(x,y)
            mineral_or_rock = rd(1,2) 
            if mineral_or_rock == 1:
                gem_type = rd(1, 3)
                
                gem = Mineral()
                gem.set_position(position)
                gem.set_image(f"data/images/gem{gem_type}.png")
                gem.set_velocity(Point(0,3))
                gem.set_points(mineral_or_rock, gem_type)
                gem.set_height(30)
                gem.set_width(30)
                cast.add_actor("minerals", gem)
            else:
                rock_type = rd(1, 3)
                rock = Mineral()
                rock.set_position(position)
                rock.set_image(f"data/images/rock{rock_type}.png")
                rock.set_velocity(Point(0,3))
                rock.set_points(mineral_or_rock, rock_type)
                rock.set_width(30)
                rock.set_height(30)
                cast.add_actor("rocks", rock)

            self._last_spawn = time.time()        
            

        for actor in cast.get_all_actors():
            actor.move_next()




        minerals = cast.get_actors("minerals")
        rocks = cast.get_actors("rocks")
        for mineral in minerals:
            if self._physics_service.check_collision(mineral, gold_digger):
                
                points = mineral.get_points()
                score.add_points(points)
                cast.remove_actor("minerals", mineral)

        for rock in rocks:
            if self._physics_service.check_collision(rock, gold_digger):
                points = rock.get_points()
                score.add_points(points)
                cast.remove_actor("rocks", rock)
            

        

        
                
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

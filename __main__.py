import os
import random

from game.casting.actor import Actor
from game.casting.mineral import Mineral
from game.casting.cast import Cast
from game.casting.score import Score

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
CAPTIONS = ["Greed: Are you feeling greedy?", "Greed: Be ready to risk it all for money"
, "Greed: Is a life worth 10,000 gems? No, much less.", "Greed: Watch for rolling rocks"
, "Greed: Who would risk their life for gems?", "Greed: Not as greedy as Cortez"]
CAPTION = CAPTIONS[random.randint(0,len(CAPTIONS)-1)]
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/images"
WHITE = Color(255, 255, 255)
DEFAULT_MINERALS = 0


def main():
    
    # create the cast
    cast = Cast()
    
    # create the score
    score = Score()
    position = Point(0, 0)
    score.set_position(position)
    cast.add_actor("score", score)
    
    # create the gold_digger
    # create the player
    x = int(MAX_X / 2)
    y = int(MAX_Y-1)
    position = Point(x, y)

    gold_digger = Actor()
    gold_digger.set_text("#")
    gold_digger.set_font_size(FONT_SIZE)
    gold_digger.set_color(WHITE)
    gold_digger.set_position(position)
    cast.add_actor("gold_digger", gold_digger)

    
    # create the artifacts
    #with open(DATA_PATH) as file:
    #   data = file.read()
    #  messages = data.splitlines()
    """
    for n in range(DEFAULT_MINERALS):
        text = chr(random.randint(33, 126))
        message = messages[n]

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        mineral = Mineral()
        mineral.set_text(text)
        mineral.set_font_size(FONT_SIZE)
        mineral.set_color(color)
        mineral.set_position(position)
        mineral.set_message(message)
        cast.add_actor("minerals", mineral)"""
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
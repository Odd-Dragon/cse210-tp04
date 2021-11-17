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
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    gold_digger = Actor()
    gold_digger.set_text("#")
    gold_digger.set_font_size(FONT_SIZE)
    gold_digger.set_color(WHITE)
    gold_digger.set_position(position)
    cast.add_actor("gold_digger", gold_digger)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
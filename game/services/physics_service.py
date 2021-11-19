import pyray

class PhysicsService:

    def __init__(self):
        pass

    def check_collision(self, actor1, actor2):
        rec1 = pyray.Rectangle(actor1.get_position().get_x(), actor1.get_position().get_y(), actor1.get_width(), actor1.get_height())
        rec2 = pyray.Rectangle(actor2.get_position().get_x(), actor2.get_position().get_y(), actor2.get_width(), actor2.get_height())
        return pyray.check_collision_recs(rec1, rec2)
        
        
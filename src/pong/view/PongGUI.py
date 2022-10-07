# package pong.view
import pygame 
import time


from pong.model import *
from pong.event.ModelEvent import ModelEvent
from pong.event.EventBus import EventBus
from pong.event.EventHandler import EventHandler
from pong.view.theme.Cool import Cool
from pong.view.theme.Duckie import Duckie

from pong.model.Paddle import Paddle
from pong.model.Config import *

from pong.model.Ball import Ball
from pong.model.Paddle import Paddle

pygame.init()


class PongGUI:
    """
    The GUI for the Pong game (except the menu).
    No application logic here just GUI and event handling.

    Run this to run the game.

    See: https://en.wikipedia.org/wiki/Pong
    """

    clock = pygame.time.Clock()
    running = False    # Is game running? ...No?



    # ------- Keyboard handling ----------------------------------
    @classmethod
    def key_pressed(cls, event):
        if not cls.running:
            return
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # TODO
                pass
            elif event.key == pygame.K_DOWN:
                # TODO
                pass
            elif event.key == pygame.K_q:
                # TODO
                pass
            elif event.key == pygame.K_a:
                # TODO
                pass

    @classmethod
    def key_released(cls, event):
        if not cls.running:
            return
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                # TODO
                pass
            elif event.key == pygame.K_DOWN:
                # TODO
                pass
            elif event.key == pygame.K_q:
                # TODO
                pass
            elif event.key == pygame.K_a:
                # TODO
                pass

    # ---- Menu handling (except themes) -----------------

    # TODO Optional

    @classmethod
    def new_game(cls):
        # TODO rebuild OO model as needed
        pass

    @classmethod
    def kill_game(cls):
        cls.running = False
        # TODO kill all aspects of game

    # -------- Event handling (events sent from model to GUI) ------------

    class ModelEventHandler(EventHandler):
        def on_model_event(self, evt: ModelEvent):
            if evt.event_type == ModelEvent.EventType.NEW_BALL:
                # TODO Optional
                pass
            elif evt.event_type == ModelEvent.EventType.BALL_HIT_PADDLE:
                PongGUI.assets.ball_hit_paddle_sound.play()
            elif evt.event_type == ModelEvent.EventType.BALL_HIT_WALL_CEILING:
                # TODO Optional
                pass

    # ################## Nothing to do below ############################

    # ---------- Theme handling ------------------------------

    assets = None

    @classmethod
    def handle_theme(cls, menu_event):
        s = "Cool"  # ((MenuItem) menu_event.getSource()).getText()
        last_theme = cls.assets
        try:
            if s == "Cool":
                cls.assets = Cool()
            elif s == "Duckie":
                cls.assets = Duckie()
            else:
                raise ValueError("No such assets " + s)
        except IOError as ioe:
            cls.assets = last_theme

    # ---------- Rendering -----------------
    @classmethod
    def render(cls):
        cls.__draw_background()
        


        cls.__update_screen()
        
        #screen = pygame.display.se
        # self.__draw_background()
        # self.__show_points()
        # self.__draw_ground()
        # self.__draw_bucket()
        # self.__draw_drops()
        # self.__update_screen()

    @classmethod
    def __draw_background(cls):
        bg = Cool.get_background()

        size = ([GAME_WIDTH, GAME_HEIGHT])
        screen = pygame.display.set_mode(size)
        screen.blit(bg, (0, 0))

    # def __show_points(self):
    #     points = self.ctr_model.get_points()
    #     img, rect = self.__create_points_image(points)
    #     self.__draw_points_image(img, rect)

    # def __draw_points_image(self, img, rect):
    #     rect.topleft = (20, 20)
    #     self.screen.blit(img, rect)

    # def __create_points_image(self, points):
    #     text = f"Points: {points}"
    #     img = self.points_font.render(text, True, self.RED) Vi borde ha: Cool.get_background()
    #     rect = img.get_rect()
    #     return img, rect


    
    @staticmethod
    def __update_screen():
        pygame.display.flip()



    #WHITE = (255, 255, 255)
    #RED   = (255,   0,   0)

    # def __init__(self):
        # drops = []
        # bucket = self.__create_bucket()
        # ground = self.__create_ground()
        # self.ctr_model = CatchTheRain(drops, ground, bucket)
        #self.screen = pg.display.set_mode([GAME_WIDTH, GAME_HEIGHT])
        # self.points_font = pg.font.SysFont(None, 36)
        # self.clock = pg.time.Clock()    
        # TODO
        pass


        #self.screen.fill(self.WHITE)
    # ---------- Game loop ----------------

    @classmethod
    def run(cls):
        ball = Ball
        paddle_right = Paddle
        paddle_left = Paddle
        keep_going = True
        while keep_going:
            cls.clock.tick(GAME_SPEED)
            cls.update()
            keep_going = cls.handle_events()
        pygame.quit()


        # keep_going = True
        # while keep_going:
            #self.clock.tick(GAME_SPEED)
            # self.update()
            # keep_going = self.handle_events()
        # pg.quit()

    @classmethod
    def update(cls):
        # TODO
        cls.render()

        
        # self.ctr_model.update(time_ns())
        # self.render()
        pass

    @classmethod
    def handle_events(cls):
        # TODO
        keep_going = True
        events = pygame.event.get()

        for event in events:
            keep_going = cls.__check_for_quit(event)

        return keep_going

        
        # keep_going = True
        # events = pg.event.get()
        # for event in events:
            # self.__handle_key_event(event)
            # keep_going &= self.__check_for_quit(event)
        # return keep_going

    @staticmethod
    def __check_for_quit(event) -> bool:
        return event.type != pygame.QUIT

    @classmethod
    def handle_key_event(cls):
        pass


if __name__ == "__main__":
    PongGUI.run()

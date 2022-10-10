# package pong.view
import pygame 
import time

from pong_game.model import *
from pong_game.event.ModelEvent import ModelEvent
from pong_game.event.EventBus import EventBus
from pong_game.event.EventHandler import EventHandler
from pong_game.view.theme.Cool import Cool
from pong_game.view.theme.Duckie import Duckie

from pong_game.model.Paddle import Paddle
from pong_game.model.Config import *

from pong_game.model.Ball import Ball
from pong_game.model.Paddle import Paddle

from pong_game.model.Pong import Pong

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

    size = ([GAME_WIDTH, GAME_HEIGHT])
    screen = pygame.display.set_mode(size)

    ball = Ball()
    paddle_right = Paddle(GAME_WIDTH - 20)
    paddle_left = Paddle(10)

    pong_model = Pong(ball, paddle_right, paddle_left)


    # ------- Keyboard handling ----------------------------------
    @classmethod
    def key_pressed(cls, event):
        if not cls.running:
            return
        if event.key == pygame.K_UP:
            cls.paddle_right.set_paddle_direction(-1)
            
        elif event.key == pygame.K_DOWN:
            # TODO
            cls.paddle_right.set_paddle_direction(1)
        elif event.key == pygame.K_q:
            # TODO
            cls.paddle_left.move_up()
        elif event.key == pygame.K_a:
            # TODO
            cls.paddle_left.move_down()

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
                pass
            elif event.key == pygame.K_a:
                

    # ---- Menu handling (except themes) -----------------

    # TODO Optional

    @classmethod
    def new_game(cls):
        # TODO rebuild OO model as needed
        # pong_model = Pong(ball, paddle_right, paddle_left)
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
        cls.__draw_ball()
        cls.__draw_paddle()

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

        # size = ([GAME_WIDTH, GAME_HEIGHT])
        # screen = pygame.display.set_mode(size)
        cls.screen.blit(bg, (0, 0))


    @classmethod
    def __draw_paddle(cls):
        left_paddle_surface = Cool.get_image(Cool.left_paddle_img_file)
        left_paddle_surface = pygame.transform.scale(left_paddle_surface,
                                             (Paddle.get_width(cls.paddle_left), Paddle.get_height(cls.paddle_left)))

        right_paddle_surface = Cool.get_image(Cool.right_paddle_img_file)
        right_paddle_surface = pygame.transform.scale(right_paddle_surface,
                                              (Paddle.get_width(cls.paddle_right), Paddle.get_height(cls.paddle_right)))

        
        cls.screen.blit(left_paddle_surface, (cls.paddle_left.get_x(), cls.paddle_right.get_y()))
        cls.screen.blit(right_paddle_surface, (cls.paddle_right.get_x(), cls.paddle_right.get_y()))


    @classmethod
    def __draw_ball(cls):
        ball = Cool.get_image("coolBall.png")
        ball = pygame.transform.scale(ball, (Ball.get_width(cls.ball), Ball.get_height(cls.ball)))
        cls.screen.blit(ball, (cls.ball.get_x(), cls.ball.get_y()))

    #@classmethod
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

        pong_model = Pong(ball, paddle_right, paddle_left)

        keep_going = True
        while keep_going:
            cls.clock.tick(GAME_SPEED)
            keep_going = cls.handle_events()
            cls.update()
        pygame.quit()

    @classmethod
    def update(cls):
        # TODO
        # cls.handle_events()
        cls.render()
        

    @classmethod
    def handle_events(cls):
        # TODO
        keep_going = True
        events = pygame.event.get()

        for event in events:
            keep_going = cls.__check_for_quit(event)
            if event.type == pygame.KEYDOWN:
                cls.key_pressed(event)
            elif event.type == pygame.KEYUP:
                cls.key_released(event)

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



if __name__ == "__main__":
    PongGUI.run()

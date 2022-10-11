# package pong.view
import pygame 
from time import time_ns

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

    
    running = True    # Is game running? ...No?

    size = ([GAME_WIDTH, GAME_HEIGHT])
    screen = pygame.display.set_mode(size)

    def __init__(self) -> None:
        self.ball = Ball()
        self.paddle_right = Paddle(GAME_WIDTH - 20)
        self.paddle_left = Paddle(10)
        self.pong_model = Pong(self.ball, self.paddle_left, self.paddle_right)
        self.points_font = pygame.font.SysFont(None, 36)
        self.clock = pygame.time.Clock()

    # ------- Keyboard handling ----------------------------------

    def key_pressed(self, event):
        if not self.running:
            return
        if event.key == pygame.K_UP:
            self.pong_model.move_the_paddle(-1, "right")
            
        elif event.key == pygame.K_DOWN:
            self.pong_model.move_the_paddle(1, "right")

        elif event.key == pygame.K_q:
            self.pong_model.move_the_paddle(-1, "left")

        elif event.key == pygame.K_a:
            self.pong_model.move_the_paddle(1, "left")


    def key_released(self, event):
        if not self.running:
            return
        if event.key == pygame.K_UP:
            self.pong_model.move_the_paddle(0, "right")

        elif event.key == pygame.K_DOWN:
            self.pong_model.move_the_paddle(0, "right")

        elif event.key == pygame.K_q:
            self.pong_model.move_the_paddle(0, "left")
    
        elif event.key == pygame.K_a:
            self.pong_model.move_the_paddle(0, "left")
    
    # move_up:
        # y -= speed


    # ---- Menu handling (except themes) -----------------

    # TODO Optional

    def new_game(self):
        # TODO rebuild OO model as needed
        # pong_model = Pong(ball, paddle_right, paddle_left)
        pass


    def kill_game(self):
        self.running = False
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

    def handle_theme(self, menu_event):
        s = "Cool"  # ((MenuItem) menu_event.getSource()).getText()
        last_theme = self.assets
        try:
            if s == "Cool":
                self.assets = Cool()
            elif s == "Duckie":
                self.assets = Duckie()
            else:
                raise ValueError("No such assets " + s)
        except IOError as ioe:
            self.assets = last_theme

    # ---------- Rendering -----------------
    def render(self):
        self.__draw_background()
        self.__draw_ball()
        self.__draw_paddle()
        self.__show_points()

        self.__update_screen()
        
        #screen = pygame.display.se
        # self.__draw_background()
        # self.__show_points()
        # self.__draw_ground()
        # self.__draw_bucket()
        # self.__draw_drops()
        # self.__update_screen()
        
    def __show_points(self):
        points = self.pong_model.get_points_left()
        img, rect = self.__create_points_image(points)
        self.__draw_points_image(img, rect)

    def __draw_points_image(self, img, rect):
        rect.topleft = (20, 20)
        self.screen.blit(img, rect)

    def __create_points_image(self, points):
        text = f"Points: {points}"
        RED = (255, 0, 0)
        img = self.points_font.render(text, True, RED)
        rect = img.get_rect()
        return img, rect

    def __draw_background(self):
        bg = Cool.get_background()
        bg = pygame.transform.scale(bg, (600, 400))
        self.screen.blit(bg, (0, 0))

    def __draw_paddle(self):
        left_paddle_surface = Cool.get_image(Cool.left_paddle_img_file)
        left_paddle_surface = pygame.transform.scale(left_paddle_surface,
                                             (Paddle.get_width(self.paddle_left), Paddle.get_height(self.paddle_left)))

        right_paddle_surface = Cool.get_image(Cool.right_paddle_img_file)
        right_paddle_surface = pygame.transform.scale(right_paddle_surface,
                                              (Paddle.get_width(self.paddle_right), Paddle.get_height(self.paddle_right)))

        
        self.screen.blit(left_paddle_surface, (self.paddle_left.get_x(), self.paddle_left.get_y()))
        self.screen.blit(right_paddle_surface, (self.paddle_right.get_x(), self.paddle_right.get_y()))


    def __draw_ball(self):
        ball_surface = Cool.get_image("coolBall.png")
        ball_surface = pygame.transform.scale(ball_surface, (Ball.get_width(self.ball), Ball.get_height(self.ball)))
        self.screen.blit(ball_surface, (self.ball.get_x(), self.ball.get_y()))

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

    def run(self):
        keep_going = True
        while keep_going:
            self.clock.tick(GAME_SPEED)
            keep_going = self.handle_events()
            self.update()
            
        pygame.quit()
        
    def update(self):
        # TODO
        self.pong_model.update(time_ns())
        self.render()
        
    def handle_events(self):
        # TODO
        keep_going = True
        events = pygame.event.get()

        for event in events:
            keep_going = self.__check_for_quit(event)
            if event.type == pygame.KEYDOWN:
                self.key_pressed(event)

            elif event.type == pygame.KEYUP:
                self.key_released(event)

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
    gui = PongGUI()
    gui.run()
    #PongGUI.run()

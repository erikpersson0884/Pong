import pygame 

from pong_game.event.EventHandler import EventHandler
from pong_game.event.ModelEvent import ModelEvent

from pong_game.view.theme.Duckie import Duckie
from pong_game.view.theme.Cool import Cool

from pong_game.model.Config import *
from pong_game.model.Pong import Pong
from pong_game.model.Ball import Ball
from pong_game.model.Paddle import Paddle



class PongGUI:
    """
    The GUI for the Pong game (except the menu).
    No application logic here just GUI and event handling.

    Run this to run the game.

    See: https://en.wikipedia.org/wiki/Pong
    """
    pygame.init()
    running = False

    def __init__(self) -> None:
        self.__keep_going = False
        self.assets = self.choose_theme()
        self.screen = pygame.display.set_mode([GAME_WIDTH, GAME_HEIGHT])

        self.ball = Ball()
        self.paddle_left = Paddle(10)
        self.paddle_right = Paddle(GAME_WIDTH - 20)
        self.pong_model = Pong(self.ball, self.paddle_left, self.paddle_right)

        self.event_sound_handler = PongGUI.ModelEventHandler(self.assets)
        self.points_font = pygame.font.SysFont(FONT, FONT_SIZE)
        self.clock = pygame.time.Clock()


    # ------- Keyboard handling ----------------------------------

    def key_pressed(self, event):
        if not self.running:
            if event.type == pygame.KEYDOWN:
                self.running = True

        elif event.key == pygame.K_UP:
            self.pong_model.move_the_paddle(-1, "right")
            
        elif event.key == pygame.K_DOWN:
            self.pong_model.move_the_paddle(1, "right")

        elif event.key == pygame.K_q:
            self.pong_model.move_the_paddle(-1, "left")

        elif event.key == pygame.K_a:
            self.pong_model.move_the_paddle(1, "left")


    def key_released(self, event):
        if not self.running:
            pass
        
        elif event.key == pygame.K_UP:
            self.pong_model.move_the_paddle(0, "right")

        elif event.key == pygame.K_DOWN:
            self.pong_model.move_the_paddle(0, "right")

        elif event.key == pygame.K_q:
            self.pong_model.move_the_paddle(0, "left")
    
        elif event.key == pygame.K_a:
            self.pong_model.move_the_paddle(0, "left")



    # -------- Event handling (events sent from model to GUI) ------------

    class ModelEventHandler(EventHandler):
        def __init__(self, assets) -> None:
            super().__init__()
            self.assets = assets
        
        def on_model_event(self, evt: ModelEvent):
            if evt.event_type == ModelEvent.EventType.BALL_HIT_PADDLE:
                self.assets.get_sound(self.assets.ball_hit_paddle_sound_file).play()


    # ---------- Theme handling ------------------------------

    @staticmethod
    def choose_theme() -> Cool | Duckie:
        while True:
            print("Current themes are Cool or Duckie")
            theme = input("Choose the theme: ").lower()
            if theme in ["cool", "duckie"]:
                break
    
        if theme == "cool":
            return Cool()
            
        elif theme == "duckie":
            return Duckie()

        
    # ---------- Rendering -----------------

    def render(self):
        self.__draw_background()
        self.__draw_paddles()
        self.__draw_ball()
        self.__draw_points()
        self.__update_screen()
    

    def __draw_background(self):
        bg = self.assets.get_background()
        bg = pygame.transform.scale(bg, (GAME_WIDTH, GAME_HEIGHT))
        self.screen.blit(bg, (0, 0))


    def __draw_paddles(self):
        left_paddle_surface = self.assets.get_image(self.assets.left_paddle_img_file)
        left_paddle_surface = pygame.transform.scale(left_paddle_surface,
                                                    (Paddle.get_width(self.paddle_left), Paddle.get_height(self.paddle_left)))

        right_paddle_surface = self.assets.get_image(self.assets.right_paddle_img_file)

        right_paddle_surface = pygame.transform.scale(right_paddle_surface,
                                                    (Paddle.get_width(self.paddle_right), Paddle.get_height(self.paddle_right)))

        self.screen.blit(left_paddle_surface, (self.paddle_left.get_x(), self.paddle_left.get_y()))
        self.screen.blit(right_paddle_surface, (self.paddle_right.get_x(), self.paddle_right.get_y()))

    
    def __draw_ball(self):
        ball_surface = self.assets.get_image(self.assets.ball)
        ball_surface = pygame.transform.scale(ball_surface, (Ball.get_width(self.ball), Ball.get_height(self.ball)))

        self.screen.blit(ball_surface, (self.ball.get_x(), self.ball.get_y()))


    def __draw_points(self):
        points_left = self.pong_model.get_points_left()
        points_left_img, points_left_rect = self.__create_points_image(points_left, BLUE)
        
        points_right = self.pong_model.get_points_right()
        points_right_img, points_right_rect = self.__create_points_image(points_right, RED)

        self.__draw_a_points_image(points_left_img, points_left_rect, 20, 20)
        self.__draw_a_points_image(points_right_img, points_right_rect, GAME_WIDTH-20, 20)

    def __create_points_image(self, points, color: tuple[int, int, int]):
        text = f"Points: {points}"
        img = self.points_font.render(text, True, color)
        rect = img.get_rect()
        return img, rect
    
    def __draw_a_points_image(self, img, rect, x: int, y: int):
        if x < GAME_WIDTH/2:
            rect.topleft = (x, y)
        else:
            rect.topright = (x, y)
        self.screen.blit(img, rect)
    

    @staticmethod
    def __update_screen():
        pygame.display.flip()

    # ---------- Game loop ----------------

    def run(self):
        self.__keep_going = True
        
        while self.__keep_going:
            self.clock.tick(GAME_SPEED)
            self.__keep_going = self.handle_events()
            self.update()
        
        pygame.quit()
        
    def update(self):
        if self.running == True:
            self.pong_model.update()

        if self.pong_model.get_pong_sound_event() == "ball_hit_paddle":
            self.event_sound_handler.on_model_event(ModelEvent(ModelEvent.EventType.BALL_HIT_PADDLE))
            self.pong_model.set_pong_sound_event("")

        self.render()
        
    def handle_events(self):
        events = pygame.event.get()

        for event in events:
            self.__keep_going = self.__check_for_quit(event)
            if event.type == pygame.KEYDOWN:
                self.key_pressed(event)

            elif event.type == pygame.KEYUP:
                self.key_released(event)

        return self.__keep_going

    @staticmethod
    def __check_for_quit(event) -> bool:
        return event.type != pygame.QUIT

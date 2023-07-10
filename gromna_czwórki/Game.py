import pygame
import sys
import constant as con
from Board import Board, Text
from Player import Player
from Token import Player1Token, Player2Token
from Menu import Menu


class Game:
    def __init__(self):
        self.menu = Menu()
        self.board = Board()
        self.rounds = 3
        self.player1 = Player(Player1Token(0, 0))
        self.player2 = Player(Player2Token(0, 0))
        self.current_player = self.player1
        self.rounds_text = Text(f"Rounds left: {self.rounds}", con.LIGHTBLUE, 0, 0)
        self.final_winner_text = Text("RED WINS THE MATCH!", con.RED, 0, 0)
        self.turn_text = Text("RED's TURN!", con.LIGHTBLUE, 0, 0)
        self.winner_text = Text("RED WINS!", con.LIGHTBLUE, 0, 0)
        self.points1 = Text(self.player1.points, con.RED, 0, 0)
        self.points2 = Text(self.player2.points, con.BLACK, 0, 0)

    @staticmethod
    def sound_play(name, loop=0):
        sound = con.SOUNDS[name]
        sound.play(loop)

    @staticmethod
    def sound_stop(name):
        sound = con.SOUNDS[name]
        sound.stop()

    def update(self):
        winner = self.winner()
        self.final_winner_text = Text("RED WINS THE MATCH!" if winner == 1 else "BLACK WINS THE MATCH!",
                                      con.RED if winner == 1 else con.BLACK, con.WIDTH / 2, con.HEIGHT / 2,
                                      font_size=70, outline_colour=con.JET_BLACK)
        self.rounds_text = Text(f"Rounds left: {self.rounds}", con.LIGHTBLUE,
                                con.WIDTH / 2, con.TOKEN_SIZE / 2 - 25, font_size=30, outline_colour=con.JET_BLACK)
        self.turn_text = Text("RED's TURN!" if self.current_player == self.player1 else "BLACK's TURN!", con.LIGHTBLUE,
                              con.WIDTH / 2, con.TOKEN_SIZE / 2 + 15, font_size=40, outline_colour=con.JET_BLACK)
        self.winner_text = Text("RED WINS!" if self.current_player == self.player1 else "BLACK WINS!",
                                con.RED if self.current_player == self.player1 else con.BLACK,
                                con.WIDTH / 2, con.HEIGHT / 2, font_size=120, outline_colour=con.JET_BLACK)
        self.points1 = Text(self.player1.points, con.RED, con.TOKEN_SIZE / 2, con.TOKEN_SIZE / 2, font_size=46,
                            outline_colour=con.JET_BLACK)
        self.points2 = Text(self.player2.points, con.BLACK, con.WIDTH - con.TOKEN_SIZE / 2, con.TOKEN_SIZE / 2,
                            font_size=46, outline_colour=con.JET_BLACK)
        self.current_player.update()

    def draw(self, surface):
        self.update()
        self.board.draw(surface)
        self.turn_text.draw(surface)
        self.rounds_text.draw(surface)
        self.current_player.draw(surface)
        self.player1.tokens.draw(surface)
        self.player2.tokens.draw(surface)
        self.points1.draw(surface)
        self.points2.draw(surface)

    def _handle_events(self):
        for event in pygame.event.get():
            posx = pygame.mouse.get_pos()[0] // con.TOKEN_SIZE
            if event.type == pygame.MOUSEMOTION:
                self.current_player.set_rect_center(posx * con.TOKEN_SIZE + con.TOKEN_SIZE / 2, con.TOKEN_SIZE * 1.5)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sound_play("put.wav")
                self.player1.set_rect_center(posx * con.TOKEN_SIZE + con.TOKEN_SIZE / 2, con.TOKEN_SIZE * 1.5)
                self.player2.set_rect_center(posx * con.TOKEN_SIZE + con.TOKEN_SIZE / 2, con.TOKEN_SIZE * 1.5)
                return self.board.add_token(posx, self.current_player)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def reset(self):
        self.player1.tokens.empty()
        self.player2.tokens.empty()
        self.board.grid = [[None] * con.BOARD_WIDTH for _ in range(con.BOARD_HEIGHT)]

    def restart(self):
        self.reset()
        self.current_player = self.player1
        self.player1.points = 0
        self.player2.points = 0
        self.rounds = 3
        self.update()

    def winner(self):
        if self.player1.points > self.player2.points:
            return 1
        elif self.player1.points < self.player2.points:
            return 2

    def start_menu(self, surface):
        # self.sound_play("background.mp3", -1)
        self.board.draw(surface)
        self.menu.buttons.clear()
        self.menu.start_menu = True
        self.menu.add_button("Start game", con.MENU_FONT_SIZE, con.WIDTH // 2, con.HEIGHT // 2 - 5)
        self.menu.add_button("<", 62, con.WIDTH // 2 - 50, con.HEIGHT // 2 + 90, 50)
        self.menu.add_button(">", 62, con.WIDTH // 2 + 50, con.HEIGHT // 2 + 90, 50)
        self.menu.add_button("Quit", con.MENU_FONT_SIZE, con.WIDTH // 2, con.HEIGHT // 2 + 150)
        self.handle_menu(surface)

    def finish_menu(self, surface):
        self.menu.buttons.clear()
        self.menu.start_menu = False
        self.menu.add_button("Play again", con.MENU_FONT_SIZE, con.WIDTH / 2, con.HEIGHT // 2)
        self.menu.add_button("Quit", con.MENU_FONT_SIZE, con.WIDTH // 2, con.HEIGHT // 2 + 100)
        self.handle_menu(surface)

    def handle_menu(self, surface):
        running = True
        while running:
            interaction = self.menu.draw_menu(surface, self.rounds)
            if interaction == "start game":
                self.run(surface)
                running = False
            elif interaction == "<" and self.rounds > 1:
                self.rounds -= 2
            elif interaction == ">" and self.rounds < 9:
                self.rounds += 2
            elif interaction == "play again":
                self.restart()
                self.start_menu(surface)
                running = False
            elif interaction == "quit":
                pygame.quit()
                sys.exit()

            pygame.display.update()

    def handle_win(self, surface):
        pygame.time.delay(400)
        self.current_player.points += 1
        self.rounds -= 1
        self.sound_play("win.wav")
        self.winner_text.draw(surface)
        pygame.display.update()
        pygame.time.delay(2500)
        self.reset()
        if self.rounds == 0:
            self.draw(surface)
            self.sound_stop("background.mp3")
            self.sound_play("final_win.wav")
            self.final_winner_text.draw(surface)
            pygame.display.update()
            pygame.time.delay(2500)
            self.finish_menu(surface)

    def handle_tie(self, surface):
        pygame.time.delay(400)
        self.winner_text = Text("IT'S A TIE!", (0, 0, 0), con.WIDTH / 2, con.HEIGHT / 2, font_size=120)
        self.winner_text.draw(surface)
        pygame.display.update()
        self.sound_play("tie.wav")
        pygame.time.delay(2500)
        self.restart()

    def run(self, surface):
        clock = pygame.time.Clock()

        window_open = True
        while window_open:
            self.draw(surface)

            if self._handle_events():
                if self.board.check_winner(self.current_player.token):
                    self.handle_win(surface)
                elif self.board.is_full():
                    self.handle_tie(surface)
                else:
                    self.current_player = self.player2 if self.current_player == self.player1 else self.player1

            pygame.display.flip()
            clock.tick(35)

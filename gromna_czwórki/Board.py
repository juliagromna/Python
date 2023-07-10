import pygame
import constant as con
import Token as t


class Board:
    def __init__(self):
        self.grid = [[None] * con.BOARD_WIDTH for _ in range(con.BOARD_HEIGHT)]

    def add_token(self, col, player):
        for row in range(con.BOARD_HEIGHT - 1, -1, -1):
            if self.grid[row][col] is None:
                self.grid[row][col] = player.token
                token = t.Token(player.token.image, col * con.TOKEN_SIZE + con.TOKEN_SIZE // 2,
                                row * con.TOKEN_SIZE + con.TOKEN_SIZE // 2 + con.BOARD_OFFSET_Y)
                player.tokens.add(token)
                return True
        return False

    def is_full(self):
        for row in range(con.BOARD_HEIGHT):
            for col in range(con.BOARD_WIDTH):
                if self.grid[row][col] is None:
                    return False
        return True

    def check_winner(self, token):
        # Sprawdzenie w pionie
        for col in range(con.BOARD_WIDTH):
            for row in range(con.BOARD_HEIGHT - 3):
                if (
                        self.grid[row][col] == token
                        and self.grid[row + 1][col] == token
                        and self.grid[row + 2][col] == token
                        and self.grid[row + 3][col] == token
                ):
                    return True

        # Sprawdzenie w poziomie
        for row in range(con.BOARD_HEIGHT):
            for col in range(con.BOARD_WIDTH - 3):
                if (
                        self.grid[row][col] == token
                        and self.grid[row][col + 1] == token
                        and self.grid[row][col + 2] == token
                        and self.grid[row][col + 3] == token
                ):
                    return True

        # Sprawdzenie po przekątnych
        for row in range(con.BOARD_HEIGHT - 3):
            for col in range(con.BOARD_WIDTH - 3):
                if (
                        self.grid[row][col] == token
                        and self.grid[row + 1][col + 1] == token
                        and self.grid[row + 2][col + 2] == token
                        and self.grid[row + 3][col + 3] == token
                ):
                    return True

                if (
                        self.grid[row][col + 3] == token
                        and self.grid[row + 1][col + 2] == token
                        and self.grid[row + 2][col + 1] == token
                        and self.grid[row + 3][col] == token
                ):
                    return True

        return False

    @staticmethod
    def draw(surface):
        surface.fill(con.GRAY)
        pygame.draw.rect(surface, con.DARK_PINK,
                         (0, con.BOARD_OFFSET_Y, con.WIDTH, con.HEIGHT - con.BOARD_OFFSET_Y), border_radius=con.RADIUS)
        pygame.draw.rect(surface, con.PINK, (con.OUTLINE_WIDTH, con.BOARD_OFFSET_Y + con.OUTLINE_WIDTH,
                                             con.WIDTH - con.OUTLINE_WIDTH * 2,
                                             con.HEIGHT - con.BOARD_OFFSET_Y - con.OUTLINE_WIDTH * 2),
                         border_radius=con.RADIUS)
        for row in range(con.BOARD_HEIGHT):
            for col in range(con.BOARD_WIDTH):
                pygame.draw.circle(
                    surface,
                    con.DARK_PINK,
                    (
                        col * con.TOKEN_SIZE + con.TOKEN_SIZE // 2,
                        row * con.TOKEN_SIZE + con.TOKEN_SIZE // 2 + con.BOARD_OFFSET_Y,
                    ),
                    con.TOKEN_SIZE // 2 - 5,
                )
                pygame.draw.circle(
                    surface,
                    con.GRAY,
                    (
                        col * con.TOKEN_SIZE + con.TOKEN_SIZE // 2,
                        row * con.TOKEN_SIZE + con.TOKEN_SIZE // 2 + con.BOARD_OFFSET_Y
                    ),
                    con.TOKEN_SIZE // 2 - 5 - con.OUTLINE_WIDTH,
                )


class Text:
    def __init__(self, text, text_colour, px, py, font_size=74, outline_colour=None, outline_width=1.5):
        super().__init__()
        self.text = str(text)
        font = pygame.font.Font(None, font_size)
        self.image = font.render(self.text, True, text_colour)
        self.draw_outline(text_colour, font, outline_colour, outline_width)
        self.rect = self.image.get_rect()
        self.rect.center = px, py

    def draw_outline(self, text_colour, font, outline_colour, outline_width):
        if outline_colour:
            outline = font.render(self.text, True, outline_colour)
            self.image = outline
            self.image.blit(outline, (outline_width, 0))
            self.image.blit(outline, (-outline_width, 0))
            self.image.blit(outline, (0, outline_width))
            self.image.blit(outline, (0, -outline_width))
            self.image.blit(font.render(self.text, True, text_colour), (0, 0))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

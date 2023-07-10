import pygame
import sys
import constant as con


class Menu:
    def __init__(self):
        self.rect = pygame.Rect(con.WIDTH // 6, con.HEIGHT // 6, con.MENU_WIDTH, con.MENU_HEIGHT)
        self.outline_rect = pygame.Rect(self.rect.x - 2, self.rect.y - 2, self.rect.width + 4, self.rect.height + 4)
        self.color = con.BEIGE
        self.outline_color = con.DARK_BEIGE
        self.buttons = []
        self.start_menu = True

    def add_button(self, text, font_size, x, y, width=con.BUTTON_WIDTH):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, con.MEDIUM_BEIGE)
        text_rect = text_surface.get_rect(center=(x, y))
        button_rect = pygame.Rect(text_rect.centerx - width // 2, text_rect.centery - font_size // 2, width, font_size)
        self.buttons.append((text, button_rect, font))

    def draw_menu(self, surface, rounds):
        pygame.draw.rect(surface, self.outline_color, self.outline_rect, border_radius=con.RADIUS)
        pygame.draw.rect(surface, self.color, self.rect, border_radius=con.RADIUS)
        self.draw_text("CONNECT 4", surface, pygame.font.Font(None, 84), con.DARK_BEIGE, con.WIDTH // 2,
                       con.HEIGHT // 3)
        if self.start_menu:
            self.draw_text("Rounds", surface, pygame.font.Font(None, con.MENU_FONT_SIZE - 5), con.MEDIUM_BEIGE,
                           con.WIDTH // 2,
                           con.HEIGHT // 2 + 50)
            self.draw_text(str(rounds), surface, pygame.font.Font(None, 62), con.MEDIUM_BEIGE, con.WIDTH // 2,
                           con.HEIGHT // 2 + 95)

        mouse_pos = pygame.mouse.get_pos()

        for button in self.buttons:
            text, rect, font = button

            if rect.collidepoint(mouse_pos):
                self.draw_text(text, surface, font, con.DARK_BEIGE, rect.centerx, rect.centery)
            else:
                self.draw_text(text, surface, font, con.MEDIUM_BEIGE, rect.centerx, rect.centery)

        return self.check_interaction(mouse_pos)

    @staticmethod
    def draw_text(text, surface, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        surface.blit(text_surface, text_rect)

    def check_interaction(self, mouse_pos):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    text, rect, _ = button
                    if rect.collidepoint(mouse_pos):
                        return text.lower()

        return None

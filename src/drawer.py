# game_drawer.py

import pygame
from config import *

class Drawer:
    
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

        # Create a pause button
        self.pause_button_rect = pygame.Rect(PAUSE_BUTTON_DIM)

        # Create a restart button
        self.restart_button_rect = pygame.Rect(RESTART_BUTTON_DIM)

        # Load a cursor image
        self.cursor_image = pygame.image.load(CURSOR_IMAGE)
        
        # Hide the default cursor
        pygame.mouse.set_visible(False)

    def draw(self):
        self.screen.fill((SCREEN_FILL_COLOR))  # Fill the screen with white

        self.draw_capture_message()
        self.draw_pause_message()
        self.draw_pause_button()
        self.draw_restart_button()
        self.draw_player_turn()
        self.draw_winning_message()
        self.draw_houses()
        self.draw_cursor()

        pygame.display.flip()

    def draw_capture_message(self):
        if self.game.animator.capturing:
            font = pygame.font.Font(CAPTURE_FONT, CAPTURE_FONT_SIZE)
            capture_message = f"Player {self.game.current_player.number} is capturing..."
            text_surface = font.render(capture_message, True, (CAPTURE_MSG_COLOR))
            self.screen.blit(text_surface, CAPTURE_MSG_DIM)

    def draw_winning_message(self):
        if self.game.game_over:
            winner = self.game.board.check_winner()
            if winner is not None:
                winning_message = f"Game over. Player {winner} win."
                font = pygame.font.Font(CAPTURE_FONT, CAPTURE_FONT_SIZE)
                text_surface = font.render(winning_message, True, RED)
                self.screen.blit(text_surface, CAPTURE_MSG_DIM)
            else:
                print("Draw method: It's a draw.")
                draw_message = f"It's a draw."
                font = pygame.font.Font(CAPTURE_FONT, CAPTURE_FONT_SIZE)
                text_surface = font.render(draw_message, True, RED)
                self.screen.blit(text_surface, CAPTURE_MSG_DIM)

    def draw_pause_message(self):
        if self.game.pause:
            font = pygame.font.Font(PAUSE_FONT, PAUSE_FONT_SIZE)
            text = font.render("Game Paused", True, PAUSE_MSG_COLOR)  # Red text
            self.screen.blit(text, PAUSE_MSG_DIM)  # Adjust position as needed

    def draw_pause_button(self):
        pygame.draw.rect(self.screen, PAUSE_BUTTON_COLOR, self.pause_button_rect)
        font = pygame.font.Font(PAUSE_BUTTON_FONT, PAUSE_BUTTON_FONT_SIZE)
        text = font.render("Pause", True, WHITE)
        self.screen.blit(text, self.pause_button_rect)

    def draw_restart_button(self):
        pygame.draw.rect(self.screen, RESTART_BUTTON_COLOR, self.restart_button_rect)
        font = pygame.font.Font(RESTART_BUTTON_FONT, RESTART_BUTTON_FONT_SIZE)
        text = font.render("Restart", True, WHITE)
        self.screen.blit(text, self.restart_button_rect)

    def draw_player_turn(self):
        font = pygame.font.Font(TURN_MSG_FONT, TURN_MSG_FONT_SIZE)
        text = font.render(f"Player {self.game.current_player.number}'s turn", True, TURN_MSG_COLOR)
        self.screen.blit(text, (0.85 * SCREEN_WIDTH, 10))  # Adjust the position as needed

    def draw_houses(self):
        for i, seeds in enumerate(self.game.board.houses):
            if i in STORE_INDICES:  # Stores
                pygame.draw.circle(self.screen, BLACK, self.game.get_pos_of_house(i), STORE_SIZE)
                font = pygame.font.Font(STORE_SEED_FONT, STORE_SEED_FONT_SIZE)
            else:  # Small houses
                pygame.draw.circle(self.screen, BLACK, self.game.get_pos_of_house(i), HOUSE_SIZE)
                font = pygame.font.Font(SEED_FONT, SEED_FONT_SIZE)

            # Draw the number of seeds in each house
            text = font.render(str(seeds), True, SEED_COLOR)
            self.screen.blit(text, self.game.get_pos_of_house(i))

            # Draw the index of each house
            index_font = pygame.font.Font(HOUSE_INDEX_FONT, HOUSE_INDEX_FONT_SIZE)
            index_text = index_font.render(str(i), True, HOUSE_INDEX_COLOR)  # Red text
            self.screen.blit(index_text, (self.game.get_pos_of_house(i)[0], self.game.get_pos_of_house(i)[1] - 30))  # Draw above the house

    def draw_cursor(self):
        font = pygame.font.Font(CURSOR_FONT, CURSOR_FONT_SIZE)
        cursor_pos = self.game.animator.get_cursor_pos()
        seeds_to_move = self.game.animator.get_seeds_to_move()
        cursor_text = font.render(f"{seeds_to_move}", True, CURSOR_FONT_COLOR)  # Black text
        cursor_width, cursor_height = self.cursor_image.get_size()

        # Flip the cursor if it's player 2's turn
        if self.game.current_player.number == 2:
            cursor_rect = pygame.Rect(cursor_pos[0] - cursor_width // 2, cursor_pos[1] - cursor_height, cursor_width, cursor_height)
            cursor_image_flipped = pygame.transform.flip(self.cursor_image, False, True)
            self.screen.blit(cursor_image_flipped, cursor_rect)
            text_pos = (cursor_rect.center[0], cursor_rect.center[1] - 20)  # Adjust the y-coordinate
        else:
            cursor_rect = self.cursor_image.get_rect(center=(cursor_pos[0], cursor_pos[1] + self.cursor_image.get_height() // 2))
            self.screen.blit(self.cursor_image, cursor_rect)
            text_pos = cursor_rect.center
        
        self.screen.blit(cursor_text, text_pos)

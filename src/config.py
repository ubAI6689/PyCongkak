# config.py

# Pygame Screen Dimensions
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600

# Player details
PLAYER_1 = 1
PLAYER_2 = 2
PLAYER_NUMBERS = [PLAYER_1, PLAYER_2]

# Game houses
PLAYER_1_STORE = 6
PLAYER_2_STORE = 13
STORE_INDICES = [PLAYER_1_STORE, PLAYER_2_STORE]

# Animation
ANIMATION_SPEED = 10
SLEEP_TIME = 0.1
CAPTURE_PHASES = [1, 2]

# Frame per second limit
FPS_LIMIT = 60

# Game board
INIT_SEEDS = 7
BOARD_HOUSES = [INIT_SEEDS] * 6 + [0] + [INIT_SEEDS] * 6 + [0]

# Game colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Seed font and size
SEED_FONT = None
SEED_FONT_SIZE = 36
SEED_COLOR = WHITE
STORE_SEED_FONT = None
STORE_SEED_FONT_SIZE = 60
HOUSE_INDEX_FONT = None
HOUSE_INDEX_FONT_SIZE = 24
HOUSE_INDEX_COLOR = RED

# cursor
CURSOR_IMAGE = "../assets/handcursor.png"
CURSOR_FONT = None
CURSOR_FONT_SIZE = 36
CURSOR_FONT_COLOR = BLACK

# pause message font and size
PAUSE_FONT = None
PAUSE_FONT_SIZE = 50
PAUSE_MSG_COLOR = RED

# capture message font and size
CAPTURE_FONT = None
CAPTURE_FONT_SIZE = 50
CAPTURE_MSG_COLOR = RED

# pause button 
PAUSE_BUTTON_FONT = None
PAUSE_BUTTON_FONT_SIZE = 36
PAUSE_BUTTON_DIM = (10, 70, 100, 50)
PAUSE_BUTTON_COLOR = BLACK

# Restart button
RESTART_BUTTON_FONT = None
RESTART_BUTTON_FONT_SIZE = 36
RESTART_BUTTON_DIM = (10, 10, 100, 50)
RESTART_BUTTON_COLOR = BLACK

# House sizes
STORE_SIZE = 90
HOUSE_SIZE = 45

# Colors and messages
SCREEN_FILL_COLOR = WHITE

# turn message font and size
TURN_MSG_FONT = None
TURN_MSG_FONT_SIZE = 36
TURN_MSG_COLOR = BLACK

# importing the required libraries
import pygame as pg
import time
from pygame.locals import *
import random
# declaring the global variables

# for storing the 'x' or 'o'
# value as character
XO = 'x'

# storing the winner's value at
# any instant of code
winner = None

# to check if the game is a draw
draw = None

# to set width of the game window
width = 400

# to set height of the game window
height = 400

# to set background color of the
# game window
white = (255, 255, 255)

# color of the straightlines on that
# white game board, dividing board
# into 9 parts
line_color = (0, 0, 0)

# setting up a 3 * 3 board in canvas
board = [[None]*3, [None]*3, [None]*3]


# initializing the pygame window
pg.init()

# setting fps manually
fps = 30

# this is used to track time
CLOCK = pg.time.Clock()

# this method is used to build the
# infrastructure of the display
screen = pg.display.set_mode((width, height + 100), 0, 32)

# setting up a nametag for the
# game window
pg.display.set_caption("My Tic Tac Toe")

# loading the images as python object
initiating_window = pg.image.load("cover2.png")
x_img = pg.image.load("X.png")
y_img = pg.image.load("O.png")

# resizing images
initiating_window = pg.transform.scale(
	initiating_window, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(y_img, (80, 80))


def game_initiating_window():

	# displaying over the screen
	screen.blit(initiating_window, (0, 0))

	# updating the display
	pg.display.update()
	time.sleep(3)
	screen.fill(white)

	# drawing vertical lines
	pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
	pg.draw.line(screen, line_color, (width / 3 * 2, 0),
				(width / 3 * 2, height), 7)

	# drawing horizontal lines
	pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
	pg.draw.line(screen, line_color, (0, height / 3 * 2),
				(width, height / 3 * 2), 7)
	draw_status()


def draw_status():

	# getting the global variable draw
	# into action
	global draw

	if winner is None:
		message = XO.upper() + "'s Turn"
	else:
		message = winner.upper() + " won !"
	if draw:
		message = "Game Draw !"

	# setting a font object
	font = pg.font.Font(None, 30)

	# setting the font properties like
	# color and width of the text
	text = font.render(message, 1, (255, 255, 255))

	# copy the rendered message onto the board
	# creating a small block at the bottom of the main display
	screen.fill((0, 0, 0), (0, 400, 500, 100))
	text_rect = text.get_rect(center=(width / 2, 500-50))
	screen.blit(text, text_rect)
	pg.display.update()


def check_win():
	global board, winner, draw

	# checking for winning rows
	for row in range(0, 3):
		if((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
			winner = board[row][0]
			pg.draw.line(screen, (250, 0, 0),
						(0, (row + 1)*height / 3 - height / 6),
						(width, (row + 1)*height / 3 - height / 6),
						4)
			break

	# checking for winning columns
	for col in range(0, 3):
		if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
			winner = board[0][col]
			pg.draw.line(screen, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0),
						((col + 1) * width / 3 - width / 6, height), 4)
			break

	# check for diagonal winners
	if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):

		# game won diagonally left to right
		winner = board[0][0]
		pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)

	if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):

		# game won diagonally right to left
		winner = board[0][2]
		pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)

	if(all([all(row) for row in board]) and winner is None):
		draw = True
	draw_status()


def drawXO(row, col):
	global board, XO

	# for the first row, the image
	# should be pasted at a x coordinate
	# of 30 from the left margin
	if row == 1:
		posx = 30

	# for the second row, the image
	# should be pasted at a x coordinate
	# of 30 from the game line
	if row == 2:

		# margin or width / 3 + 30 from
		# the left margin of the window
		posx = width / 3 + 30

	if row == 3:
		posx = width / 3 * 2 + 30

	if col == 1:
		posy = 30

	if col == 2:
		posy = height / 3 + 30

	if col == 3:
		posy = height / 3 * 2 + 30

	# setting up the required board
	# value to display
	board[row-1][col-1] = XO

	if(XO == 'x'):

		# pasting x_img over the screen
		# at a coordinate position of
		# (pos_y, posx) defined in the
		# above code
		screen.blit(x_img, (posy, posx))
		XO = 'o'

	else:
		screen.blit(o_img, (posy, posx))
		XO = 'x'
	pg.display.update()





def ai_move():
    global board, XO
    
    # Check for winning moves
    for i in range(3):
        # Check rows for 'o'
        if board[i][0] == board[i][1] == 'o' and board[i][2] is None:
            board[i][2] = 'o'
            drawXO(i+1, 3)
            check_win()
            return
        elif board[i][0] == board[i][2] == 'o' and board[i][1] is None:
            board[i][1] = 'o'
            drawXO(i+1, 2)
            check_win()
            return
        elif board[i][1] == board[i][2] == 'o' and board[i][0] is None:
            board[i][0] = 'o'
            drawXO(i+1, 1)
            check_win()
            return
        
        # Check columns for 'o'
        if board[0][i] == board[1][i] == 'o' and board[2][i] is None:
            board[2][i] = 'o'
            drawXO(3, i+1)
            check_win()
            return
        elif board[0][i] == board[2][i] == 'o' and board[1][i] is None:
            board[1][i] = 'o'
            drawXO(2, i+1)
            check_win()
            return
        elif board[1][i] == board[2][i] == 'o' and board[0][i] is None:
            board[0][i] = 'o'
            drawXO(1, i+1)
            check_win()
            return

    # Check diagonals for 'o'
    if board[0][0] == board[1][1] == 'o' and board[2][2] is None:
        board[2][2] = 'o'
        drawXO(3, 3)
        check_win()
        return
    elif board[0][0] == board[2][2] == 'o' and board[1][1] is None:
        board[1][1] = 'o'
        drawXO(2, 2)
        check_win()
        return
    elif board[0][2] == board[1][1] == 'o' and board[2][0] is None:
        board[2][0] = 'o'
        drawXO(3, 1)
        check_win()
        return
    elif board[0][2] == board[2][0] == 'o' and board[1][1] is None:
        board[1][1] = 'o'
        drawXO(2, 2)
        check_win()
        return

    # Block opponent's winning moves
    for i in range(3):
        # Check rows for 'x'
        if board[i][0] == board[i][1] == 'x' and board[i][2] is None:
            board[i][2] = 'o'
            drawXO(i+1, 3)
            check_win()
            return
        elif board[i][0] == board[i][2] == 'x' and board[i][1] is None:
            board[i][1] = 'o'
            drawXO(i+1, 2)
            check_win()
            return
        elif board[i][1] == board[i][2] == 'x' and board[i][0] is None:
            board[i][0] = 'o'
            drawXO(i+1, 1)
            check_win()
            return
        
        # Check columns for 'x'
        if board[0][i] == board[1][i] == 'x' and board[2][i] is None:
            board[2][i] = 'o'
            drawXO(3, i+1)
            check_win()
            return
        elif board[0][i] == board[2][i] == 'x' and board[1][i] is None:
            board[1][i] = 'o'
            drawXO(2, i+1)
            check_win()
            return
        elif board[1][i] == board[2][i] == 'x' and board[0][i] is None:
            board[0][i] = 'o'
            drawXO(1, i+1)
            check_win()
            return

    # Check diagonals for 'x'
    if board[0][0] == board[1][1] == 'x' and board[2][2] is None:
        board[2][2] = 'o'
        drawXO(3, 3)
        check_win()
        return
    elif board[0][0] == board[2][2] == 'x' and board[1][1] is None:
        board[1][1] = 'o'
        drawXO(2, 2)
        check_win()
        return
    elif board[0][2] == board[1][1] == 'x' and board[2][0] is None:
        board[2][0] = 'o'
        drawXO(3, 1)
        check_win()
        return
    elif board[0][2] == board[2][0] == 'x' and board[1][1] is None:
        board[1][1] = 'o'
        drawXO(2, 2)
        check_win()
        return

    # If no winning move is available, make a random move
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    if board[row][col] is None:
        board[row][col] = 'o'  # AI plays as 'o'
        drawXO(row+1, col+1)  # Adjust for 1-based counting
        check_win()
        return
			

def ai_vs_ai():
    time.sleep(0.5)
    global board, XO
    XO = 'x'
    while True:
        ai_move()
        time.sleep(0.5)
        check_win()
        if winner or draw:
            break
        ai_move()
        check_win()
        if winner or draw:
            break
        time.sleep(0.5)
    if draw:
        print("The game was a draw.")
    else:
        if XO == 'x':
            print("AI 1 (X) won.")
        else:
            print("AI 2 (O) won.")

def reset_game():
	global board, winner, XO, draw
	time.sleep(0.5)
	XO = 'x'
	draw = False
	game_initiating_window()
	winner = None
	board = [[None]*3, [None]*3, [None]*3]



game_initiating_window()
ai_vs_ai()
reset_game()
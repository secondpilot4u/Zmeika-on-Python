import curses
import random

screen = curses.initscr()
curses.curs_set(0)
screen_height, screen_width = screen.getmaxyx()
window = curses.newwin(screen_height, screen_width, 0, 0)
window.keypad(1)
window.timeout(100)

snake = [(screen_height//2, screen_width//2)]
food = (random.randint(1, screen_height-2), random.randint(1, screen_width-2))

key = curses.KEY_RIGHT

while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    new_head = (snake[0][0] + (key == curses.KEY_DOWN) - (key == curses.KEY_UP),
                snake[0][1] + (key == curses.KEY_RIGHT) - (key == curses.KEY_LEFT))

    if (new_head[0] < 1 or new_head[0] >= screen_height-1 or
        new_head[1] < 1 or new_head[1] >= screen_width-1 or
        new_head in snake):
        break

    snake.insert(0, new_head)

    if new_head == food:
        food = (random.randint(1, screen_height-2), random.randint(1, screen_width-2))
    else:
        snake.pop()

    window.clear()
    window.border(0)
    for segment in snake:
        window.addch(segment[0], segment[1], '#')
    window.addch(food[0], food[1], '@')
    window.refresh()

curses.endwin()
import curses
import math

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.curs_set(0)

    stdscr.border()
    stdscr.bkgd(' ', curses.color_pair(1))

    height, width = stdscr.getmaxyx()


    # Nightlight Message
    stdscr.addstr(height // 2, width // 2 - 5, "Nightlight v0.0.1", curses.A_BOLD)


    # Customization message
    percentage = (3 / width) * 100
    customize_width = math.ceil(round(percentage, 2))
    stdscr.addstr(height-3, customize_width, f"<F2> Customize System", curses.A_BOLD)



    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)

import curses
import os

def print_menu(window, items, selected_row_idx):
    window.erase()
    window.border()
    height, width = window.getmaxyx()
    for idx, item in enumerate(items):
        x = 4
#        x = width // 7 - len(item) // 2
        y = height // 6 - len(items) // 2 + idx
        if idx == selected_row_idx:
            window.attron(curses.color_pair(1))
            window.addstr(y, x, item)
            window.attroff(curses.color_pair(1))
        else:
            window.addstr(y, x, item)
    window.refresh()

def run_menu(window, title, items):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    selected_row_idx = 0
    print_menu(window, items, selected_row_idx)
    while True:
        key = window.getch()
        if key == curses.KEY_UP and selected_row_idx > 0:
            selected_row_idx -= 1
        elif key == curses.KEY_DOWN and selected_row_idx < len(items) - 1:
            selected_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return selected_row_idx
        print_menu(window, items, selected_row_idx)

def main(window):
    main_menu_items = ["Configure Management Network", "Configure System", "Reboot Host", "Shutdown Host", "Exit to Shell"]
    
    # Customization message
    while True:
        curses.curs_set(0)
        selected_main_idx = run_menu(window, "Main Menu", main_menu_items)

        if selected_main_idx == 0:
            submenu1_items = ["IPv4 Configuration", "Test Network", "Back"]
            while True:
                 selected_sub1_idx = run_menu(window, "Configure Management Network", submenu1_items)
                 if selected_sub1_idx == len(submenu1_items) - 1:
                    break
                 # Handle submenu 1 options here
                 window.addstr(0, 0, f"Submenu 1 Option {submenu1_items[selected_sub1_idx]} selected")
                 window.refresh()
                 window.getch()
        elif selected_main_idx == 1:
            submenu2_items = ["Choice X", "Choice Y", "Back"]
            while True:
                selected_sub2_idx = run_menu(window, "Submenu 2", submenu2_items)
                if selected_sub2_idx == len(submenu2_items) - 1:
                    break
                # Handle submenu 2 options here
                window.addstr(0, 0, f"Submenu 2 Option {submenu2_items[selected_sub2_idx]} selected")
                window.refresh()
                window.getch()
        elif selected_main_idx == 2:
            # Add prompt to check if you really want to reboot
            os.system("reboot")
        else:
             break

curses.wrapper(main)

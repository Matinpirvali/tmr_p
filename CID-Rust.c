#include <ncurses.h>
#include <stdlib.h>

#define BUFFER_SIZE 1024

int main() {
    char buffer[BUFFER_SIZE];
    int row, col;
    int ch;

    initscr();
    raw();
    keypad(stdscr, TRUE);
    noecho();

    getmaxyx(stdscr, row, col);

    WINDOW *win = newwin(row - 1, col, 0, 0);

    while (1) {
        int i;
        for (i = 0; i < BUFFER_SIZE; i++) {
            buffer[i] = '\0';
        }

        mvwgetnstr(win, 0, 0, buffer, BUFFER_SIZE - 1);

        if (buffer[0] == ':') {
            if (strcmp(buffer, ":q") == 0) {
                break;
            } else if (strcmp(buffer, ":clear") == 0) {
                wclear(win);
                wrefresh(win);
                continue;
            }
        }

        wprintw(win, "%s\n", buffer);
        wrefresh(win);
    }

    delwin(win);
    endwin();
    refresh();

    return 0;
}

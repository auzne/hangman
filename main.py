# made by https://github.com/auzne
import curses
import random
import webbrowser

screen = curses.initscr()
screen.keypad(1)
curses.curs_set(0)
curses.noecho()
dims = screen.getmaxyx()
y, q = 0, -1
while q != 1:
    if y == 0:
        screen.addstr(int(dims[0]/2)-2, int(dims[1]/2)-6, "Play", curses.A_REVERSE)
        screen.addstr(int(dims[0]/2)-1, int(dims[1]/2)-6, "Help")
        screen.addstr(int(dims[0]/2), int(dims[1]/2)-6, "Quit")
    elif y == 1:
        screen.addstr(int(dims[0]/2)-2, int(dims[1]/2)-6, "Play")
        screen.addstr(int(dims[0]/2)-1, int(dims[1]/2)-6, "Help", curses.A_REVERSE)
        screen.addstr(int(dims[0]/2), int(dims[1]/2)-6, "Quit")
    elif y == 2:
        screen.addstr(int(dims[0]/2)-2, int(dims[1]/2)-6, "Play")
        screen.addstr(int(dims[0]/2)-1, int(dims[1]/2)-6, "Help")
        screen.addstr(int(dims[0]/2), int(dims[1]/2)-6, "Quit", curses.A_REVERSE)
    screen.addstr(int(dims[0]/2)-6, int(dims[1]/2)-7, "Hangman", curses.A_UNDERLINE)
    screen.refresh()

    q = screen.getch()
    if q == curses.KEY_UP:
        if y == 0:
            y = 2
        elif y == 1:
            y = 0
        elif y == 2:
            y = 1
    elif q == curses.KEY_DOWN:
        if y == 0:
            y = 1
        elif y == 1:
            y = 2
        elif y == 2:
            y = 0
    elif q == curses.KEY_RIGHT:
        if y == 0:
            screen.clear()
            break
        elif y == 1:
            webbrowser.open('https://www.wikihow.com/Play-Hangman', new=0, autoraise=True)
        elif y == 2:
            screen.clear()
            quit()

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split() #from https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

def template(die):
    screen.addstr(1,1,'  +---+')
    screen.addstr(2,1,'  |   |')
    screen.addstr(3,1,'      |')
    screen.addstr(4,1,'      |')
    screen.addstr(5,1,'      |')
    screen.addstr(6,1,'      |')
    screen.addstr(7,1,'=========')
    if die == 1:
        screen.addstr(3,1,'  O   |')
    elif die == 2:
        screen.addstr(3,1,'  O   |')
        screen.addstr(4,1,'  |   |')
    elif die == 3:
        screen.addstr(3,1,'  O   |')
        screen.addstr(4,1,' /|   |')
    elif die == 4:
        screen.addstr(3,1,'  O   |')
        screen.addstr(4,1,' /|\  |')
    elif die == 5:
        screen.addstr(3,1,'  O   |')
        screen.addstr(4,1,' /|\  |')
        screen.addstr(5,1,' /    |')
    elif die == 6:
        screen.addstr(3,1,'  O   |')
        screen.addstr(4,1,' /|\  |')
        screen.addstr(5,1,' / \  |')
    screen.refresh()

att, disc, miss, win = 0, [], [], False
word = random.choice(words)

def winner():
    global disc, word
    tt = 0
    for i in word:
        if i in disc:
            tt += 1
    if tt == len(word):
        return True
    else:
        return False

while att != 6:
    start = 15
    template(att)
    screen.addstr(1, 15, 'Hangman - Only animals', curses.A_UNDERLINE)
    for i in word:
        if i in disc:
            screen.addstr(3, start, i)
        else:
            screen.addstr(3, start, ' ', curses.A_UNDERLINE)
        start += 2
    screen.addstr(5, 15, 'Misses Words', curses.A_UNDERLINE)
    start, lg = 15, 7
    for i in miss:
        if start > 50:
            lg += 1
            start = 15
        screen.addstr(lg, start, i, curses.A_UNDERLINE)
        start += 2
    screen.refresh()
    q = screen.getch()
    if chr(q) in word:
        if chr(q) not in disc:
            disc.append(chr(q))
            if winner():
                win = True
                break
    else:
        if chr(q) not in miss:
            miss.append(chr(q))
            att += 1
template(att)
screen.refresh()
if win:
    screen.addstr(9, 1, 'You Win, the word was: ' + word)
else:
    screen.addstr(9, 1, 'You Lose, the word was: ' + word)
screen.addstr(10, 1, '[Q]uit')
while True:
    q = screen.getch()
    if q == ord('q'):
        quit()
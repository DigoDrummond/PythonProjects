import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()#clear terminal
    stdscr.addstr("Welcome to the Speed Typing Test!",curses.color_pair(1))
    stdscr.addstr("\nPress any key to begin!",curses.color_pair(1))
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr,target_text,current_text,wpm=0):
    stdscr.addstr(target_text)
    stdscr.addstr(1, 0, f"WPM: {wpm}")
         
    for i, char in enumerate(current_text):
        correct_char = target_text[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
            
        stdscr.addstr(0, i, char, color)
    
def load_text():
    with open("C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\PythonProjects\\WPMTypingTest\\text.txt","r",encoding="utf-8") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)#do not delay waiting for the user to hit a key
   
    
    while(True):
        time_elapsed = max(time.time() - start_time,1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)
        
        stdscr.clear()#clear terminal
        display_text(stdscr,target_text,current_text,wpm)
        stdscr.refresh()
        
        #combine caracters from the list in a string
        if "".join(current_text) == target_text:
          stdscr.nodelay(False)
          break
        
        try:
            key = stdscr.getkey()
        except:
            continue#brings back to the top of the while loop
        
        #escape Esc
        if ord(key) == 27:
            break
        
        if key in ("KEY_BACKSPACE",'\b',"\x7f"):
            if len(current_text) > 0:
                current_text.pop()#remove the last element from the list
        elif len(current_text) < len(target_text):
            current_text.append(key)
        
        

def main(stdscr):
    #color variables
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
        key = stdscr.getkey()
        if ord(key) == 27:
            break
    
wrapper(main)


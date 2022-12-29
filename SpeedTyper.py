import random
import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
import sv_ttk
import math
from time import sleep

with open("3000mostcommon.txt") as file:
    words = file.readlines()
    words = [word.strip().lower() for word in words]
    
    
random_words = random.sample(words, 500)
#print(random_words)

DARKEST = "#439A97"
LIGHT = "#62B6B7"
LIGHTER = "#97DECE"
OFFWHITE = "#CBEDD5"
FONT = ("Roboto", 20)
wordindex = 0
CORRECT = 0 
WRONG = 0
CORRECTWORDS = []
MISTYPEDWORDS = []


#Requirements

#1 Display a random selection of 10-15 words 
# on the screen in a box
#DONE

#2 Create a writing field
#DONE

#Space should check if the correct is correct, if it is 
#move to the next word and highlight the word green
#If it's not highlight it red
#Found a way to check now let's see how to highlight individual words in the wordblock

#3 Create a 1 minute timer activated upon clicking a 
#start button or starting to type

#4 While the timer is running count how many words were 
#correctly typed

#They're short for Characters Per Minute, and Words Per Minute. 
# The "raw CPM" is the actual number of characters you type per minute, 
# including all the mistakes. "Corrected" scores count only correctly typed words. 
# "WPM" is just the corrected CPM divided by 5.

#Done-also added wpm and cpm

#5 Show the final number after the clock hits 0,add a reset button
#to start typing again

#6 Make the words scroll down and show new ones as the words
#Are being written
#Kind of done but sloppy 

#7 Show which words were mistaken at the end together with the wpm
#DONE

#8 Create separate file for high scores and display them 

#9 Add dificulties with longer and less common words


window = tk.Tk()
window.tk_setPalette('SystemButtonFace')
window.title("SpeedTyper")

window.geometry("1000x724")

window.resizable(True, True)

sv_ttk.set_theme("dark")

 
        
def start_timer():
    global CORRECTWORDS,MISTYPEDWORDS,CORRECT,WRONG,random_words,wordindex
    CORRECTWORDS = []
    MISTYPEDWORDS = []
    CORRECT = 0
    WRONG = 0
    wordindex = 0
    random_words = random.sample(words, 500)
    the_word.config(text=random_words[wordindex:wordindex+3])
    wordblock.config(text=random_words[wordindex:wordindex+20])
    
    typeline.focus()
    
    minute =  60
    count_down(minute)
    
    
def start_timer_event(event):
    global CORRECTWORDS,MISTYPEDWORDS,CORRECT,WRONG,random_words,wordindex
    CORRECTWORDS = []
    MISTYPEDWORDS = []
    CORRECT = 0
    WRONG = 0
    wordindex = 0
    random_words = random.sample(words, 500)
    the_word.config(text=random_words[wordindex:wordindex+3])
    wordblock.config(text=random_words[wordindex:wordindex+20])
    
    typeline.focus()

    minute =  60
    count_down(minute)
    
    
def count_down(count):
    global wordindex,the_word

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        raw_cpm = [len(word) for word in random_words[:wordindex]]
        correct_cpm = [len(word) for word in CORRECTWORDS]
        #Just divide by the amount of seconds then multiply by 60 to get cpm 
        #Or dont multiply for per second counts
        with open("HighScores.txt", 'a') as file:
            file.write(f"\n{(int(sum(raw_cpm))):.2f},{(int(sum(correct_cpm))):.2f},{(int(sum(correct_cpm))/5):.2f}")
        print(f"RAW CPM:{(int(sum(raw_cpm))):.2f}")
        print(f"CORRECTED CPM:{(int(sum(correct_cpm))):.2f}")
        print(f"WPM:{(int(sum(correct_cpm))/5):.2f}")
        the_word.config(text=f"Correctly typed:{CORRECT}:Mistypes:{WRONG}")
        wordblock.config(text=f"RAW CPM:{(int(sum(raw_cpm))):.2f}\nCORRECTED CPM:{(int(sum(correct_cpm))):.2f}\nWPM:{(int(sum(correct_cpm))/5):.2f}")
        reset_timer()
        
        
# The "raw CPM" is the actual number of characters you type per minute, 
# including all the mistakes. "Corrected" scores count only correctly typed words. 
# "WPM" is just the corrected CPM divided by 5.
        
        
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    #Need to make this update the above list aswell
    #Did it in the start function
    #Need to reset the word label on timer start too
        


canvas = tk.Canvas(width=50, height=50, bg= LIGHTER, highlightthickness=0)
timer_text = canvas.create_text(25, 25, text="00:00", fill="black", font=(FONT, 15))
canvas.pack(side=tk.TOP, anchor="w")

title_label = tk.Label(text="SpeedTyper", fg=LIGHTER, font=(FONT, 50))
title_label.pack(side=tk.TOP,anchor='n', padx=15)


Frame = tk.Frame(window, background="#1b1b1b", height=20,pady=20)
Frame.pack(side=tk.TOP, fill=tk.X)

the_word = tk.Label(Frame, text="Welcome to the SpeedTyper,press Enter or Click the start button to begin", justify=tk.CENTER, foreground=OFFWHITE,
                  font=("Roboto", 25), borderwidth=5, background=DARKEST, activebackground="#1b1b1b",fg="black")
the_word.config(wraplength=500)
the_word.pack(side=tk.TOP,pady=10)

wordblock = tk.Label(Frame, text="The current and the next 2 words will appear above.", justify=tk.CENTER, foreground=OFFWHITE,
                  font=("Roboto", 25), borderwidth=5, background=DARKEST, activebackground="#1b1b1b",fg="black")
wordblock.config(wraplength=500)
wordblock.pack(side=tk.TOP,pady=10)



#if canvas.itemcget(timer_text,'text') == "00:00":
start_button = ttk.Button(text="Start", command=start_timer)
start_button.pack(side=tk.TOP, anchor="n")

start_button = ttk.Button(text="Reset", command=reset_timer)
start_button.pack(side=tk.RIGHT, anchor="n")








typeline = tk.Entry(Frame,width=30,foreground=OFFWHITE, borderwidth=0, 
                    background="black",font=FONT)
typeline.pack(side=tk.BOTTOM,padx=10, pady=10)

def check_word(event):
    global random_words,wordindex,CORRECT,WRONG,the_word,wordblock,MISTYPEDWORDS,CORRECTWORDS
    try:
        # Get the word typed in the Entry widget
        typed_word = typeline.get().strip()
        # Check if the word is correct
        current_word = random_words[wordindex]
        if typed_word == current_word:
            CORRECT +=1
            wordindex +=1
            CORRECTWORDS.append(typed_word)
            #entry_text.set(typeline.get().rstrip())
            # Delete the remaining text in the Entry widget
            typeline.delete(0, tk.END)
        elif typed_word != current_word:
            wordindex +=1
            WRONG +=1
            MISTYPEDWORDS.append(typed_word)
            # If the word is incorrect, display a message
            typeline.delete(0, tk.END)
        the_word.config(text=random_words[wordindex:wordindex+3])
        if wordindex % 10 == 0:
            wordblock.config(text=random_words[wordindex:wordindex+20])
    except IndexError:
        the_word.config(text=f"Correctly typed:{CORRECT}:Mistypes:{WRONG}", font=(FONT, 15))
        
        
        

        
        
typeline.bind("<space>",check_word)
window.bind('<Return>', start_timer_event)


window.mainloop()


#Next steps
#Add timer which will start counting for the words
#1 minute then post the cpm,wpm and correctly typed and wrongly typed words
#DONE


#To do-
#Make the experience smoother
#Add a reset button to reset the words,correct and wrongs lists and restart timer from 0
#Maybe put all of this inside the start timer function
#Start button resets the counts and lists and will only give you wpm for the minute you typed in

#Need to fix multiple presses of the button


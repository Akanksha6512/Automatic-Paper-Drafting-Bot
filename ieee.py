import time
import pyautogui
import pyperclip
import re
import speech_recognition as sr

def abstract():
    #print "\nAbstract selected\n"
    write_module("Abstract")
    print "Abstract written successfully"
    return


def add_module():
    print "add"
    new_module = raw_input("Enter module to be created: ")
    with open("ieee.txt",'a') as fo:
        fo.write(new_module)
        fo.write("\n")
    return

def edit_module():
    
    with open("ieee.txt",'r') as fo:
        print fo.read()
    print "please read a module "
    module_choice = main_type_module()
    print "Do you want to write or append "
    write_choice = main_type_module()
    if write_choice.lower() == "write" or write_choice.lower() == "right":
        print "Write "+module_choice+" selected"
        write_module(module_choice)
    elif write_choice.lower() == "append":
        print "Append "+module_choice+"selected"
        append_module(module_choice)  
    
    
    return

def type_module():
    print "Listening...."
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    temp = r.recognize_google(audio)
    pyautogui.typewrite(temp)
    return temp

def main_type_module():
    print "Listening...."
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    #pyautogui.typewrite(r.recognize_google(audio))
    x = r.recognize_google(audio)
    print "Choice heard: "+x
    return x

def write_module(module_name):
    print "Open the document you wish to edit"
    time.sleep(5)
    print "Read done when done "
    choice = main_type_module()

    while choice.lower() != "done":
        time.sleep(1)

    #time.sleep(5)
    #print "\nPreparing to write....\n"
    #pyautogui.hotkey('alt','tab')
    
    pyautogui.hotkey('ctrl','home')
    
    pyautogui.hotkey('ctrl','f')
    pyautogui.typewrite(module_name)
    pyautogui.press('esc')
    pyautogui.press(['right','right','d',' '])    
    
    inp = ""
    inp1 = ""

    while True:
        pyautogui.hotkey('shift','end')       
        pyautogui.hotkey('ctrl','c')
        time.sleep(1)
        inp = pyperclip.paste()
        time.sleep(1)
        if inp1 == inp:
            break
        pyautogui.press('del')
        inp1 = inp

    

    pyautogui.press(['backspace','backspace'])
        
    x = type_module()
    print "Input Speech: "
    print x
    time.sleep(1)
    pyautogui.hotkey('alt','tab')

        
    
    return
def append_module(module_name):
    print "Open the document you wish to edit"
    time.sleep(10)
    print "Read done when done "
    
    choice = main_type_module()

    while choice.lower() != "done":
        time.sleep(1)

    #time.sleep(5)
    print "Preparing to append...."
    pyautogui.hotkey('alt','tab')
    
    pyautogui.hotkey('ctrl','f')
    pyautogui.typewrite(module_name)
    pyautogui.press('esc')
    pyautogui.press(['right','right','d',' '])    
    
    inp = ""
    inp1 = ""


    pyautogui.press(['backspace','backspace'])

    x = type_module()
    
    time.sleep(5)

    

    

    pyautogui.press(['enter','up'])

    print "Input Speech: "
    print x

    print "Number of paragraphs to be skipped: "

    pyautogui.hotkey('alt','tab')

    i = int(main_type_module())

    pyautogui.hotkey('alt','tab')

    while i!=0:
        pyautogui.hotkey('shift','alt','down')
        i=i-1
    print "Data appended successfully"
        

    
    return
    




if __name__ == "__main__":

    pyautogui.hotkey('win','right')
    while True:
        print "1. Abstract\n2. Module\n3. Exit\nPlease read the option name you wish to choose"
        #main_module = raw_input("\nType the choice name: ")
        main_module = main_type_module()
        if main_module.lower() == "abstract":
            #print "\nSelecting abstract..."
            abstract()
        elif main_module.lower() == "module":
            print "Selecting module..."
            print "1. Edit\nRead the choice name: "
            sub_module = main_type_module()
            if sub_module.lower() == "add":
                add_module()
            elif sub_module.lower() == "edit":
                edit_module()
        elif main_module.lower() == "exit":
            print "\nProgram ended\n\nThank you!!!\n"
            break
        else:
            print "\nPlease read a valid choice\n"
            
        
    

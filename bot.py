import pyautogui, time

GAME_REGION = ()

def count_down():
    timer = 5
    for t in range(timer,0,-1):
        print('Starting in ' + str(t) + ' seconds, click the search icon now')
        time.sleep(1)

def setupCoordinates():
    global GAME_REGION
    ''' find search (top left) '''
    search_location = pyautogui.locateOnScreen('search_box_arrow.png')

    ''' find smiley (bottom right) '''
    smiley_location = pyautogui.locateOnScreen('smiley.png')

    ''' set region (left, top, width, and height '''
    GAME_REGION=(search_location[0],search_location[1]+search_location[3],smiley_location[0],smiley_location[1])
    print('Found region: ' + str(GAME_REGION))


def typeNow():
    print('Clicked "typing...", sending keystrokes now')
    pyautogui.typewrite('aaaaa', interval=0.25)
    print('Typing stopped, cleaning up')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')
    print('Restarting monitor')    

            

def startMonitor():
    while True:
        pos_white = pyautogui.locateOnScreen('typing_white.png', region=GAME_REGION)
        if pos_white is not None:
            print('White typing found')
            pyautogui.click(pos_white)
            typeNow()
        pos_grey = pyautogui.locateOnScreen('typing_grey.png', region=GAME_REGION)
        if pos_grey is not None:
            print('Grey typing found')
            pyautogui.click(pos_grey)
            typeNow()

def main():
    count_down()
    setupCoordinates()
    print('Starting scanning, no exit now')
    startMonitor()

if __name__ == '__main__':
    main()
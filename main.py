#!/usr/bin/env python
import webbrowser
import pyautogui as py
import time
import cv2
import numpy as np
import pyperclip
import csv

def csvFileReader(csv_file):
    """This function reads the csv_file and return the output as a dictionary"""
    result = []
    with open(csv_file, encoding='UTF-8') as software:
        reader = csv.DictReader(software)
        for row in reader:
            result.append(row)
    return result

def getMatchVer2(sub_image, name):
    """This function uses the address of the subimage in the OS. It will return the location of the matching process"""
    while True:
        try:
                # Take a screenshot and save it as 'template.png'
                myScreenshot = py.screenshot()
                myScreenshot.save('screenshot.png')

                # Load the larger image and the sub-image (template)
                # image = cv2.imread('screenshot.png')
                image = cv2.imread('screenshot.png')
                template = cv2.imread(sub_image)

                # Perform template matching
                result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

                # Set a threshold for matching result (adjust this as needed)
                threshold = 0.5

                # Locate where the match exceeds the threshold
                loc = np.where(result >= threshold)

                # Code for printing the result
                w, h = template.shape[:-1]
                for pt in zip(*loc[::-1]):  # Switch columns and rows
                    cv2.rectangle(image, pt, (pt[0] + h, pt[1] + w), (0, 0, 255), 2)

                if len(loc[0]) > 0:
                    print("Matched found: " + name);
                    # Save result picture for debugging
                    cv2.imwrite('result/' + name + '.png', image)
                    return

        except Exception as e:
            print(f"An error occurred: {e}")

def autoTextingVer2(message):
    """This funcion will move the cursor to the pos_x and pos_y, then begin the auto texting process (Only with FB)"""
    # Dealing with the unicode message
    pyperclip.copy(message)
    py.hotkey('ctrl', 'v')
    time.sleep(2)
    # Send the message
    # py.press("enter")
    time.sleep(1)

def main():
    # Input your message here
    message = "CN 7h sân 7?"
    friends_dict = csvFileReader("friends.csv")
    webbrowser.open("facebook.com/khoango1810/")
    time.sleep(1)
    for friend in friends_dict:
      webbrowser.open("facebook.com/messages/t/" + friend["id"])
      getMatchVer2("sub_image.png", friend["name"])
      time.sleep(2)
      autoTextingVer2(message)
      time.sleep(2)
      py.hotkey('ctrl', 'w')
      time.sleep(0.5)
    py.hotkey('alt', 'f4')
    print('Done')

main()
'''
            DATA SCIENCE & AI INTERNSHIP
            DEVSTACK STUDENT INTERNSHIP PROGRAM
            NAME:- Anurag Ranjan
            TAST-1 ---> Make a color detection system with the help of Panda and Open CV based on the provided dataset.
'''

import cv2
import pandas as pd

img_path = r'colors.jpg'
img = cv2.imread(img_path)

# declaring global variables (are used later on)
clicked = False # initially should set as False
r = g = b = x_pos = y_pos = 0 # declaring the initial positions as 0

# Reading csv file
index = ["color", "color_name", "hex", "R", "G", "B"] # setting up index for colored names
csv = pd.read_csv('colors.csv', names=index, header=None) # reading the csv file with the help of pandas

# function to calculate minimum distance from all colors and get the most matching color
def get_color_name(R, G, B):
    minimum = 10000 # setting up the minimum threshold value
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# function to get x,y coordinates of cursor where it has been clicked
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
    cv2.imshow("image", img)
    if clicked:
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1) # calculating the image start point, endpoint, color, thickness

        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b) # Creating text string to display (Color name and RGB values)

        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA) # deciding the fontScale,color,thickness,lineType

        # deciding the text color should be contrast (white for all dark colors and black for all light colors)
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        clicked = False

    # Break the loop when user hits 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break # comes out of the program

cv2.destroyAllWindows()

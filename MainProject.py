from fingers import point
from fingers import finger
import cv2
import mediapipe as mp
import time

from SignLanguageLookup import *

# captures video from webcam
# NOTE: input value can vary between -1, 0, 1, 2 (differs per device, 0 or 1 is common)
# WARNING: VideoCapture does not work if another application is using camera (ie. video calling)
cap = cv2.VideoCapture(0)

# from pre-trained Mediapipe to draw hand landmarks and connections
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# used to calculate FPS
pTime = 0  # previous time
cTime = 0  # current time
pointNum = [0] * 21  # point number list

# finger objects
thumb = finger()
index = finger()
middle = finger()
ring = finger()
pinky = finger()


def checkSign():
    # Loop through 4
    for num in range(5):
        if num < 1:

            # Checking for letter c
            isC = True
            isU = True

            num = 1
            if((abs(thumb.point[num].x-pinky.point[num].x) < 0.05) and (abs(thumb.point[num].y-pinky.point[num].y) < 0.3)
               and (abs(thumb.point[num].y-pinky.point[num].y) > 0.2)):
                print("This is a c")

            # Checking for U
            elif((abs(index.point[num].x-middle.point[num].x) < 0.07) and abs(index.point[num].x-middle.point[num].x) > 0.001
                    and (abs(index.point[num].y-middle.point[num].y) < 0.07)
                    and (abs(index.point[num].y-middle.point[num].y) > 0.005) and abs(index.point[num].z-middle.point[num].z)
                    < 0.03 and abs(index.point[3].y-ring.point[3].y) > 0.1):
                print("This is a U")

            # Checking for V
            # if((abs(thumb.point[num].x-pinky.point[num].x) < 0.05) and (abs(thumb.point[num].y-pinky.point[num].y) < 0.3)
            #    and (abs(thumb.point[num].y-pinky.point[num].y) > 0.2)):
            #     print("This is a V")

    # Detects


def printFingerValues(finger):
    for i in range(len(finger.point)):
        print("Point", i, ": x", finger.point[i].x, ", y",
              finger.point[i].y, ", z", finger.point[i].z)


counter = 0

while True:
    # reads image from webcam
    success, img = cap.read()

    # converts default image value to RGB value
    # NOTE: when printing back to the screen, use default value (img) NOT imgRGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # use Mediapipe to process converted RGB value
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # creates list of all landmarks for easier indexing
            # list will have 21 values -> lm_list[0] will be first landmark
            lm_list = []

            # id corresponds to landmark #
            #   -> 21 landmarks in total (4 on non-thumb fingers, rest on thumb and palm)
            # lm corresponds to landmark value
            #   -> each lm has x coordinate and y coordinate
            #   -> default values are in ratio (value between 0 and 1)
            #   -> to convert to pixel value, multiple by width and height of screen
            #   IMPORTANT: probably gonna need to hardcode landmark distance values to represent sign language
            for id, lm in enumerate(handLms.landmark):
                # get height, width, depth or color(?)
                h, w, c = img.shape
                # convert to x and y pixel values
                cx, cy = int(lm.x*w), int(lm.y*h)
                counter += 1
                # points on the thumb
                if (id > 0 and id < 5):
                    thumb.point[id] = point(id, lm.x, lm.y, lm.z)
                    print("Finger: Thumb: ", "point: ", thumb.point[id].id, "x:",
                          thumb.point[id].x, "y:", thumb.point[id].y, "z: ", thumb.point[id].z,)

                # points on index
                if (id > 4 and id < 9):
                    fingerNum = id-4
                    index.point[fingerNum] = point(fingerNum, lm.x, lm.y, lm.z)
                    print("Finger: index: ", "point: ", index.point[fingerNum].id, "x:",
                          index.point[fingerNum].x, "y:", index.point[fingerNum].y, "z: ", index.point[fingerNum].z,)

                # points on middle
                if (id > 8 and id < 13):
                    fingerNum = id-8
                    middle.point[fingerNum] = point(
                        fingerNum, lm.x, lm.y, lm.z)
                    print("Finger: middle: ", "point: ", middle.point[fingerNum].id, "x:",
                          middle.point[fingerNum].x, "y:", middle.point[fingerNum].y, "z: ", middle.point[fingerNum].z,)

                # points on fourth finger
                if (id > 12 and id < 17):
                    fingerNum = id-12
                    ring.point[fingerNum] = point(
                        fingerNum, lm.x, lm.y, lm.z)
                    print("Finger: ring: ", "point: ", ring.point[fingerNum].id, "x:",
                          ring.point[fingerNum].x, "y:", ring.point[fingerNum].y, "z: ", ring.point[fingerNum].z,)

                # points on fifth finger
                if (id > 16 and id < 21):
                    fingerNum = id-16
                    pinky.point[fingerNum] = point(
                        fingerNum, lm.x, lm.y, lm.z)
                    print("Finger: pinky: ", "point: ", pinky.point[fingerNum].id, "x:",
                          pinky.point[fingerNum].x, "y:", pinky.point[fingerNum].y, "z: ", pinky.point[fingerNum].z,)

                if (counter > 30):
                    checkSign()

                # pointNum[id] = id

                # points on pinky

                # print("pointNum", pointNum[id], "ID", id, ":", lm.z)

                # code to draw bigger circle on specific landmark
                # if id == 4:
                #    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

                lm_list.append([id, cx, cy])

            OUTPUT_LIST = createOutputList(lm_list)
            # print(OUTPUT_LIST)
            if tuple(OUTPUT_LIST) in CONVERSION_LOOKUP:
                cv2.putText(img, CONVERSION_LOOKUP[tuple(OUTPUT_LIST)], (550, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0),
                            3)

            # draw hand landmarks and connections
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # print FPS on screen (not console)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

    # print current image captured from webcam
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    # press Q to quit or "stop" button
    if key == ord("q"):
        break


test()
# cleanup
cap.release()
cv2.destroyAllWindows()


tip_ids = [4, 8, 12, 16, 20]
finger_lms = [[5, 6, 7, 8], [9, 10, 11, 12],
              [13, 14, 15, 16], [17, 18, 19, 20]]

# FOR FOUR FINGERS: number of pixels allowed to be considered same "level"
VERTICAL_ERROR_MARGIN = 10
# FOR THUMB - less horizontal space than vertical so needs to have smaller margin
HORIZONTAL_ERROR_MARGIN = 5


def createOutputList(lm_list):
    a = analyseThumb(lm_list)
    b = analyseIndexFinger(lm_list)
    c = analyseMiddleFinger(lm_list)
    d = analyseRingFinger(lm_list)
    e = analysePinkyFinger(lm_list)
    return [a, b, c, d, e]

# check position of tip of thumb relative to other base finger LMs (ie. 5, 9, 13)


def analyseThumb(lm_list):
    THUMB_TIP = lm_list[4]
    INDEX_BASE = lm_list[5]
    MIDDLE_BASE = lm_list[9]
    RING_BASE = lm_list[13]

    if THUMB_TIP[1] > RING_BASE[1] or abs(THUMB_TIP[1] - RING_BASE[1]) < HORIZONTAL_ERROR_MARGIN:
        return 0
    elif THUMB_TIP[1] > MIDDLE_BASE[1] or abs(THUMB_TIP[1] - MIDDLE_BASE[1]) < HORIZONTAL_ERROR_MARGIN:
        return 1
    elif THUMB_TIP[1] > INDEX_BASE[1] or abs(THUMB_TIP[1] - INDEX_BASE[1]) < HORIZONTAL_ERROR_MARGIN:
        return 2
    return 3

# check position of tip of index finger relative to other LMs


def analyseIndexFinger(lm_list):
    INDEX_FINGER_TIP = lm_list[8]
    INDEX_FINGER_DIP = lm_list[7]
    INDEX_FINGER_PIP = lm_list[6]
    INDEX_FINGER_MCP = lm_list[5]

    if INDEX_FINGER_TIP[2] > INDEX_FINGER_MCP[2] or abs(INDEX_FINGER_TIP[2] - INDEX_FINGER_MCP[2]) < VERTICAL_ERROR_MARGIN:
        return 0
    elif INDEX_FINGER_TIP[2] > INDEX_FINGER_PIP[2] or abs(INDEX_FINGER_TIP[2] - INDEX_FINGER_PIP[2]) < VERTICAL_ERROR_MARGIN:
        return 1
    elif INDEX_FINGER_TIP[2] > INDEX_FINGER_DIP[2] or abs(INDEX_FINGER_TIP[2] - INDEX_FINGER_DIP[2]) < VERTICAL_ERROR_MARGIN:
        return 2
    return 3

# check position of tip of middle finger relative to other LMs


def analyseMiddleFinger(lm_list):
    MIDDLE_FINGER_TIP = lm_list[12]
    MIDDLE_FINGER_DIP = lm_list[11]
    MIDDLE_FINGER_PIP = lm_list[10]
    MIDDLE_FINGER_MCP = lm_list[9]

    if MIDDLE_FINGER_TIP[2] > MIDDLE_FINGER_MCP[2] or abs(MIDDLE_FINGER_TIP[2] - MIDDLE_FINGER_MCP[2]) < VERTICAL_ERROR_MARGIN:
        return 0
    elif MIDDLE_FINGER_TIP[2] > MIDDLE_FINGER_PIP[2] or abs(MIDDLE_FINGER_TIP[2] - MIDDLE_FINGER_PIP[2]) < VERTICAL_ERROR_MARGIN:
        return 1
    elif MIDDLE_FINGER_TIP[2] > MIDDLE_FINGER_DIP[2] or abs(MIDDLE_FINGER_TIP[2] - MIDDLE_FINGER_DIP[2]) < VERTICAL_ERROR_MARGIN:
        return 2
    return 3

# check position of tip of ring finger relative to other LMs


def analyseRingFinger(lm_list):
    RING_FINGER_TIP = lm_list[16]
    RING_FINGER_DIP = lm_list[15]
    RING_FINGER_PIP = lm_list[14]
    RING_FINGER_MCP = lm_list[13]

    if RING_FINGER_TIP[2] > RING_FINGER_MCP[2] or abs(RING_FINGER_TIP[2] - RING_FINGER_MCP[2]) < VERTICAL_ERROR_MARGIN:
        return 0
    elif RING_FINGER_TIP[2] > RING_FINGER_PIP[2] or abs(RING_FINGER_TIP[2] - RING_FINGER_PIP[2]) < VERTICAL_ERROR_MARGIN:
        return 1
    elif RING_FINGER_TIP[2] > RING_FINGER_DIP[2] or abs(RING_FINGER_TIP[2] - RING_FINGER_DIP[2]) < VERTICAL_ERROR_MARGIN:
        return 2
    return 3

# check position of tip of pinky relative to other LMs


def analysePinkyFinger(lm_list):
    PINKY_FINGER_TIP = lm_list[20]
    PINKY_FINGER_DIP = lm_list[19]
    PINKY_FINGER_PIP = lm_list[18]
    PINKY_FINGER_MCP = lm_list[17]

    if PINKY_FINGER_TIP[2] > PINKY_FINGER_MCP[2] or abs(PINKY_FINGER_TIP[2] - PINKY_FINGER_MCP[2]) < VERTICAL_ERROR_MARGIN:
        return 0
    elif PINKY_FINGER_TIP[2] > PINKY_FINGER_PIP[2] or abs(PINKY_FINGER_TIP[2] - PINKY_FINGER_PIP[2]) < VERTICAL_ERROR_MARGIN:
        return 1
    elif PINKY_FINGER_TIP[2] > PINKY_FINGER_DIP[2] or abs(PINKY_FINGER_TIP[2] - PINKY_FINGER_DIP[2]) < VERTICAL_ERROR_MARGIN:
        return 2
    return 3


# format is [thumb, index, middle, ring, pinky]

# SCHEME FOR THUMB (different since thumb is measured horizontally instead of vertica
# 0 for bent past pinky finger's x-value (like in "R" and "W")
# 1 for bent past middle finger's x-value (like in "E")
# 2 for bent past index finger's x-value (like in "B")lly)
# 3 for vertical/almost vertical thumb (like in letter "A")

# SCHEME FOR FOUR FINGERS EXCLUDING THUMB (measured using y-value)
# 0 for all the way down (fingers closed like fist)
# 1 for over 50% down but not all the way down (crosses LM2's y value)
# 2 for almost pointing up but not all the way up (crosses own finger's second highest LM)
# 3 for all the way up (fingers pointing up like pencil)

CONVERSION_LOOKUP = {
    (3, 0, 0, 0, 0): "A",
    (3, 3, 3, 3, 3): "B",
    (2, 2, 2, 2, 2): "C",
    (1, 3, 1, 1, 1): "D",
    (1, 1, 1, 1, 1): "E",
    (3, 2, 3, 3, 3): "F",
    (3, 3, 1, 1, 1): "G",
    (3, 3, 3, 0, 0): "H",
    (3, 0, 0, 0, 3): "I",
    (3, 0, 0, 0, 2): "J",
    (3, 3, 2, 0, 0): "K",
    (3, 3, 0, 0, 0): "L",
    (2, 0, 0, 0, 0): "M",
    (2, 1, 1, 0, 0): "N",
    (3, 1, 1, 0, 1): "O",
    (2, 3, 0, 0, 0): "P",
    (2, 3, 3, 0, 0): "R",
    (1, 0, 0, 0, 0): "S",
    (3, 2, 0, 0, 0): "T",
    (0, 3, 3, 0, 0): "U",
    # come back to V, same positioning as U
    (0, 3, 3, 3, 0): "W",
    (1, 3, 0, 0, 0): "X",
    # come back to Y, same positioning as I
    # come back to Z, same positioning as L

}

# def points(self, x, y, z):

# def finger(self, points):
# self.points[4]


# def fingerClosed:
# for x in 4:
# if fing[x].y (within range of) index[x+1].y
# Then fingerclosed = true


# finding c
# if index.x && index.y within range of pinky.x && pinky.y

# index[4] storing 4 landmarks of the index
# pinky[4] storing 4 landmarks of the index


# for x in 4:
#    if (pinky[x] > [index[x] +20] && if pinky[x] < [index[x]] + 30)
#   return

# Reference for c valeus


# thumb

# ID 1 : -0.054008327424526215
# ID 2 : -0.08915983885526657
# ID 3 : -0.1106901615858078
# ID 4 : -0.13401658833026886

# index

# ID 5 : -0.09317348152399063
# ID 6 : -0.1340368390083313
# ID 7 : -0.16393175721168518
# ID 8 : -0.18637309968471527

# third

# ID 9 : -0.07456375658512115
# ID 10 : -0.11399233341217041
# ID 11 : -0.14275501668453217
# ID 12 : -0.163238525390625

# ring

# ID 13 : -0.005223339889198542
# ID 14 : -0.027664903551340103
# ID 15 : -0.04998425021767616
# ID 16 : -0.06748953461647034

# pinky

# ID 17 : -0.05205222964286804
# ID 18 : -0.07689081877470016
# ID 19 : -0.09152737259864807
# ID 20 : -0.10459191352128983

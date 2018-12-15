import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
import os, time, copy, itertools

def initGelTable(size):
    gelTable = []

    for i in range(0, size):
        x = i % 3
        gelTable.append([x] * size)

    return gelTable

def initCandyTable(size, candy):
    candyTable = []

    for i in range(0, size):

        candyTable.append([])

        for j in range(0, size):

            color = randint(0, 5)

            if j > 1 and i > 1:
                if (candyTable[i][j - 1]['color'] == candy[color]['color'] and candyTable[i][j - 2]['color'] ==
                    candy[color]['color']) or (
                        candyTable[i - 1][j]['color'] == candy[color]['color'] and candyTable[i - 2][j]['color'] ==
                        candy[color]['color']):
                    temp = randint(0, 5)
                    while candy[temp]['color'] == candyTable[i][j - 1]['color'] or candy[temp]['color'] == \
                            candyTable[i - 1][j]['color']:
                        temp = randint(0, 5)
                    color = temp

            elif j > 1:
                if candyTable[i][j - 1]['color'] == candy[color]['color'] and candyTable[i][j - 2]['color'] == \
                        candy[color]['color']:
                    temp = randint(0, 5)
                    while color == temp:
                        temp = randint(0, 5)
                    color = temp

            elif i > 1:
                if candyTable[i - 1][j]['color'] == candy[color]['color'] and candyTable[i - 2][j]['color'] == \
                        candy[color]['color']:
                    temp = randint(0, 5)
                    while color == temp:
                        temp = randint(0, 5)
                    color = temp

            candyTable[i].append({'color': candy[color]['color'], 'type': ' '})

    return candyTable

def checkMap(size, candyTable):

    for i in range(size):
        for j in range(size):
            if candyTable[i][j]['color'] == '@':
                return 1
            if i < size-1:
                if candyTable[i][j]['color'] == candyTable[i+1][j]['color']:
                    try:
                        candyTable[i + 3][j]['color'] == candyTable[i][j]['color']
                    except IndexError:
                        pass
                    else:
                        if candyTable[i+3][j]['color'] == candyTable[i][j]['color']:
                            return 1

                    try:
                        candyTable[i+2][j-1]['color'] == candyTable[i][j]['color']
                    except IndexError:
                        pass
                    else:
                        if candyTable[i+2][j-1]['color'] == candyTable[i][j]['color']:
                            return 1

                    try:
                        candyTable[i+2][j+1]['color'] == candyTable[i][j]['color']
                    except IndexError:
                        pass
                    else:
                        if candyTable[i+2][j+1]['color'] == candyTable[i][j]['color']:
                            return 1

                    try:
                        candyTable[i-2][j]['color'] == candyTable[i][j]['color']
                    except IndexError:
                        pass
                    else:
                        if candyTable[i-2][j]['color'] == candyTable[i][j]['color']:
                            return 1

                    try:
                        candyTable[i-1][j-1]['color'] == candyTable[i][j]['color']
                    except IndexError:
                        pass
                    else:
                        if candyTable[i-1][j-1]['color'] == candyTable[i][j]['color']:
                            return 1

                    try:
                        candyTable[i-1][j+1]['color'] == candyTable[i][j]['color']
                    except IndexError:
                        pass
                    else:
                        if candyTable[i-1][j+1]['color'] == candyTable[i][j]['color']:
                            return 1
            if i < size-2:
                if candyTable[i][j]['color'] == candyTable[i+2][j]['color']:
                    try:
                        candyTable[i+1][j+1]['color'] == candyTable[i][j]['color']
                    except IndexError:
                        pass
                    else:
                        if candyTable[i+1][j+1]['color'] == candyTable[i][j]['color']:
                            return 1

                    try:
                        candyTable[i+1][j-1]['color'] == candyTable[i][j]['color']
                    except IndexError:
                        pass
                    else:
                        if candyTable[i+1][j-1]['color'] == candyTable[i][j]['color']:
                            return 1
            if j < size-1:
                if candyTable[i][j]['color'] == candyTable[i][j+1]['color']:
                    try:
                        candyTable[i][j+3]['color'] == candyTable[i][j]['color']
                    except IndexError:
                        pass
                    else:
                        if candyTable[i][j+3]['color'] == candyTable[i][j]['color']:
                            return 1

                    try:
                        candyTable[i-1][j+2]['color'] == candyTable[i][j]['color']
                    except IndexError:
                        pass
                    else:
                        if candyTable[i-1][j+2]['color'] == candyTable[i][j]['color']:
                            return 1

                    try:
                        candyTable[i+1][j+2]['color'] == candyTable[i][j]['color']
                    except IndexError:
                        pass
                    else:
                        if candyTable[i+1][j+2]['color'] == candyTable[i][j]['color']:
                            return 1

                    try:
                        candyTable[i][j-2]['color'] == candyTable[i][j]['color']
                    except IndexError:
                        pass
                    else:
                        if candyTable[i][j-2]['color'] == candyTable[i][j]['color']:
                            return 1

                    try:
                        candyTable[i-1][j-1]['color'] == candyTable[i][j]['color']
                    except IndexError:
                        pass
                    else:
                        if candyTable[i-1][j-1]['color'] == candyTable[i][j]['color']:
                            return 1

                    try:
                        candyTable[i+1][j-1]['color'] == candyTable[i][j]['color']
                    except IndexError:
                        pass
                    else:
                        if candyTable[i+1][j-1]['color'] == candyTable[i][j]['color']:
                            return 1
            if j < size-2:
                if candyTable[i][j]['color'] == candyTable[i][j+2]['color']:
                    try:
                        candyTable[i+1][j+1]['color'] == candyTable[i][j]['color']
                    except IndexError:
                        pass
                    else:
                        if candyTable[i+1][j+1]['color'] == candyTable[i][j]['color']:
                            return 1

                    try:
                        candyTable[i-1][j+1]['color'] == candyTable[i][j]['color']
                    except IndexError:
                        pass
                    else:
                        if candyTable[i-1][j+1]['color'] == candyTable[i][j]['color']:
                            return 1
    return 0

class window1(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(438, 306)
        self.setWindowTitle("Candy Crush")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Candy Crush")
        self.label.setGeometry(QtCore.QRect(110, 40, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setText("Enter the size of the game table:")
        self.label_2.setGeometry(QtCore.QRect(90, 130, 161, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setText("Enter the number of allowed moves:")
        self.label_3.setGeometry(QtCore.QRect(90, 170, 181, 16))
        self.label_3.setObjectName("label_3")

        self.spinBox = QtWidgets.QSpinBox(self)
        self.spinBox.setGeometry(QtCore.QRect(300, 130, 42, 22))
        self.spinBox.setMinimum(3)
        self.spinBox.setObjectName("spinBox")

        self.spinBox_2 = QtWidgets.QSpinBox(self)
        self.spinBox_2.setGeometry(QtCore.QRect(300, 170, 42, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setObjectName("spinBox_2")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setText("Start")
        self.pushButton.setGeometry(QtCore.QRect(170, 220, 111, 41))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.initGame)

        self.show()

    def initGame(self):
        size = self.spinBox.value()
        moves = self.spinBox_2.value()

        gelTable = initGelTable(size)

        candyTable = initCandyTable(size, self.candy)
        while not (checkMap(size, candyTable)):
            candyTable = initCandyTable(size, self.candy)

        self.w2 = window2(size, moves, self.candy, candyTable, gelTable)
        self.w2.show()
        self.hide()

    candy = [{'color': 'R'},
             {'color': 'B'},
             {'color': 'G'},
             {'color': 'O'},
             {'color': 'P'},
             {'color': 'Y'},
             {'color': '@'}]

class window2(QtWidgets.QWidget):

    def __init__(self, size, moves, candy, candyTable, gelTable):
        super().__init__()
        self.size = size
        self.moves = moves
        self.candy = candy
        self.candyTable = candyTable
        self.gelTable = gelTable
        self.d1 = dialog1("Invalid Move")
        self.d2 = dialog1("Refreshing Board")
        self.d3 = dialog2("You Won :)")
        self.d4 = dialog2("Game Over :(")
        self.initUI()

    def initUI(self):
        self.resize(610, 580)
        self.setWindowTitle("Candy Crush")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Remaining Moves:")
        self.label.setGeometry(QtCore.QRect(50, 20, 111, 20))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(160, 20, 31, 16))
        self.label_2.setText(str(self.moves))
        self.label_2.setObjectName("label_2")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 70, 551, 300))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setText(self.getCandyTable())
        self.label_3.adjustSize()
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setText(self.getGelTable())
        self.label_4.adjustSize()
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(50, 430, 351, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(110, 410, 20, 151))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setText("Row")
        self.label_5.setGeometry(QtCore.QRect(70, 460, 47, 13))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setText("Column")
        self.label_6.setGeometry(QtCore.QRect(60, 520, 47, 13))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setText("Candy 1")
        self.label_7.setGeometry(QtCore.QRect(180, 410, 47, 13))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setText("Candy 2")
        self.label_8.setGeometry(QtCore.QRect(290, 410, 47, 13))
        self.label_8.setObjectName("label_8")

        self.spinBox = QtWidgets.QSpinBox(self)
        self.spinBox.setGeometry(QtCore.QRect(180, 460, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(self.size)
        self.spinBox.setObjectName("spinBox")

        self.spinBox_2 = QtWidgets.QSpinBox(self)
        self.spinBox_2.setGeometry(QtCore.QRect(290, 460, 42, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(self.size)
        self.spinBox_2.setObjectName("spinBox_2")

        self.spinBox_3 = QtWidgets.QSpinBox(self)
        self.spinBox_3.setGeometry(QtCore.QRect(180, 520, 42, 22))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(self.size)
        self.spinBox_3.setObjectName("spinBox_3")

        self.spinBox_4 = QtWidgets.QSpinBox(self)
        self.spinBox_4.setGeometry(QtCore.QRect(290, 520, 42, 22))
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(self.size)
        self.spinBox_4.setObjectName("spinBox_4")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setText("Switch")
        self.pushButton.setGeometry(QtCore.QRect(460, 450, 75, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.run)

    def getCandyTable(self):
        ct = ""

        for i in range(self.size):
            for j in range(self.size):
                ct = ct + self.candyTable[i][j]['color'] + self.candyTable[i][j]['type'] + "\t"

            ct = ct + "\n\n\n"

        return ct

    def getGelTable(self):
        gt = ""

        for i in range(self.size):
            for j in range(self.size):
                gt = gt + str(self.gelTable[i][j]) + "\t"

            gt = gt + "\n\n\n"

        return gt

    def run(self):
        candy1, candy2 = self.getMove()

        while not (self.checkMove(candy1, candy2)):
            self.d1.show()
            return

        self.switchCandy(candy1, candy2)

        if candy2[0] < candy1[0]:
            temp = candy1
            candy1 = candy2
            candy2 = temp

        if self.candyTable[candy1[0]][candy1[1]]['color'] == '@':
            self.updateMap2(candy1, candy2)
        elif self.candyTable[candy2[0]][candy2[1]]['color'] == '@':
            self.updateMap2(candy2, candy1)
        else:
            self.updateMap([candy1, candy2])

        self.fillMap()

        self.moves = self.moves - 1

        self.label_2.setText(str(self.moves))
        self.label_3.setText(self.getCandyTable())
        self.label_4.setText(self.getGelTable())

        if self.gelSum() == 0:
            self.d3.show()
        elif self.moves == 0:
            self.d4.show()
        else:
            if not checkMap(self.size, self.candyTable):
                while not (checkMap(self.size, self.candyTable)):
                    self.candyTable = initCandyTable(self.size, self.candy)
                self.d2.show()
                self.label_3.setText(self.getCandyTable())

    def getMove(self):

        row1 = self.spinBox.value()
        col1 = self.spinBox_3.value()

        row2 = self.spinBox_2.value()
        col2 = self.spinBox_4.value()

        return [row1 - 1, col1 - 1], [row2 - 1, col2 - 1]

    def checkMove(self, candy1, candy2):

        if self.candyTable[candy1[0]][candy1[1]]['color'] == self.candyTable[candy2[0]][candy2[1]]['color']:
            return 0

        if (self.candyTable[candy1[0]][candy1[1]]['color'] == '@' or self.candyTable[candy1[0]][candy1[1]]['type'] == '!' or
            self.candyTable[candy1[0]][candy1[1]]['type'] == '=' or self.candyTable[candy1[0]][candy1[1]]['type'] == '#') and \
                (self.candyTable[candy2[0]][candy2[1]]['color'] == '@' or self.candyTable[candy2[0]][candy2[1]]['type'] == '!' or
                 self.candyTable[candy2[0]][candy2[1]]['type'] == '=' or self.candyTable[candy2[0]][candy2[1]]['type'] == '#'):
            return 0

        elif self.candyTable[candy1[0]][candy1[1]]['color'] == '@' or self.candyTable[candy2[0]][candy2[1]]['color'] == '@':
            return 1

        candy = [candy1, candy2]

        for i in range(2):

            try:
                if (self.candyTable[candy[i][0] + 1][candy[i][1]]['color'] ==
                        self.candyTable[candy[(i + 1) % 2][0]][candy[(i + 1) % 2][1]]['color'] and
                        self.candyTable[candy[i][0] + 2][candy[i][1]]['color'] ==
                        self.candyTable[candy[(i + 1) % 2][0]][candy[(i + 1) % 2][1]]['color']):
                    return 1
            except IndexError:
                pass

            try:
                if (self.candyTable[candy[i][0] - 1][candy[i][1]]['color'] ==
                        self.candyTable[candy[(i + 1) % 2][0]][candy[(i + 1) % 2][1]]['color'] and
                        self.candyTable[candy[i][0] - 2][candy[i][1]]['color'] ==
                        self.candyTable[candy[(i + 1) % 2][0]][candy[(i + 1) % 2][1]]['color']):
                    return 1
            except IndexError:
                pass

            try:
                if (self.candyTable[candy[i][0] - 1][candy[i][1]]['color'] ==
                        self.candyTable[candy[(i + 1) % 2][0]][candy[(i + 1) % 2][1]]['color'] and
                        self.candyTable[candy[i][0] + 1][candy[i][1]]['color'] ==
                        self.candyTable[candy[(i + 1) % 2][0]][candy[(i + 1) % 2][1]]['color']):
                    return 1
            except IndexError:
                pass

            try:
                if (self.candyTable[candy[i][0]][candy[i][1] + 1]['color'] ==
                        self.candyTable[candy[(i + 1) % 2][0]][candy[(i + 1) % 2][1]]['color'] and
                        self.candyTable[candy[i][0]][candy[i][1] + 2]['color'] ==
                        self.candyTable[candy[(i + 1) % 2][0]][candy[(i + 1) % 2][1]]['color']):
                    return 1
            except IndexError:
                pass

            try:
                if (self.candyTable[candy[i][0]][candy[i][1] - 1]['color'] ==
                        self.candyTable[candy[(i + 1) % 2][0]][candy[(i + 1) % 2][1]]['color'] and
                        self.candyTable[candy[i][0]][candy[i][1] - 2]['color'] ==
                        self.candyTable[candy[(i + 1) % 2][0]][candy[(i + 1) % 2][1]]['color']):
                    return 1
            except IndexError:
                pass

            try:
                if (self.candyTable[candy[i][0]][candy[i][1] - 1]['color'] ==
                        self.candyTable[candy[(i + 1) % 2][0]][candy[(i + 1) % 2][1]]['color'] and
                        self.candyTable[candy[i][0]][candy[i][1] + 1]['color'] ==
                        self.candyTable[candy[(i + 1) % 2][0]][candy[(i + 1) % 2][1]]['color']):
                    return 1
            except IndexError:
                pass

    def switchCandy(self, candy1, candy2):
        temp = self.candyTable[candy1[0]][candy1[1]]
        self.candyTable[candy1[0]][candy1[1]] = self.candyTable[candy2[0]][candy2[1]]
        self.candyTable[candy2[0]][candy2[1]] = temp

    def updateMap(self, candys):

        temp = copy.deepcopy(self.candyTable)

        for candy in candys:

            burst = self.getBurst(candy)

            if not (len(burst[0]) == 0 and len(burst[1]) == 0):
                type = self.findType(burst)

                burst = [candy] + burst[0] + burst[1]

                burst = self.modifyBurst(burst)

                for i in burst:
                    if not (i == candy):
                        self.candyTable[i[0]][i[1]]['color'] = '*'
                    if self.gelTable[i[0]][i[1]] > 0:
                        self.gelTable[i[0]][i[1]] = self.gelTable[i[0]][i[1]] - 1;

                if type == 0:
                    self.candyTable[candy[0]][candy[1]]['color'] = '*'

                if type == 12:
                    self.candyTable[candy[0]][candy[1]]['type'] = '='

                if type == 11:
                    self.candyTable[candy[0]][candy[1]]['type'] = '!'

                if type == 2:
                    self.candyTable[candy[0]][candy[1]]['color'] = '@'
                    self.candyTable[candy[0]][candy[1]]['type'] = ' '

                if type == 3:
                    self.candyTable[candy[0]][candy[1]]['type'] = '#'

                movedCandy = self.dropCandy()

                movedCandy = [x for x in movedCandy if not (self.candyTable[x[0]][x[1]]['color'] == '*')]

                for i in range(self.size):
                    for j in range(self.size):
                        if self.candyTable[i][j]['color'] == '*':
                            self.candyTable[i][j]['color'] = ' '

                if not (temp == self.candyTable):
                    self.updateMap(movedCandy)

    def updateMap2(self, candy1, candy2):

        color = self.candyTable[candy2[0]][candy2[1]]['color']
        self.candyTable[candy1[0]][candy1[1]]['color'] = '*'

        if self.gelTable[candy1[0]][candy1[1]] > 0:
            self.gelTable[candy1[0]][candy1[1]] = self.gelTable[candy1[0]][candy1[1]] - 1;

        for i in range(self.size):
            for j in range(self.size):
                if self.candyTable[i][j]['color'] == color:
                    self.candyTable[i][j]['color'] = '*'
                    if self.gelTable[i][j] > 0:
                        self.gelTable[i][j] = self.gelTable[i][j] - 1;

        movedCandy = self.dropCandy()

        movedCandy = [x for x in movedCandy if not (self.candyTable[x[0]][x[1]]['color'] == '*')]

        for i in range(self.size):
            for j in range(self.size):
                if self.candyTable[i][j]['color'] == '*':
                    self.candyTable[i][j]['color'] = ' '

        self.updateMap(movedCandy)

    def getBurst(self, candy):

        burst = [[], []]

        for i in range(candy[0] - 1, -1, -1):
            try:
                if self.candyTable[i][candy[1]]['color'] == self.candyTable[candy[0]][candy[1]]['color']:
                    burst[0].append([i, candy[1]])
                else:
                    break
            except IndexError:
                pass

        burst[0].reverse();

        for i in range(candy[0] + 1, self.size, 1):
            try:
                if self.candyTable[i][candy[1]]['color'] == self.candyTable[candy[0]][candy[1]]['color']:
                    burst[0].append([i, candy[1]])
                else:
                    break
            except IndexError:
                pass

        for j in range(candy[1] - 1, -1, -1):
            try:
                if self.candyTable[candy[0]][j]['color'] == self.candyTable[candy[0]][candy[1]]['color']:
                    burst[1].append([candy[0], j])
                else:
                    break
            except IndexError:
                pass

        for j in range(candy[1] + 1, self.size, 1):
            try:
                if self.candyTable[candy[0]][j]['color'] == self.candyTable[candy[0]][candy[1]]['color']:
                    burst[1].append([candy[0], j])
                else:
                    break
            except IndexError:
                pass

        if len(burst[0]) < 2:
            burst[0] = []

        if len(burst[1]) < 2:
            burst[1] = []

        return burst

    def findType(self, burst):

        verCount = len(burst[0])
        horCount = len(burst[1])

        if (verCount < 2 and horCount == 2) or (horCount < 2 and verCount == 2):
            type = 0

        if verCount < 3 and horCount == 3:
            type = 12

        if horCount < 3 and verCount == 3:
            type = 11

        if (verCount < 3 and horCount > 3) or (horCount < 3 and verCount > 3):
            type = 2

        if horCount == 2 and verCount == 2:
            type = 3

        return type

    def modifyBurst(self, burst):

        temp = copy.deepcopy(burst)

        for i in burst:
            if self.candyTable[i[0]][i[1]]['type'] == '!':
                newBurst = [[x, i[1]] for x in range(self.size)]
                temp = temp + newBurst
            elif self.candyTable[i[0]][i[1]]['type'] == '=':
                newBurst = [[i[0], y] for y in range(self.size)]
                temp = temp + newBurst
            elif self.candyTable[i[0]][i[1]]['type'] == '#':
                newBurst = [[i[0] + x, i[1] + y] for x in range(-1, 2) for y in range(-1, 2)]
                temp = temp + newBurst

        temp.sort()

        temp = list(temp for temp, _ in itertools.groupby(temp))

        burst.sort()

        if not (temp == burst):
            return self.modifyBurst(temp)
        else:
            return temp

    def dropCandy(self):

        moved = []

        temp = copy.deepcopy(self.candyTable)

        for i in range(self.size - 1):
            for j in range(self.size):
                if self.candyTable[i + 1][j]['color'] == '*' and not (self.candyTable[i][j]['color'] == '*'):
                    self.candyTable[i + 1][j]['color'] = self.candyTable[i][j]['color']
                    self.candyTable[i + 1][j]['type'] = self.candyTable[i][j]['type']
                    self.candyTable[i][j]['color'] = '*'
                    moved.append([i + 1, j])

        if not (temp == self.candyTable):
            moved = moved + self.dropCandy()

        moved.sort()

        return list(moved for moved, _ in itertools.groupby(moved))

    def fillMap(self):

        for row in range(self.size):
            for col in range(self.size):
                if self.candyTable[row][col]['color'] == ' ':
                    r = randint(0, 5)
                    self.candyTable[row][col]['color'] = self.candy[r]['color']
                    self.candyTable[row][col]['type'] = ' '
                    burst = self.getBurst([row, col])
                    while not (len(burst[0]) == 0 and len(burst[1]) == 0):
                        r = randint(0, 5)
                        self.candyTable[row][col]['color'] = self.candy[r]['color']
                        self.candyTable[row][col]['type'] = ' '
                        burst = self.getBurst([row, col])

    def gelSum(self):

        s = 0

        for row in self.gelTable:
            s = s + sum(row)

        return s

class dialog1(QtWidgets.QDialog):
    def __init__(self, s):
        super().__init__()
        self.setupUi()
        self.label.setText(s)

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(333, 167)
        self.setWindowTitle("Candy Crush")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(90, 30, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(130, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.hide)

class dialog2(QtWidgets.QDialog):
    def __init__(self, s):
        super().__init__()
        self.setupUi()
        self.label.setText(s)

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(343, 173)
        self.setWindowTitle("Candy Crush")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 40, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(80, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Retry")
        self.pushButton.clicked.connect(self.retry)

        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 110, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("Exit")
        self.pushButton_2.clicked.connect(self.exit)

    def retry(self):
        w1.w2.close()
        w1.show()
        self.close()

    def exit(self):
        w1.w2.close()
        w1.close()
        self.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w1 = window1()
    sys.exit(app.exec_())
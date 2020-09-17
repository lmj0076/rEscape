from bangtal import *

#장면 생성
scene1 = Scene("룸1", "images2/background2.jpg")
scene2 = Scene("룸2", "images2/background.png")


#################################################

#scene1


#문 생성
door1 = Object("images2/door1.png")
door1.locate(scene1,250, 200)
door1.show()
door1.closed = True

#문 클릭 시 열림/메세지
def door1_onMouseAction(x, y, action):
    if door1.closed == True:
        if key.inHand():
            door1.setImage("images2/door2.png")
            door1.closed = False
        else:
            showMessage("열쇄가 필요해요")
    else:
        scene2.enter()

door1.onMouseAction = door1_onMouseAction


#열쇄 생성
key = Object("images2/key.png")
key.locate(scene1,485, 130)
key.setScale(0.2)
key.show()

#열쇄 클릭시 줍기
def key_onMouseAction(x, y, action):
    key.pick()

key.onMouseAction = key_onMouseAction


#항아리 생성
jar = Object("images2/항아리.png")
jar.locate(scene1,420, 100)
jar.setScale(0.4)
jar.show()

#항아리 클릭시 이동
def jar_onMouseAction(x, y, action):
    if glove.inHand():
        if action == MouseAction.DRAG_UP:
            jar.locate(scene1, 450, 200)
    else:
        showMessage("비싼 항아리에요! 맨손으로 만질 수 없어요!")

jar.onMouseAction = jar_onMouseAction


#장갑 생성
glove = Object("images2/장갑.png")
glove.locate(scene1,800, 500)
glove.setScale(0.2)
glove.show()

#장갑 클릭시 줍기
def glove_onMouseAction(x, y, action):
    glove.pick()

glove.onMouseAction = glove_onMouseAction


#액자 생성
flower = Object("images2/flower.png")
flower.locate(scene1, 750, 500)
flower.setScale(0.3)
flower.show()

#액자 클릭시 이동
def flower_onMouseAction(x, y, action):
    if action == MouseAction.DRAG_DOWN:
        flower.locate(scene1, 750, 300)

flower.onMouseAction = flower_onMouseAction


#기타 가구
chair = Object("images2/chair.png")
chair.locate(scene1, 835, 100)
chair.show()

ex1 = Object("images2/ex1.png")
ex1.locate(scene1, 600, 100)
ex1.setScale(0.5)
ex1.show()

flower2 = Object("images2/flower2.png")
flower2.locate(scene1, 500, 480)
flower2.setScale(0.5)
flower2.show()

flower3 = Object("images2/flower3.png")
flower3.locate(scene1, 25, 50)
flower3.setScale(0.5)
flower3.show()


#설명견 생성
dog = Object("images2/dog.png")
dog.locate(scene1, 900, 220)
dog.setScale(0.5)
dog.show()

#설명견 클릭시 메시지
def dog_onMouseAction(x, y, action):
    showMessage("안녕~ 비싼 해바라기 뒤에 비싼 물건을 만질 때 쓰는 물건이 있어~")

dog.onMouseAction = dog_onMouseAction


#################################################

#scene2


#문2 생성
door2 = Object("images2/door2.png")
door2.locate(scene2,280, 130)
door2.show()

#문2 클릭시 scene1으로 이동
def door2_onMouseAction(x, y, action):
    scene1.enter()

door2.onMouseAction = door2_onMouseAction


#문3 생성
door3 = Object("images2/door1.png")
door3.locate(scene2,780, 130)
door3.show()
door3.closed = True


#벌래 생성
bug1 = Object("images2/bug.png")
bug2 = Object("images2/bug.png")
bug3 = Object("images2/bug.png")
bug4 = Object("images2/bug.png")
bug5 = Object("images2/bug.png")
bug6 = Object("images2/bug.png")
bug7 = Object("images2/bug.png")
bug1.cnt = 7    #벌래 수 카운트 다운

bug1.locate(scene2, 100, 200)
bug2.locate(scene2, 800, 433)
bug3.locate(scene2, 950, 593)
bug4.locate(scene2, 185, 400)
bug5.locate(scene2, 600, 280)
bug6.locate(scene2, 550, 100)
bug7.locate(scene2, 100, 20)

bug1.setScale(0.3)
bug2.setScale(0.3)
bug3.setScale(0.3)
bug4.setScale(0.3)
bug5.setScale(0.3)
bug6.setScale(0.3)
bug7.setScale(0.3)

bug1.show()
bug2.show()
bug3.show()
bug4.show()
bug5.show()
bug6.show()
bug7.show()


#설명견 생성
dog2 = Object("images2/dog.png")
dog2.locate(scene2, 100, 20)
dog2.setScale(0.5)
dog2.show()
dog2.moved = False

#설명견 클릭시 메시지/이동
def dog2_onMouseAction(x, y, action):
    showMessage("벌래는 총 7마리야! (쉿! 내 뒤에도 한 마리 있어~)")
    if dog2.moved == False:
        if action == MouseAction.DRAG_RIGHT:
            dog2.locate(scene2, 200,20)
            dog2.moved = True
dog2.onMouseAction = dog2_onMouseAction


#상자 생성
box3 = Object("images2/box3.png")
box3.locate(scene2, 500, 20)
box3.setScale(0.5)
box3.show()
box3.moved = False

#상자 클릭시 이동
def box3_onMouseAction(x, y, action):
    if box3.moved == False:
        if action == MouseAction.DRAG_RIGHT:
            box3.locate(scene2, 600, 20)
            box3.moved = True
            
box3.onMouseAction = box3_onMouseAction


#보물상자 생성
box1 = Object("images2/box1.png")
box1.locate(scene2, 900, 15)
box1.setScale(0.5)
box1.show()
box1.closed = True


#채 생성
stick = Object("images2/stick.png")
stick.locate(scene2, 900, 80)
stick.setScale(0.7)
stick.hide()


#키패드 생성
keypad = Object("images2/keypad.png")
keypad.locate(scene2, 965, 80)
keypad.setScale(0.05)
keypad.show()


#전등 생성
light = Object("images2/light.png")
light.locate(scene2, 600, 600)
light.setScale(0.2)
light.show()
light.lighted = True


#힌트 생성
message = Object("images2/message.png")
message.locate(scene2, 350, 50)
message.hide()

#전등 클릭시 밝기 조정/힌트 표시
def light_onMouseAction(x, y, action):
    if light.lighted == True:
        scene2.setLight(0.3)
        message.show()
        light.lighted = False
    else:
        scene2.setLight(1.0)
        message.hide()
        light.lighted = True

light.onMouseAction = light_onMouseAction


#보물상자 암호 열림시 이밴트
def box1_onKeypad():
    showMessage("철커덕~")
    box1.closed = False

box1.onKeypad = box1_onKeypad


#키패드 암호 설정
def keypad_onMouseAction(x, y, action):
    showKeypad("gold", box1)

keypad.onMouseAction = keypad_onMouseAction


#보물상자 클릭시 열림/채 표시
def box1_onMouseAction(x, y, action):
    if box1.closed == False:
        keypad.hide()
        box1.setImage("images2/box2.png")
        stick.show()
    else:
        showMessage("암호를 입력하세요")

box1.onMouseAction = box1_onMouseAction


#채 클릭시 줍기
def stick_onMouseAction(x, y, action):
    stick.pick()

stick.onMouseAction = stick_onMouseAction

#벌래(1~7) 클릭시 사라짐/카운트 다운
def bug1_onMouseAction(x, y, action):
    if stick.inHand():
        bug1.hide()
        bug1.cnt = bug1.cnt - 1
    else:
        showMessage("채가 필요해요~")
def bug2_onMouseAction(x, y, action):
    if stick.inHand():
        bug2.hide()
        bug1.cnt = bug1.cnt - 1
    else:
        showMessage("채가 필요해요~")
def bug3_onMouseAction(x, y, action):
    if stick.inHand():
        bug3.hide()
        bug1.cnt = bug1.cnt - 1
    else:
        showMessage("채가 필요해요~")
def bug4_onMouseAction(x, y, action):
    if stick.inHand():
        bug4.hide()
        bug1.cnt = bug1.cnt - 1
    else:
        showMessage("채가 필요해요~")
def bug5_onMouseAction(x, y, action):
    if stick.inHand():
        bug5.hide()
        bug1.cnt = bug1.cnt - 1
    else:
        showMessage("채가 필요해요~")
def bug6_onMouseAction(x, y, action):
    if stick.inHand():
        bug6.hide()
        bug1.cnt = bug1.cnt - 1
    else:
        showMessage("채가 필요해요~")
def bug7_onMouseAction(x, y, action):
    if stick.inHand():
        bug7.hide()
        bug1.cnt = bug1.cnt - 1
    else:
        showMessage("채가 필요해요~")

bug1.onMouseAction = bug1_onMouseAction
bug2.onMouseAction = bug2_onMouseAction
bug3.onMouseAction = bug3_onMouseAction
bug4.onMouseAction = bug4_onMouseAction
bug5.onMouseAction = bug5_onMouseAction
bug6.onMouseAction = bug6_onMouseAction
bug7.onMouseAction = bug7_onMouseAction


#문3 클릭시 열림/메시지
def door3_onMouseAction(x, y, action):
    if bug1.cnt == 0:
        if door3.closed == True:
            door3.setImage("images2/door2.png")
            showMessage("달칵~")
            door3.closed = False
        else:
            endGame()
    else:
        showMessage("벌래를 다 잡지 못했어요ㅠㅠ")

door3.onMouseAction = door3_onMouseAction


#################################################

#게임 시작
startGame(scene1)
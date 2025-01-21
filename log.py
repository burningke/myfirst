import pydirectinput
import time

Nam_vor = list("")
Nam_nach = list("")
Sch_vor = list("")
Sch_nach = list("")
time.sleep(5.5)

for i,j in enumerate(Nam_vor):
    pydirectinput.press(j)
    time.sleep(0.1)

pydirectinput.keyDown('shift')
pydirectinput.press('2')
pydirectinput.keyUp('shift')
time.sleep(0.1)

for i,j in enumerate(Nam_nach):
    pydirectinput.press(j)
    time.sleep(0.1)

pydirectinput.press('enter')
time.sleep(1.5)

for i,j in enumerate(Sch_vor):
    pydirectinput.press(j)
    time.sleep(0.1)

pydirectinput.keyDown('shift')
pydirectinput.press('1')
pydirectinput.keyUp('shift')
time.sleep(0.1)

for i,j in enumerate(Sch_nach):
    pydirectinput.press(j)
    time.sleep(0.1)

pydirectinput.press('enter')


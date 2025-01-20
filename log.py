import pydirectinput
import time

Nam_vor = "".split()
Nam_nach = "".split()
Sch_vor = "".split()
Sch_nach = "".split()
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
time.sleep(0.1)

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


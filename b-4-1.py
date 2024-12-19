import pyxel

pyxel.init(200, 200)
pyxel.cls(1)

for a in range(0, 10, 1):
    for b in range(0, 10, 1):
        if (a+b) % 2 == 0:
            pyxel.circ(a*20+10, b*20+10, 10, 6)
        else:
            pyxel.circ(a*20+10, b*20+10, 10, 14)

pyxel.show()
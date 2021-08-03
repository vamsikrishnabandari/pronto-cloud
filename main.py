#Created on 03/08/2021.
#Author: vamsikrishna bandari
x = 0
y = 0
xpos = 'True'
ypos = 'True'

#Here xpos and ypos are coordinates

def checkleft(xpos,ypos):
    if xpos == 'Stop' and ypos == 'True':
        xpos = 'False Stop'
        return xpos
    elif xpos == 'False' and ypos == 'Stop':
        ypos = 'Stop False'
        return ypos
    elif xpos == 'Stop' and ypos == 'False':
        xpos = 'True stop'
        return xpos 
    elif xpos == 'True' and ypos == 'Stop':
        ypos = 'Stop True'
        return ypos

def checkright(xpos,ypos):
    if xpos == 'Stop' and ypos == 'True':
        xpos = 'True Stop'
        return xpos
    elif xpos == 'True' and ypos == 'Stop':
        ypos = 'Stop False'
        return ypos
    elif xpos == 'Stop' and ypos == 'False':
        xpos = 'False stop'
        return xpos 
    elif xpos == 'False' and ypos == 'Stop':
        ypos = 'Stop True'
        return ypos

def rotateleft(lx,ly,count):
    if lx == 'Stop' and ly =='True':
        return count
    else:
        res = checkleft(lx,ly)
        resp = res.split(' ')
        lx = resp[0]
        ly = resp[1]
        count = count + 1
        return rotateleft(lx,ly,count)

def rotateright(rx,ry,count):
    if rx == 'Stop' and ry =='True':
        return count
    else:
        res = checkright(rx,ry)
        resp = res.split(' ')
        rx = resp[0]
        ry = resp[1]
        count = count + 1
        return rotateright(rx,ry,count)
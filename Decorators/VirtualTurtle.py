#Написать параметрический итератор turtle(coord, direction), описывающий движение «черепахи» по координатной плоскости.
#coord — это кортеж из двух целочисленных начальных координат, direction описывает первоначальное направление
#(0 — восток, 1 — север, 2 — запад, 3 — юг). Координаты увеличиваются на северо-восток.
#Итератор принимает три команды — "f" (переход на 1 шаг вперёд), "l" (поворот против часовой стрелки на 90°)
#и "r" (поворот по часовой стрелке на 90°) и возвращает текущие координаты черепахи.

def turtle(Position,Direct):
    ChDirFlag=True
    XOff=YOff=0
    while True:
        if ChDirFlag:
            if Direct==0:
                XOff=1
            elif Direct==1:
                YOff=+1
            elif Direct==2:
                XOff=-1
            elif Direct==3:
                YOff=-1
        ChDirFlag=False
        State=yield Position
        if State=='r':
            Direct=(Direct-1)%4
            ChDirFlag=True
            XOff=YOff=0
        if State=='l':
            Direct=(Direct+1)%4
            ChDirFlag=True
            XOff=YOff=0
        if State=='f':
            Position=(Position[0]+XOff,Position[1]+YOff)

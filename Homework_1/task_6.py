import math

print('Введите тип фигуры (круг, треугольник, прямоугольник): ')
shape = input().lower()
area = 0
if 'круг' in shape:
    print('Введите радиус круга: ')
    radius = float(input())
    area = math.pi * radius * radius
elif 'треугольник' in shape:
    print('Введите длины трех сторон треугольника (в одну строку через пробел): ')
    side1, side2, side3 = map(int, input().split())
    semiPerimeter = (side1 + side2 + side3)/2
    area = math.sqrt(semiPerimeter * (semiPerimeter - side1)*(semiPerimeter - side2) * (semiPerimeter - side3))
elif 'прямоугольник' in shape:
    print('Введите длины сторон прямоугольника (в одну строку через пробел): ')
    side1, side2 = map(int, input().split())
    area = side1 * side2
if area != 0:
    print(f'Площадь {shape}а равна: ', "%.2f" % area)
else:
    print('Пожалуйста, выберете одну из трех предложенных фигур. Попробуйте снова')

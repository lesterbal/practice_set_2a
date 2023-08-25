from math import sqrt

def calculate_triangle_area(a, b, c):
    semi_perimeter = (a + b + c) / 2
    return sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))

measurement_unit = 'cm'

try:
    sides = [float(input(f':: Enter value for side {i+1}: ')) for i in range(3)]

    triangle_area = calculate_triangle_area(*sides)

    print(f'\n[Area of triangle = {triangle_area:.2f}{measurement_unit}]')
except ValueError:
    print('\n[!] Please enter valid numeric values!')

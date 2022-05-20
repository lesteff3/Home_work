from classes import Circle, Triangle, Square, figure_perimeter

if __name__ == '__main__':
    circle = Circle(x=3, y=1, radius=10)
    triangle = Triangle(x=12, y=13, z=14)
    square = Square(x=10, y=10)
    figure_perimeter(figure_list=[circle, triangle, square])


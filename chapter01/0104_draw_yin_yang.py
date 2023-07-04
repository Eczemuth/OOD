class Canvas:
    def __init__(self, w, h, bg = '.'):
        self.w = w
        self.h = h
        self.canvas = [[bg for _ in range(w)] for _ in range(h)]

    def draw(self):
        r = ''
        for row in self.canvas:
            for pixel in row:
                r += pixel
            r += '\n'

        print(r)

    def draw_rectangle(self, top_left_pos, w, h, brush = '*'):
        x1, y1 = top_left_pos
        for y in range(y1, y1 + h):
            for x in range(x1, x1 + w):
                if x < 0 or y < 0:
                    continue
                try:
                    self.canvas[y][x] = brush
                except IndexError:
                    continue

    def draw_circle(self, pos, r, brush = '*'):
        x1, y1 = pos
        for y in range(self.h):
            for x in range(self.w):
                if ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5 <= r:
                    print(x, y)
                    self.canvas[y][x] = brush

    def __trinagle_area(self, p1, p2, p3):
        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

    def __find_bounding_box(self, *points):
        min_x = points[0][0]
        min_y = points[0][1]
        max_x = points[0][0]
        max_y = points[0][1]
        for point in points:
            x = point[0]
            y = point[1]

            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x

            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y

        return (min_x, max_y,), (max_x, min_y)

    def __point_in_triangle(self, p, p1, p2, p3):
        a1 = self.__trinagle_area(p, p2, p3)
        a2 = self.__trinagle_area(p, p1, p2)
        a3 = self.__trinagle_area(p, p1, p3)
        a = self.__trinagle_area(p1, p2, p3)
        return a == a1 + a2 + a3

    def draw_triangle(self, p1, p2, p3, brush = '*'):
        tl, br = self.__find_bounding_box(p1, p2, p3)
        min_x, max_y = tl
        max_x, min_y = br
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if x < 0 or y < 0:
                    continue
                p = (x, y)
                if self.__point_in_triangle(p, p1, p2, p3):
                    try:
                        self.canvas[y][x] = brush
                    except IndexError:
                        continue


num = int(input('Enter Input : '))
w = (num + 2) * 2

canvas = Canvas(w, w)

canvas.draw_rectangle((w//2, 0), w//2, w//2, brush='+')
canvas.draw_rectangle((w//2 + 1, 1), num, num, brush='#')

canvas.draw_rectangle((0, w//2), w//2, w//2, brush='#')
canvas.draw_rectangle((1, w//2 + 1), num, num, brush='+')

canvas.draw_triangle((w//2 - 1, 0), (w//2 - 1, w//2 - 1), (0, w//2 - 1), brush='#')
canvas.draw_triangle((w//2, w//2), (w - 1, w//2), (w//2, w - 1), brush='+')

canvas.draw()

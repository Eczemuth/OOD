# This is Canvas class which allow you to draw some primitive shapes (rectangle, triangle) using coordinate geometry.
# In the best case if someone has use my code and find bugs or someway to improve please tell me


class Canvas:
    ASCII_OPAQUE = """ .'`^",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"""
    OPAQUE_RATIO = 70

    def __init__(self, w, h, bg='.'):
        # the bg will be the common element in canvas list
        self.bg = bg
        self.w = w
        self.h = h
        self.canvas = [[bg for _ in range(w)] for _ in range(h)]

    def clear(self):
        self.canvas = [[self.bg for _ in range(self.w)] for _ in range(self.h)]

    def draw(self):
        r = ''
        for row in self.canvas:
            for pixel in row:
                r += pixel
            r += '\n'

        print(r)

    def __verify_brush(self, brush, opacity = None):
        if opacity:
            brush = self.ASCII_OPAQUE[int(opacity * self.OPAQUE_RATIO) - 1]
        return brush

    def __pos_in_canvas(self, pos):
        x, y = pos
        return 0 < x < self.w and 0 < y < self.h

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

    def draw_rectangle(self, top_left_pos, w, h, brush = '*', opacity = None):
        x1, y1 = top_left_pos
        brush = self.__verify_brush(brush, opacity)
        for y in range(y1, y1 + h):
            for x in range(x1, x1 + w):
                if self.__pos_in_canvas((x, y)):
                    self.canvas[y][x] = brush

    def draw_circle(self, pos, r, brush = '*', opacity = None):
        x1, y1 = pos
        brush = self.__verify_brush(brush, opacity)
        for y in range(self.h):
            for x in range(self.w):
                if round(((x - x1) ** 2 + (y - y1) ** 2) ** 0.5, 3) <= r and self.__pos_in_canvas((x, y)):
                    self.canvas[y][x] = brush

    def draw_triangle(self, p1, p2, p3, brush = '*', opacity = None):
        tl, br = self.__find_bounding_box(p1, p2, p3)
        min_x, max_y = tl
        max_x, min_y = br
        brush = self.__verify_brush(brush, opacity)
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                p = (x, y)
                if self.__point_in_triangle(p, p1, p2, p3) and self.__pos_in_canvas((x, y)):
                    self.canvas[y][x] = brush

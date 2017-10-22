from .base import Widget


class Context2D(Widget):
    def create(self):
        pass

    def save(self):
        pass

    def restore(self):
        pass

    def release(self):
        pass

    def line_width(self, width=2.0):
        pass

    def fill_style(self, color='None', r=0.0, b=0.0, g=0.0, a=1.0):
        pass

    def stroke_style(self, color='None', r=0.0, b=0.0, g=0.0, a=1.0):
        pass

    def begin_path(self):
        pass

    def close_path(self):
        pass

    def move_to(self, x, y):
        pass

    def line_to(self, x, y):
        pass

    def bezier_curve_to(self, cp1x, cp1y, cp2x, cp2y, x, y):
        pass

    def quadratic_curve_to(self, cpx, cpy, x, y):
        pass

    def arc(self, x, y, radius, startangle, endangle, anticlockwise):
        pass

    def ellipse(self, x, y, radiusx, radiusy, rotation, startangle, endangle, anticlockwise):
        pass

    def rect(self, x, y, width, height):
        pass

    # Drawing Paths

    def fill(self, fill_rule, preserve):
        pass

    def stroke(self):
        pass

    # Transformations

    def rotate(self, radians):
        pass

    def scale(self, sx, sy):
        pass

    def translate(self, tx, ty):
        pass

    def reset_transform(self):
        pass

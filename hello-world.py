from manim import *

class HelloWorld(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(1)  # Ensures rendering duration
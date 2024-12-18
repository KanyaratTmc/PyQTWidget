class MyClass:

    def __init__(self, name):
        self.name = name

    def greet(self):
        """แสดงคำทักทาย"""
        return f"สวัสดี, {self.name}!"

class MathOperations:

    def __init__(self,a,b):
        self.a = a 
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b
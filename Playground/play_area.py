import sys


print(sys.version)
print("hello world")


class TestClass(object):
    """docstring for TestClass"""

    def __init__(self):
        super(TestClass, self).__init__()

    def hello_world(self):
        print("Hello World")


foo = TestClass()
foo.hello_world()

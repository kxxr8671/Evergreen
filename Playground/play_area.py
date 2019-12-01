import sys
import datetime


print(sys.version)
print("version check 2")


class TestClass(object):
    """docstring for TestClass"""

    def __init__(self):
        super(TestClass, self).__init__()

    def hello_world(self):
        print(datetime.datetime.now().year)


foo = TestClass()
foo.hello_world()

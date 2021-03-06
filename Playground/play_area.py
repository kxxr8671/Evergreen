import sys
import datetime

class TestClass(object):
    """docstring for TestClass"""

    def __init__(self):
        super(TestClass, self).__init__()

    def hello_world(self):
        print(datetime.datetime.now().year)

    def __str__(self):
        return f"Running under Python {sys.version}"

print(TestClass())

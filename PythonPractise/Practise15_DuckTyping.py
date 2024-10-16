class PyCharm:
    def exe(self):
        print('compiling')
        print('executing')


class MyEditor:
    def exe(self):
        print('spell check')
        print('compiling')
        print('executing')


# whatever talks, walks , swims like a duck then it is a duck
# whatever has exe method, ide param below will take it
class Laptop:
    def code(self,ide):
        ide.exe()


ide = PyCharm()
ide2 = MyEditor()

Lap = Laptop()
Lap.code(ide)
Lap.code(ide2)
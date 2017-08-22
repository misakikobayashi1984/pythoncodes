#モジュール（.py）名、クラス名
from .moduleMain import moduleMain

class moludeFunc02(moduleMain):
    def __init__(self):
        super(moludeFunc02, self).__init__()
        
    def sub(self):
        result = self.x - self.y
        print('sub x - y: ', result)
    
if __name__ == '__main__':
    fnc02 = moludeFunc02()
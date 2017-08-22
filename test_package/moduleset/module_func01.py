#.はこのパッケージの相対パス　モジュール（.py）名、クラス名
from .moduleMain import moduleMain

class moludeFunc01(moduleMain):
    def __init__(self):
        super(moludeFunc01, self).__init__()
        print('x, y; ', self.x, self.y)
        
    def add(self):
        result = self.x + self.y
        print('Add x + y: ', result)
    
if __name__ == '__main__':
    fnc01 = moludeFunc01()
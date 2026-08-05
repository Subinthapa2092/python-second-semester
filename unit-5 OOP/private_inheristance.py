### Property Decorator 
class Personal:
    def __init__(self,public,_protected,__private):
        self.public = public 
        self._protected = _protected
        self.__private = __private

per = Personal("Public Data","Protected Data","Private Data")
print(per.public)
print(per._protected)
# print(per.__private)### private data can not be accessed directly 
print(dir(per))
# print(per.__Personal__private)
print(per._Personal__private)### private data can be accessed using this method
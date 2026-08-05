###### 
class GeometricIterator:
    def __iter__(self):
        self.summation = 0 
        self.k = 0 
        self.term = 1 
        self.cr = 1/3 
        return self 
    def __next__(self):
        gp = self.term *self.cr **self.k 
        self.summation = self.summation+gp 
        self.k = self.k +1 
        return gp,self.summation
gp1 = GeometricIterator()
gpiter = iter(gp1)
print(next(gpiter))
print(next(gpiter))
print(next(gpiter))
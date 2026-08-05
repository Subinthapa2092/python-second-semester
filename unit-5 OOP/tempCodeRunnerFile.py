#### Python in a program to  make itertor to print prime numbers upto 100

class PrimeNumbers:
    
    def __iter__(self):
        self.a = 2 
        return self 
    def __next__(self):
        if self.a <=100:
            for i in range(2,self.a):
                if self.a % i == 0:
                    break 
            else:
                x = self.a ### x values += 1 
                self.a += 1 
                return x 
            self.a += 1 
            return self.__next__()
        else:
            raise StopIteration 
primeobj = PrimeNumbers()
primIter = iter(primeobj)
print("Displaying the Prime Number Number ")
for i in primIter:
    print(i)
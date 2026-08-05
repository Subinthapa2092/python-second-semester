class EvenNumbers:
    def __iter__(self):
        self.a = 2 
        return self 
    def __next__(self):
        if self.a <=20:
            x = self.a 
            self.a += 2 
            return x 
        else:
            raise StopIteration 
evenobj = EvenNumbers()
evenIter = iter(evenobj)
print("The even numbers between 1 and 20 are folllows")
for x in evenIter:
    print(x)
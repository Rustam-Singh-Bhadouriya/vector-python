class vector():
    def __init__(self , value : list):
        self.vectorValue = value
    
    def size(self):
        length = len(self.vectorValue)
        return length

    def show(self , toPrint = None ):
        if toPrint == None:
            toPrint = self.vectorValue
            for items in toPrint:
                print(items , end=" ")
            print("\n")
        
        else:
            if type(toPrint) == int or type(toPrint) == float or type(toPrint) == str:
                print(toPrint)

            else:
                values = list(toPrint)
                for items in values:
                    print(items ,end=" " )
                print("\n")

            
    
    def font(self):
        return self.vectorValue[0]
    
    def back(self):
        return self.vectorValue[-1]
    
    def reverse(self):
        reversed_val = self.vectorValue.reverse()
        return reversed_val
    
    def push_back(self , pushBackValue : any):
        self.vectorValue.append(pushBackValue)
        return
    
    def pop_back(self):
        self.vectorValue.pop()
        return
    
    def pop(self , valueIndex = 0):
        self.vectorValue.pop(valueIndex)
        return
    
    def insert(self , Index , Value):
        self.vectorValue.insert(Index , Value)
        return
    
    def at(self , Index):
        return self.vectorValue[Index]
        
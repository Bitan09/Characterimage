from os import system

class charimage:
    def __init__(self,bg:str):
        if len(bg)!=1:
            raise ValueError("Argument must be only 1 character long")
        self.bg = bg
    def generate(self,height:int,width:int): #must be used atleast once before changing image
        if height <= 0 or width <= 0:
            raise ValueError("Height and width must be greater than 0")
        self.height = height
        self.width = width
        linelist = []
        for i in range(height):
            line = []
            for j in range(width):
                line.append(self.bg)
            linelist.append(line)
        self.imageline = linelist
        return linelist
    def __str__(self):
        s = ""
        for lines in self.imageline:
            for character in lines:
                s += character
            s += "\n"
        return s
    def show(self):
        xlen = len(str(self.width))
        ylen = len(str(self.height))
        print(" ",end=" "*ylen)
        for x in range(self.width):
            nxlen = len(str(x))
            print(x,end=" "*(xlen-nxlen+1))
        print()
        for y in range(self.height):
            nylen = len(str(y))
            print(y,end=" "*(ylen-nylen+1))
            for character in self.imageline[y]:
                print(character,end=" "*(xlen))
            print()
    def addcharacter(self,char:str,*positions): #positions must be given as (height,width)
        for i in positions:
            if i[0] >= self.height and i[1] >= self.width:
                raise ValueError("Argument must be lesser than image height and width")
        if len(char)!=1:
            raise ValueError("Argument must be only 1 character long")
        for i in positions:
            self.imageline[i[0]][i[1]] = char
        return self.imageline
    def changeline(self,char:str,direction:str,*lines):#lines must be given as line
        if len(char)!=1:
            raise ValueError("Argument must be only 1 character long")
        for i in lines:
            if direction.lower() == "x":
                if i >= self.height:
                    raise ValueError("Argument must be lesser than image height")
            elif direction.lower() == "y":
                if i >= self.width:
                    raise ValueError("Argument must be lesser than image width")
            else:
                raise ValueError("direction argument must be x or y")
        if direction.lower() == "x":
            for i in lines:
                for j in range(self.width):
                    self.imageline[i][j] = char
        else:
            for i in lines:
                for j in range(self.height):
                    self.imageline[j][i] = char
        return self.imageline

def clear():
    system('clear')

if __name__ == "__main__":
    clear()
    while True:
        bg = input("background character: ")
        if len(bg) == 1:break
        else:print("invalid input")
    generated = False
    img = charimage(bg)
    history = []
    while True:
        prompt = input("[Prompt]: ") 
        if prompt == "":continue
        elif prompt == "exit":break
        elif prompt == "print":print(img)
        elif prompt == "clear":clear()
        elif prompt == "history":[print(i) for i in history]
        elif "generate" in prompt:
            try:
                eval(f"img.{prompt}")
                generated=True
            except:print("!!!Invalid command!!!")
        else:
            if generated:
                try:eval(f"img.{prompt}") #characters must be given in quotes
                except:print("!!!Invalid command!!!")
            else:print("!!!Generate image first!!!")
        history.append(prompt)

from os import system

class charimage:
    def __init__(self,bg:str):
        if len(bg)!=1:
            raise ValueError("Argument must be only 1 character long")
        self.bg = bg
    def generate(self,height:int,width:int): #must be used atleast once before changing image
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
    def addcharacter(self,char:str,*positions): #positions must be given as (height,width)
        if len(char)!=1:
            raise ValueError("Argument must be only 1 character long")
        for i in positions:
            self.imageline[i[0]][i[1]] = char

def clear():
    system('clear')

if __name__ == "__main__":
    clear()
    while True:
        bg = input("background character: ")
        if len(bg) == 1:break
        else:print("invalid input")
    x = False
    img = charimage(bg)
    while True:
        prompt = input("[Prompt]: ")
        if prompt == "exit":break
        elif prompt == "print":print(img)
        elif prompt == "clear":clear()
        elif "generate" in prompt:
            try:
                eval(f"img.{prompt}")
                x=True
            except:print("!!!Invalid command!!!")
        else:
            if x:
                try:eval(f"img.{prompt}") #characters must be given in quotes
                except:print("!!!Invalid command!!!")
            else:print("!!!Generate image first!!!")

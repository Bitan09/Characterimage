from os import system

class charimage:
	def __init__(self,bg:str):
		if len(bg)!=1:
			raise ValueError("Parameter must be only 1 character long")
		self.bg = bg
	def generate(self,height:int,width:int):
		self.height = height
		self.width = width
		linelist = list()
		for i in range(height):
			line = []
			for i in range(width):
				line append(self.bg)
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
    def addcharacter(char:str,*positions):
        if len(char)!=1:
			raise ValueError("Parameter must be only 1 character long")
        for i in self.line:
            for j in positions:
                pass

def clear():
    system('clear')

if __name__ == "__main__":
	clear()
	while True:
		bg = input("background character: ")
		if len(bg) == 1 and len(fg) == 1:break
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
				try:eval(f"img.{prompt}")
				except:print()
			else:print("!!!Generate image first!!!")

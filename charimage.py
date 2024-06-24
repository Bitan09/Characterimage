from os import system

class charimage:
	def __init__(self,bg:str,fg:str):
		if len(bg)!=1 or len(fg)!=1:
			raise ValueError("Background character must be only 1 character long")
		self.bg = bg
		self.fg = fg
	def generate(self,height:int,width:int):
		self.height = height
		self.width = width
		linelist = list()
		for i in range(height):
			string = ""
			for i in range(width):
				string += self.bg
			linelist.append(string)
		self.line = linelist
		return linelist
	def __str__(self):
		s = ""
		for lines in self.line:
			s += lines +"\n"
		return s

def clear():
    system('clear')

if __name__ == "__main__":
	clear()
	while True:
		bg = input("background character: ")
		fg = input("foreground character: ")
		if len(bg) == 1 and len(fg) == 1:break
		else:print("invalid input")
	x = False
	img = charimage(bg,fg)
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

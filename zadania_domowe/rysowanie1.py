import turtle

def figury(n):
	for i in range(n):
		turtle.left(360/n)
		turtle.forward(100)

print(figury(9))




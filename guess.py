import random
s = input('猜數字遊戲起始數字: ')
s = int(s)
end = input('猜數字遊戲末端數字: ')
end = int(end)
r = random.randint(s, end)
n = 5 # 5次機會
print(r)
while n > 0:
	n = n -1
	num = input('請猜數字')
	num = int(num)
	if num > r:
		print('數字比答案大', n,'次機會')
	elif num < r:
		print('數字比答案小', n,'次機會')
	elif num == r:
		print('恭喜你猜對數字了')
		break
	
		
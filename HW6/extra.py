a , b = int(input('Введите а ')), int(input('Введите b '))
dic ={0:''}
dic[a//b]="a < b"
dic[b//a]="b < a"
dic[a-b]="a=b"
print(dic[0])
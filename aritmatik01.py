#operasi aritmatika

a = 20
b = 10

# penjumlahan +

hasil= a + b
print(a,'+',b,'=',hasil)

# pengurangan -

hasil= a - b
print(a,'-',b,'=',hasil)

# perkalian *

hasil= a*b
print(a,'*',b,'=',hasil)

# pembagian /

hasil= a / b
print(a,'/',b,'=',hasil)

# eksponen (pangkat) **

hasil= a**b
print(a,'**',b,'=',hasil)

# modulus (hasil pembagian) %

hasil= a%b 
print(a,'%',b,'=',hasil)

# floor division //

hasil= a//b
print(a,'//',b,'=',hasil)

#  prioritas operasi,operational presedence
'''
#urutan prioritas
1.() OP
2.**
3.*,/,%,//
4.+,-

'''
x=4
y=6
z=5

hasil= y ** z + z / x - z**y + z%x
print (y,'**',z,'+',z,'/',x,'-',z,'**',y,'+',z,'%',x, '=',hasil)

hasil= z + y * y - x * z ** y + z // x * y % x
print (z,'+',y,'*',y,'-',x,'*',z,'**',y,'+',z,'//',x,'*',y,'%',x, '=',hasil)
   
hasil= z + y * x * z / y ** x % y + z 
print ( z,'+',y,'*',x,'*',z,'/',y,'**',x,'%',y,'+',z ,'=',hasil),


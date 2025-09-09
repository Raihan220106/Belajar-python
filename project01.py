#a=10, a adalah variabel dengan nilai 10 

#tipe fata : angka satuan (integer)
data_integer= 100000
print("data :",data_integer)
print("-bertipe: ", type(data_integer))

#Tipe data: angka dengan koma (float)
data_float= 1.5
print("data :" ,data_float)
print("-bertipe: ", type(data_float))

#Tipe data : kumpulan karakter (string)
data_string= "Raihan"
print("data :" ,data_string)
print("-bertipe: ", type(data_string))

#Tipe data : Biner true/false (boolean)
data_bool= False
print("data :" ,data_bool)
print("-bertipe: ", type(data_bool))

###Tipe Data Khusus###


#Bilangan Kompleks
data_complex=complex(5.6)
print("data :" ,data_complex)
print("-bertipe: ", type(data_complex))


#Tipe Data dari Bahasa C
from ctypes import c_double

data_c_double= c_double(20.10)
print("data :" ,data_c_double)
print("-bertipe: ", type(data_c_double))

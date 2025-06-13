# type casting

x = 10 # int
y = 2.5 # float

# Aqui o python realiza o casting automaticamente(quando é seguro)
resultado = x + y
print(resultado)
print(type(resultado)) # <class 'float'>

# str -> int 
numero = int("10")
print(numero, type(numero))

# int → str
texto = str(123)
print(texto, type(texto))  # "123" <class 'str'>

# float → int (trunca, não arredonda!)
# Trunca é para remover a parte decimal
print(int(3.99))  # 3

# int → float
print(float(3))  # 3.0

# qualquer valor → bool
print(bool(0))     # False
print(bool(123))   # True
print(bool(""))    # False
print(bool("abc")) # True

# Nem sempre a conversão cai acontecer

int("abc")  # ValueError!

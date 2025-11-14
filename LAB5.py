#1
a= input("Введите имя:").strip()
if any(b.isalnum() for b in a):
    a = a.lower()
    print("Имя корректно: ",a)
else:
    print("Ошибка")
#2
a = input("Введите пароль: ")
if len(a) > 8:
    if any(cifra.isdigit() for cifra in a):
        if any(BUKVA.isupper() for BUKVA in a):
            print("Пароль надежен")
        else:
            print("Пароль слаб")
    else:
        print("Пароль слаб")
else:
    print("Пароль слаб")
#3
login="ACCESS DENIED"
a ="- вход запрещен"
login =str.capitalize(login)
print(login+a)
#4
data = "ERROR connection ERROR failed access"
updated_data = data.replace("ERROR", "ALERT")
alert_count = updated_data.count("ALERT")
print(updated_data)
print(alert_count)
#5
a = input("Введите електронный адрес: ")
if a.find("@") != -1 :
    b = a.split("@")
    if a.endswith(".com"):
        print("Домен:", b[1])
    else:
        print("Некорректный адрес")
else:
    print("Некорректный адрес")
#6
a = input("Введите текст: ").lower().strip(" ").replace(" ", "_")
print(a)
#7
a = input("Введите текст: ")
if a.find("SECRET") != -1:
    b = a.replace("SECRET","******")
    print(b,"Предупреждение")
else:
    print("Cообщение о безопасности")
#8
word = input("Введите слово: ")
codes = ""
for ch in word:
    codes += str(ord(ch)) + " "
print("Коды символов:", codes)
restored = ""
for code in codes.split():
    restored += chr(int(code))
print("Восстановленная строка:", restored)
#9
text = "login attempt failed access denied unauthorized access"
a = text.count("failed")
b = text.count("denied")
if a != -1 and b != -1:
    print("Попытка несанкционированного доступа")
#10
a = input("Введите отчет: ").lower()
b = len(a.split("."))
print(b)
c = a.strip()
d = len(c)
print(d)
if a.startswith("report"):
    print("Начинаетcя с 'report'")
if a.count("erorr") >= 2:
    print("Ошибки найдены")
else:
    print("Ошибки не найдены")
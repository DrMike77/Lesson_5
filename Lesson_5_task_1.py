a = open("output.txt", "w")
b = []
while True:
     b = input("Введите строку: ")
     if not b:
          break
     a.write(f"{b}\n")
else: a.close()
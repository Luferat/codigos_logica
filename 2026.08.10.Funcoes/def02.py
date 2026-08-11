def fahrenheit_to_celsius():
  fahrenheit = input("Digite a temperatura em °F ou 'FIM' para sair: ") 
  if fahrenheit.upper() == "FIM":
    exit()
  print((float(fahrenheit) - 32) * 5 / 9)

# "Main loop"
while True:
    # A função sem "return" devolve "None"
    print(fahrenheit_to_celsius())
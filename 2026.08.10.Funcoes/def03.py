def fahrenheit_to_celsius(fahrenheit):
  c = (fahrenheit - 32) * 5 / 9
  return c
  print("Acabou") # Inútil por causa do "return"

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

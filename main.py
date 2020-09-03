temperature = input("Enter temperature: ")
temperatureChoice = input("Enter unit in F/f or C/c: ")
temperatureFloat = float(temperature)

if (temperatureChoice == "F" or temperatureChoice == "f"):
  celsius = (temperatureFloat - 32) * (5/9)
  print(f"{temperatureFloat}° in Fahrenheit is equivalent to {celsius}° Celsius.")
elif (temperatureChoice == "C" or temperatureChoice == "c"):
  fahrenheit = temperatureFloat * (9/5) + 32
  print(f"{temperatureFloat}° in Celsius is equivalent to {fahrenheit}° Fahrenheit.")
else:
  print(f"Invalid unit({temperatureChoice}")
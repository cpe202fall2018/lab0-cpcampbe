def weight_on_planets():
   weight = input("What do you weigh on earth? ")
   intWeight = int(weight)
   print ("\nOn Mars you would weigh", intWeight * .38,
          "pounds.\nOn Jupiter you would weigh", intWeight * 2.34, "pounds.")
if __name__ == '__main__':
   weight_on_planets()

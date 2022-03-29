from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee = "cappuccino"


profit = 0
def checker(coffee):
  '''
  Check if the resource is sufficient
  '''

  Water = MENU[coffee]["ingredients"]["water"]
  Milk = MENU[coffee]["ingredients"]["milk"]
  Coffee = MENU[coffee]["ingredients"]["coffee"]

  rem_Water = resources["water"]
  rem_Milk = resources["milk"]
  rem_Coffee = resources["coffee"]

  if Water > rem_Water:
    print("Sorry there is no enough water 😮.")
   
  if Milk > rem_Milk:
    print("Sorry there is no enough milk 🥛.")
   
  if Coffee > rem_Coffee:
    print("Sorry there is no enough coffee 😣.")


def money_process():
  '''
  Ask customer to pay in coins.
  '''
  QQ = int(input("How many quarters(0.25)? "))
  DD = int(input("How many dimes(0.1)? "))
  NN = int(input("How many nickels(0.05)? "))
  PP = int(input("How many pennys(0.01)? "))
  total_payment = QQ*0.25 + DD*0.1 + NN*0.05 + PP*0.01
  return total_payment

def money_checking(coffee,the_total_payment):
  '''
  Checking if payment is enough and machine need to return change or not.
  '''
  coffee_cost = MENU[coffee]["cost"]
  if coffee_cost > the_total_payment:
    print("Sorry that is not enough money. Money refund 🪙🪙🪙 ")
  else:
    global profit
    profit += coffee_cost
    return_change = the_total_payment - coffee_cost
    if return_change > 0:
      print(f"Here is ${return_change} in change.💰 ")


def make_coffee(coffee):
  '''
  Make the coffee
  '''
  Water = MENU[coffee]["ingredients"]["water"]
  Milk = MENU[coffee]["ingredients"]["milk"]
  Coffee = MENU[coffee]["ingredients"]["coffee"]

  rem_Water = resources["water"]
  rem_Milk = resources["milk"]
  rem_Coffee = resources["coffee"]

  res_Water = rem_Water - Water
  res_Milk = rem_Milk - Milk
  res_Coffee = rem_Coffee - Coffee

  resources_new = {
    "water": res_Water,
    "milk": res_Milk,
    "coffee": res_Coffee,
  }
 
  return resources_new


def coffee_machine():
  print(logo)
  global resources, profit
  is_on = True
  while is_on:
    coffee = input("What would you like (espresso/latte/cappuccino)? ☕☕☕ ").lower()
    if coffee in ("latte", "cappuccino", "espresso"): 
      checker(coffee)
      money_checking(coffee,money_process())
      
      resources = make_coffee(coffee)
    elif coffee == "report": 
      Water = resources["water"]
      Milk = resources["milk"]
      Coffee = resources["coffee"]
      Money = profit
      print(f"Water: {Water}ml \nMilk: {Milk}ml \nCoffee: {Coffee}g \nMoney: ${Money}")
    elif coffee == "off":
      is_on = False


coffee_machine()  
  

  
from replit import clear
from art import logo

print(logo)

bids = {}

name = input("Enter your name: ")
bid = int(input("Enter you bid price: $"))

#Adding name, bid to dictionary
bids[name] = bid

response = input("Are there any other bidders? Type 'yes' or 'no': ")

while response == "yes":
  # clear()
  name = input("Enter your name: ")
  bid = int(input("Enter your bid price: $"))

  # Adding name, bid to dictionary
  bids[name] = bid
  response = input("Are there any other bidders? Type 'yes' or 'no': ")

highest_bid = 0
winner = ""
for bidder in bids:
  if bids[bidder] > highest_bid:
    highest_bid = bids[bidder]
    winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}")

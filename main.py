import art
print(art.logo)
print("Welcome to the secret auction program")

check = 'yes'

dic = {}


def add_new(n, b):
    dic[n] = b


while check != 'no':
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    check = input("Are there any other bidders? Type 'yes' or 'no'.")
    add_new(name, bid)


# max_val = max(zip(dic.values(), dic.keys()))[1]
def find_highest_bidder(dic):
    highest_bid = 0
    winner = ""
    for i in dic:
        bid_amount = dic[i]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = i
    print(f"The winner is {winner} with a bid of ${highest_bid}")


find_highest_bidder(dic)


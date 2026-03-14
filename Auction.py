users = []
items = []

# ---------- FILE FUNCTIONS ----------

def save_data():
    file = open("auction_data.txt", "w")

    for user in users:
        file.write(f"USER,{user['id']},{user['name']}\n")

    for item in items:
        file.write(f"ITEM,{item['id']},{item['name']},{item['highest_bid']},{item['bidder']}\n")

    file.close()


def load_data():
    try:
        file = open("auction_data.txt", "r")

        for line in file:
            data = line.strip().split(",")

            if data[0] == "USER":
                users.append({
                    "id": int(data[1]),
                    "name": data[2]
                })

            elif data[0] == "ITEM":
                items.append({
                    "id": int(data[1]),
                    "name": data[2],
                    "highest_bid": float(data[3]),
                    "bidder": data[4] if data[4] != "None" else None
                })

        file.close()

    except FileNotFoundError:
        pass


# ---------- AUCTION FUNCTIONS ----------

def add_user():
    name = input("Enter user name: ")
    user = {"id": len(users)+1, "name": name}
    users.append(user)
    save_data()
    print("User added!")


def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter starting price: "))

    item = {
        "id": len(items)+1,
        "name": name,
        "highest_bid": price,
        "bidder": None
    }

    items.append(item)
    save_data()
    print("Item added!")


def view_items():
    print("\nItems:")
    for item in items:
        print(item)


def place_bid():
    user_id = int(input("Enter user id: "))
    item_id = int(input("Enter item id: "))
    amount = float(input("Enter bid amount: "))

    item = items[item_id-1]

    if amount > item["highest_bid"]:
        item["highest_bid"] = amount
        item["bidder"] = users[user_id-1]["name"]
        save_data()
        print("Bid placed!")
    else:
        print("Bid must be higher!")


def close_auction():
    item_id = int(input("Enter item id: "))
    item = items[item_id-1]

    print("\nAuction Closed")
    print("Winner:", item["bidder"])
    print("Winning Bid:", item["highest_bid"])


# ---------- MAIN PROGRAM ----------

load_data()

while True:

    print("\n1 Add User")
    print("2 Add Item")
    print("3 View Items")
    print("4 Place Bid")
    print("5 Close Auction")
    print("6 Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_user()

    elif choice == "2":
        add_item()

    elif choice == "3":
        view_items()

    elif choice == "4":
        place_bid()

    elif choice == "5":
        close_auction()

    elif choice == "6":
        print("Program closed")
        break
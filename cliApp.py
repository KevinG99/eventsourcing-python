import requests

BASE_URL = "http://localhost:8000"

def create_item():
    name = input("Enter the name of the item: ")
    response = requests.post(f"{BASE_URL}/items/", json={"name": name})
    if response.status_code == 200:
        print(f"Item created with ID: {response.json()['item_id']}")
    else:
        print(f"Error: {response.text}")

def modify_item():
    item_id = input("Enter the ID of the item to modify: ")
    new_name = input("Enter the new name of the item: ")
    response = requests.put(f"{BASE_URL}/items/", json={"item_id": item_id, "new_name": new_name})
    if response.status_code == 200:
        print(f"Item with ID {item_id} modified.")
    else:
        print(f"Error: {response.text}")

def get_items():
    response = requests.get(f"{BASE_URL}/items/")
    if response.status_code == 200:
        print("Items:", response.json()["items"])
    else:
        print(f"Error: {response.text}")

def get_modification_count():
    item_id = input("Enter the ID of the item: ")
    response = requests.get(f"{BASE_URL}/analytics/{item_id}/modification_count")
    if response.status_code == 200:
        print(f"Modification count for item {item_id}: {response.json()['modification_count']}")
    else:
        print(f"Error: {response.text}")

def get_modification_history():
    item_id = input("Enter the ID of the item: ")
    response = requests.get(f"{BASE_URL}/analytics/{item_id}/modification_history")
    if response.status_code == 200:
        print(f"Modification history for item {item_id}: {response.json()['modification_history']}")
    else:
        print(f"Error: {response.text}")

def get_item_history():
    item_id = input("Enter the ID of the item: ")
    response = requests.get(f"{BASE_URL}/history/{item_id}")
    if response.status_code == 200:
        print(f"History for item {item_id}: {response.json()['history']}")
    else:
        print(f"Error: {response.text}")

def compare_histories():
    item_id = input("Enter the ID of the item: ")
    response = requests.get(f"{BASE_URL}/history/{item_id}/comparison")
    if response.status_code == 200:
        print(f"Comparison of histories for item {item_id}: {response.json()['comparison']}")
    else:
        print(f"Error: {response.text}")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Create a new item")
        print("2. Modify an existing item")
        print("3. Get all items")
        print("4. Get modification count of an item")
        print("5. Get modification history of an item")
        print("6. Get history of an item")
        print("7. Compare histories of an item")
        print("8. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            create_item()
        elif choice == "2":
            modify_item()
        elif choice == "3":
            get_items()
        elif choice == "4":
            get_modification_count()
        elif choice == "5":
            get_modification_history()
        elif choice == "6":
            get_item_history()
        elif choice == "7":
            compare_histories()
        elif choice == "8":
            print("Exiting the CLI.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()

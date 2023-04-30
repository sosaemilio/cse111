def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list.reverse()
    print(f"Reverse: {fruit_list}")

    fruit_list.append("orange")
    print(f"Append Orange: {fruit_list}")

    fruit_list.insert(fruit_list.index("apple"), "cherry")
    print(f"Insert Cherry: {fruit_list}")

    fruit_list.remove("banana")
    print(f"Remove Banana: {fruit_list}")
    
    fruit_list.pop()
    print(f"Pop last element: {fruit_list}")

    fruit_list.sort()
    print(f"Sorted: {fruit_list}")

    fruit_list.clear()
    print(f"Clear: {fruit_list}")

if __name__ == "__main__":
    main()
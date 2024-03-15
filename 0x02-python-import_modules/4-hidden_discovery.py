#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    args = dir(hidden_4)
    # Sorting and filtering
    sorted_list = sorted([item for item in args if not item.startswith('_')])

    # Printing the sorted list
    print(sorted_list)

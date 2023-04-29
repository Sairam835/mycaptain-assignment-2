def most_frequent(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    for char, freq in sorted_frequency:
        print(f"{char} = {freq:02}")
string = input("Please enter a string\n")
most_frequent(string)

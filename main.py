
from Program1 import *
from Program2 import Square

def main():
    text = './files/profram1_file.txt'
    frequencies = compute_word_frequency_from_file(text)
    for i in frequencies.items():
        print(i)
    print(frequencies)

    square = Square(4)
    print(square.area())
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

import threading
from Program1 import *
from Program2 import Square

def main():
    text = './files/profram1_file.txt'
    thread1 = threading.Thread(target=compute_word_frequency_from_file, args=(text,))
    square = Square(4)
    thread2 = threading.Thread(target=square.area)

    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

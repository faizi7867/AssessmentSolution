def compute_word_frequency(text):
    data = text.split(' ')
    d = {}

    for i in data:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    sorted_data = dict(sorted(d.items()))
    for i in sorted_data.items():
        print(i)

def compute_word_frequency_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return compute_word_frequency(text)

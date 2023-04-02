def add_text(filepath, insert_text, index_number):
    f = open(filepath, "r")
    line_index = index_number
    lines = None
    lines = f.readlines()
    lines.insert(line_index, insert_text)
    f = open(filepath, 'w')
    f.writelines(lines)
    f.close()


def replace(filepath, find_text, replace_text):
    # read input file
    fin = open(filepath, "rt")
    # read file contents to string
    data = fin.read()
    # replace all occurrences of the required string
    data = data.replace(find_text, replace_text)
    # close the input file
    fin.close()
    # open the input file in write mode
    fin = open(filepath, "wt")
    # overrite the input file with the resulting data
    fin.write(data)
    # close the file
    fin.close()
    return fin

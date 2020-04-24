def rail_cypher_fence(text, rail_key):
    n = len(text)
    letters_in_one_cycle = 2 * rail_key - 2
    cycle = n / (2 * rail_key - 2)
    columns = n
    float_cycle = cycle - int(cycle)    # value of partial cycle
    # a full cycle has length equal to letters_in_one_cycle
    # each cycle has two phases: upward and downward

    # fence: table for assigning letters
    # Adding place holders in the fence
    fence = [[] for i in range(rail_key)]
    for i in range(rail_key):
        fence[i] = ["" for j in range(columns)]

    # Assigning letters in fence
    for i in range(rail_key):
        j = i  # column no.
        while j < columns:  # filling the downward  part of cycle
            fence[i][j] = text[j]
            j += letters_in_one_cycle
        if i != 0 and i != rail_key:  # filling the upward part of cycle between first and last row
            j = j - letters_in_one_cycle
            j = j - 2 * i
            while j > (rail_key - 1):
                fence[i][j] = text[j]
                j -= letters_in_one_cycle

    if float_cycle >= 0 and float_cycle != 0.5:  # filling partial cycles
        if float_cycle > 0.5:  # partial upward cycle
            residue_num = n - int(
                cycle) * letters_in_one_cycle - rail_key  # no of letters left after fillilg full cycles
            j = n - residue_num  # The  index of letter in string to start assigning from
        elif float_cycle == 0:  # no partial cycle
            residue_num = letters_in_one_cycle - rail_key
            j = n - residue_num  # The  index of letter in string to start assigning from
        elif 0 < float_cycle < 0.5:  # for the  upward cycle in the last full cycle
            residue_num = int((letters_in_one_cycle + 2) * 0.5 - int(float_cycle * letters_in_one_cycle)) - 1
            j = n - residue_num - int(2 * (cycle - int(
                cycle)) * letters_in_one_cycle - 1)  # The  index of letter in string to start assigning from
        letters = 0
        row_list = [num + 1 for num in range(rail_key - 2)][::-1]
        for i in row_list:
            if letters < residue_num and j > 0:
                fence[i][j] = text[j]
                j = j + 1
                letters += 1
            else:
                break
    return fence


def encode(text, rail_key):
    """
    Takes the letters from text and fills them into a table of rail_key rows (here rail_keys=3) :
    text=Hello World

    H . . . O . . . R . . .
    . E . L .   . O . L . !
    . . L . . . W . . . D .

    returns the encoded string  HOREL OL!LWD
    where the letters are read row wise.
    """
    fence1 = rail_cypher_fence(text, rail_key)

    encoded_text = ""
    for row in fence1:  # joining the items in the fence list as a string
        for values in row:
            if values != "":
                encoded_text = encoded_text + values
    return encoded_text


def decode(encoded_text, rail_key):
    """
       Converts the encoded text into readable output.
       """
    text = "-" * len(encoded_text)
    fence2 = rail_cypher_fence(text, rail_key)  # constructing a fence with placeholder "-" for each letter in the
    # encoded_text

    str_index = 0  # Index of letters in encoded_text
    for i in range(len(fence2)):  # replacing "-" to etters from encoded_text
        for j in range(len(fence2[i])):
            if fence2[i][j] == "-":
                fence2[i][j] = encoded_text[str_index]
                str_index += 1

    fence2 = [[row[i] for row in fence2] for i in range(len(fence2[0]))]  # tranposing the list of lists

    decoded_text = ""
    for i in fence2:  # arranging the letters to be readable string
        for j in i:
            if j != "":
                decoded_text += j
    return decoded_text




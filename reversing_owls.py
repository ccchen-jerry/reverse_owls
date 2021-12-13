input_string="apple"

def reversed_owls(input_string="apple"):
    string_list = list(input_string)
    
    owl_list = list()
    none_owl = list()
    for letter in input_string:
        if letter in "aeiou":
            owl_list.append(letter)
        else:
            none_owl.append(letter)
    
    owl_position = list()
    for owl in owl_list:
        owl_position.append(input_string.index(owl))

    print(owl_position)
    print(owl_list[::-1])
    print(none_owl)
    
    return owl_position, owl_list[::-1], none_owl

reversed_owls(input_string="apple")

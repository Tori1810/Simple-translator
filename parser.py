from lexer import*
from tree import *

error_table={"Wrong delimiter":-1, "Wrong key_word":-2, "No such identifier":-3, "Wrong integer":-4}

lex_list=lexer("TEST.txt")
tree = Tree()

def scan(dictionary, value):
    for key, v in dictionary.items():
        if v == value:
            return key

def err(err_number):
    tree.add(err_number)
    tree.current_element = tree.current_element.parent_element
    tree.print_tree()
    print(scan(error_table, err_number))
    quit()
    
def statement_list_proc(i):
    tree.add('statement-list')
    # tree.add('statement')
    # lexem = lex_list[i]
    # identifier_proc(lexem)
    # i+=1
    # lexem = lex_list[i]
    # if lexem == 40:
    #     tree.add(scan(simple_separetors_dic, lexem))
    #     tree.current_element = tree.current_element.parent_element
    # else:
    #     err(-1)
    # i+=1
    # lexem = lex_list[i]
    # while lexem!= 41:
    #     identifier_proc(lexem)
    #     i+=1
    #     lexem = lex_list[i]
    #     if lexem == 44:
    #         tree.add(scan(simple_separetors_dic, lexem))
    #         tree.current_element = tree.current_element.parent_element
    #         i+=1
    #         lexem = lex_list[i]
    #     elif lexem == 41:
    #         i+=1
    #         lexem = lex_list[i]
    #         break
    #     else:
    #         err(-2)

    # tree.add(scan(simple_separetors_dic, lexem))
    # tree.current_element = tree.current_element.parent_element



    lexem=lex_list[i]
    if lexem==403:
        tree.add('empty')
        tree.current_element = tree.current_element.parent_element
    else:
        err(-2)
    tree.current_element = tree.current_element.parent_element
    # i+=1
    return i
    
def block_proc(i):
    tree.add('block')
    lexem=lex_list[i]
    if lexem==402:
        tree.add(scan(key_words_dic, lexem))
        tree.current_element = tree.current_element.parent_element
    else:
        err(-2)
    i+=1
    i=statement_list_proc(i)
    lexem=lex_list[i]
    if lexem==403:
        tree.add(scan(key_words_dic, lexem))
        tree.current_element = tree.current_element.parent_element
    else:
        err(-2)
    tree.current_element = tree.current_element.parent_element
    return i;

def identifier_proc(lexem):
    tree.add('procedure-identifier')
    tree.add('identifier')
    if lexem>=1000:
        tree.add(scan(identificators_dic, lexem))
        tree.current_element = tree.current_element.parent_element
    else:
        err(-3)
    tree.current_element = tree.current_element.parent_element
    tree.current_element = tree.current_element.parent_element

def attributes_list_proc(i):
    tree.add('attributes-list')
    lexem=lex_list[i]
    while lexem in range(405,411):
        tree.add('attribute')
        tree.add(scan(key_words_dic, lexem))
        tree.current_element = tree.current_element.parent_element
        tree.current_element = tree.current_element.parent_element
        i+=1
        lexem=lex_list[i]
    tree.current_element = tree.current_element.parent_element
    return i
        
def identifiers_list_proc(i):
    tree.add('identifiers-list')
    lexem=lex_list[i]
    while lexem>=1000:
        tree.add('variable-identifier')
        tree.add('identifier')
        tree.add(scan(identificators_dic, lexem))
        tree.current_element = tree.current_element.parent_element
        tree.current_element = tree.current_element.parent_element
        tree.current_element = tree.current_element.parent_element
        i+=1
        lexem=lex_list[i]
        if lexem == 44:
            tree.add(scan(simple_separetors_dic, lexem))
            tree.current_element = tree.current_element.parent_element
        else:
            if lexem== 58:
                break
            else:
                err(-1)
        i+=1
        lexem = lex_list[i]
    tree.current_element = tree.current_element.parent_element
    return i

def declaration_proc(i):
    tree.add('declaration')
    lexem=lex_list[i]
    # if lexem==411:
    #     tree.add(scan(key_words_dic, lexem))
    #     tree.current_element = tree.current_element.parent_element
    #     i+=1
    #     lexem=lex_list[i]
    #     while lexem!=59:
    #         if lexem in range(500, 600):
    #             tree.add("unsigned-integer")
    #             tree.add(scan(digits_dic, lexem))
    #             tree.current_element = tree.current_element.parent_element
    #             tree.current_element = tree.current_element.parent_element
    #             i+=1
    #             lexem=lex_list[i]
    #             if lexem==44:
    #                 tree.add(scan(simple_separetors_dic, lexem))
    #                 tree.current_element = tree.current_element.parent_element
    #                 i+=1
    #                 lexem=lex_list[i]
    #             elif lexem==59:
    #                 tree.add(scan(simple_separetors_dic, lexem))
    #                 tree.current_element = tree.current_element.parent_element
    #                 i+=1
    #                 break
    #             else:
    #                 err(-1)
    #         else:
    #             tree.add("unsigned-integer")
    #             err(-4)
    #             tree.current_element = tree.current_element.parent_element
    #             i+=2
    #             lexem=lex_list[i]
    #             continue;
        
        
    if lexem!=411:
        i=identifiers_list_proc(i)
        lexem=lex_list[i]
        if lexem==58:
            tree.add(scan(simple_separetors_dic, lexem))
            tree.current_element = tree.current_element.parent_element
        else:
            err(-1)
        i+=1
        i=attributes_list_proc(i)
        lexem=lex_list[i]
        if lexem==59:
            tree.add(scan(simple_separetors_dic, lexem))
            tree.current_element = tree.current_element.parent_element
            i+=1
        else:
            err(-1)
    tree.current_element = tree.current_element.parent_element
    return i
       
def declaration_list_proc(i):
    tree.add('declaration-list')
    lexem=lex_list[i]
    while lexem!=41:
        i=declaration_proc(i)
        lexem=lex_list[i]
        print(lexem)
    tree.current_element = tree.current_element.parent_element
    return i

def parameters_list_proc(i):
    tree.add('parameters-list')
    lexem=lex_list[i]
    if lexem==40:
        tree.add(scan(simple_separetors_dic, lexem))
        tree.current_element = tree.current_element.parent_element
    else:
        err(-1)
    i+=1
    i=declaration_list_proc(i)
    lexem=lex_list[i]
    if lexem==41:
        tree.add(scan(simple_separetors_dic, lexem))
        tree.current_element = tree.current_element.parent_element
    else:
        err(-1)
    tree.current_element = tree.current_element.parent_element
    return i
    
def program_proc():
    tree.add('program')
    i=0
    lexem=lex_list[i]
    if lexem==401:
        tree.add(scan(key_words_dic, lexem))
        tree.current_element = tree.current_element.parent_element
        i+=1
        lexem=lex_list[i]
        identifier_proc(lexem);
        i+=1
        lexem=lex_list[i]
        if lexem==59:
            tree.add(scan(simple_separetors_dic, lexem))
            tree.current_element = tree.current_element.parent_element
        else:
            err(-1)
        i+=1
        i=block_proc(i)
        i+=1
        lexem=lex_list[i]
        if lexem==46:
            tree.add(scan(simple_separetors_dic, lexem))
            tree.current_element = tree.current_element.parent_element
        else:
            err(-1)
        i+=1
        lexem=lex_list[i]
        
    if lexem==404:
        tree.add(scan(key_words_dic, lexem))
        tree.current_element = tree.current_element.parent_element
        i+=1
        lexem=lex_list[i]
        identifier_proc(lexem)
        i+=1
        i=parameters_list_proc(i)
        i+=1
        lexem=lex_list[i]
        if lexem==59:
            tree.add(scan(simple_separetors_dic, lexem))
            tree.current_element = tree.current_element.parent_element
        else:
            err(-1)
        i+=1
        i = block_proc(i)
        i+=1
        lexem=lex_list[i]
        # if lexem==402:
        #     tree.add(scan(key_words_dic, lexem))
        #     tree.current_element = tree.current_element.parent_element
        # else:
        #     err(-2)
        # i+=1
        # lexem=lex_list[i]
        # if lexem==403:
        #     tree.add(scan(key_words_dic, lexem))
        #     tree.current_element = tree.current_element.parent_element
        # else:
        # #     err(-2)
        # tree.current_element = tree.current_element.parent_element
        # i+=1
        # lexem=lex_list[i]
        if lexem==59:
            tree.add(scan(simple_separetors_dic, lexem))
            tree.current_element = tree.current_element.parent_element
        else:
            err(-1)
    else:
        err(-2)

def signal_program_proc():
    if lex_list:
        program_proc()
        print(lex_list)
        tree.print_tree()
        print()
        print(error_table)
        print()
        tree.listing()
    return tree
        
if __name__ == '__main__':
    print(lex_list)
    signal_program_proc()
    

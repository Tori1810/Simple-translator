key_words_dic = {"PROGRAM": 401, "BEGIN": 402, "END":403, "PROCEDURE": 404,
             "SIGNAL": 405, "COMPLEX": 406, "INTEGER": 407, "FLOAT": 408,
             "BLOCKFLOAT": 409, "EXT": 410}
simple_separetors_dic={";":59, ".":46, ":":58, ",":44, "(":40, ")":41} 
identificators_dic={}
digits_dic={}

def lexer(file_name):
    white_space=[32, 13, 10, 9, 11, 12]
    digits=[i for i in range(48,57)]
    chars=[i for i in range(65, 90)]
    simple_separetors = [i for i in simple_separetors_dic.keys()]
    key_words = [i for i in key_words_dic.keys()]
    line=''
    lex_list=[]
    counter_identificators=1001
    counter_digits=501
    line_counter=1

    file=open(file_name)
    ch=file.read(1)
    while ch:
        if ch=="\n":
            line_counter+=1
        
        if ord(ch) in white_space:
            ch=file.read(1)
            
        elif ord(ch) in chars:
            line+=ch
            ch=file.read(1)
            while ch and ( ord(ch) in chars or ord(ch) in digits):
                line+=ch
                ch=file.read(1)
            if line!='':
                if line in key_words:
                    lex_list.append(key_words_dic[line])
                    line=''
                else:
                    if line in identificators_dic.keys():
                        lex_list.append(identificators_dic[line])
                        line = ''
                    else:
                        identificators_dic[line] = counter_identificators
                        lex_list.append(counter_identificators)
                        counter_identificators += 1
                        line = ''
                        
        # elif ord(ch) in digits:
        #     line+=ch
        #     ch=file.read(1)
        #     while ch in digits:
        #         line+=ch
        #         ch=file.read(1)
        #     if line in digits_dic.keys():
        #         lex_list.append(digits_dic[line])
        #     else:
        #         digits_dic[line] = counter_digits
        #         lex_list.append(counter_digits)
        #         counter_digits += 1
        #     line = ''

                       
        elif ch in simple_separetors:
            line=ch
            ch=file.read(1)
            if ch=='*':
                flag_comment=0
                ch=file.read(1)
                while ch:
                    if ch=='*':
                        ch=file.read(1)
                        if ch==')':
                            ch=file.read(1)
                            flag_comment=1
                            break;
                    else:
                        ch=file.read(1)
                    if ch=="\n":
                        line_counter+=1
                if flag_comment==0:
                    print("uncloset comment")
                    lex_list=[]
                    break
            else:
                lex_list.append(simple_separetors_dic[line])
            line=''
                
                    
        else:
            print("Lexical error at line " + str(line_counter))
            lex_list=[]
            break
            ch=file.read(1)

        
    file.close()
    #print(key_words_dic)
    #print(" ")
    #print(simple_separetors_dic)
    #print(" ")
    #print(identificators_dic)
    #print(" ")
    #print(lex_list)
    return lex_list

#if __name__ == '__main__':
    #lexer("TEST.txt")
    
            
        
                
            

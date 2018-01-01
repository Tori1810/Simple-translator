from parser import signal_program_proc


global proc_identifier
global key
global count_proc_identifier
global count_var_identifier
global wrong_identifier
global var_identifier
wrong_identifier = []
proc_identifier = []
var_identifier = []
key = []
count_proc_identifier = 0
count_var_identifier = 0


def var_proc(node):
	if (node.val == "variable-identifier"):
		ident = node.leaves[0].leaves[0].val
		if (ident in proc_identifier or ident in var_identifier):
			wrong_identifier.append(ident)
		var_identifier.append(ident)

	for i in range(len(node.leaves)):
		var_proc(node.leaves[i])
	return var_identifier



def kompile(fname):
	global proc_identifier
	global wrong_identifier
	global count_proc_identifier
	global count_var_identifier
	global key
	global var_identifier

	tree = signal_program_proc()
	for i in range(0, len(tree.root.leaves[0].leaves)):
		if (tree.root.leaves[0].leaves[i].val == "procedure-identifier"):
			ident = tree.root.leaves[0].leaves[i].leaves[0].leaves[0].val
			if (ident in proc_identifier):
				wrong_identifier.append(ident)
			proc_identifier.append(tree.root.leaves[0].leaves[i].leaves[0].leaves[0].val)

		if (tree.root.leaves[0].leaves[i].val == "PROGRAM" or tree.root.leaves[0].leaves[i].val == "PROCEDURE"):
			key.append(tree.root.leaves[0].leaves[i].val)

	var_identifier = var_proc(tree.root)
	print("\n\n====================CODE=========================")
	generator(tree.root)

def generator(node):
	global proc_identifier
	global var_identifier
	global count_proc_identifier
	global count_var_identifier
	global key


	if (node.val == "PROGRAM"):
		tmp = "; "
		tmp += proc_identifier[count_proc_identifier]
		tmp += "\ncode SEGMENT\n\tASSUME cs:code"
		if (node.parent_element.leaves[3].leaves[0].val == "BEGIN"):
			tmp += '\nbegin:'
			tmp += "\tpush	ebp\n"
			tmp += "\tmov	ebp, esp\n"
			tmp += "\txor	eax, eax\n"
			tmp += "\tmov	esp, ebp\n"
			tmp += "\tpop	ebp\n"
			print(tmp)


#Для доп задания
	# elif (node.val == 'statement'):
	# 	tmp = '\ncall '
	# 	ident = node.leaves[0].leaves[0].leaves[0].val
	# 	if ident in proc_identifier:
	# 		tmp+=ident
	# 		print(tmp)
	# 	else:
	# 		print(tmp)
	# 		print("NO SUCH PROCEDURE")
	# 		quit()


	elif (node.val == "PROCEDURE"):
		tmp =''
		ident = proc_identifier[count_proc_identifier]
		if ident in wrong_identifier:
			tmp += proc_identifier[count_proc_identifier]
			print (tmp)
			print ('This identifier already exist')
			quit()
		tmp += proc_identifier[count_proc_identifier]
		tmp += " PROC"
		print(tmp)


	elif (node.val == "declaration"):
		tmp = ''
		count = 8
		for i in range(0, len(node.leaves[0].leaves)):
			if (node.leaves[0].leaves[i].val != ','):
				if (node.leaves[0].leaves[i].leaves[0].val == "identifier"):
					tmp += "\t_"
					if (var_identifier[count_var_identifier] in wrong_identifier):
						tmp += var_identifier[count_var_identifier]
						print(tmp)
						print('This identifier already exist')
						quit()
					tmp += var_identifier[count_var_identifier]
					count_var_identifier +=1
					tmp += "$ = "
					tmp += str(count)
					tmp += "\n"
					count += 4
			i+=1
		print(tmp)


	elif node.val == "END":
		tmp = ''
		if (key[count_proc_identifier] == "PROCEDURE"):
			ident = proc_identifier[count_proc_identifier]
			if ident in wrong_identifier:
				tmp += proc_identifier[count_proc_identifier]
				print (tmp) 
				print ('This identifier already exist')		
				quit()
			tmp += proc_identifier[count_proc_identifier]
			tmp += " PROC\n"
			tmp += "\tret   0\n"
			tmp += proc_identifier[count_proc_identifier]
			tmp += " ENDP\n"
			count_proc_identifier +=1

		else:
			tmp += "\tret   0\n"
			tmp += "\n\tmov ax, 4c00h\n\tint 21h\ncode ENDS\n\tend begin\n\n"
			count_proc_identifier +=1
		print(tmp)

	for i in range(len(node.leaves)):
		generator(node.leaves[i])


if __name__ == '__main__':
    kompile('TEST.txt')
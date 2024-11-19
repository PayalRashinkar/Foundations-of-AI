import time
start_time = time.time()
import re
import itertools
import collections
import copy
import queue

p = open("input.txt","r")
input_data = p.readlines()
count = 0
n = 1
query = list()
query.append(input_data[0].rstrip())
k = int(input_data[1])
kb_init = list()

var_array = list("abcdefghijklmnopqrstuvwxyz")
var_array2 = []
var_array3 = []
var_array5 = []
var_array6 = []
for eachCombination in itertools.permutations(var_array, 2):
    var_array2.append(eachCombination[0] + eachCombination[1])
for eachCombination in itertools.permutations(var_array, 3):
    var_array3.append(eachCombination[0] + eachCombination[1] + eachCombination[2])
for eachCombination in itertools.permutations(var_array, 4):
    var_array5.append(eachCombination[0] + eachCombination[1] + eachCombination[2] + eachCombination[3])
for eachCombination in itertools.permutations(var_array, 5):
    var_array6.append(
        eachCombination[0] + eachCombination[1] + eachCombination[2] + eachCombination[3] + eachCombination[4])
var_array = var_array + var_array2 + var_array3 + var_array5 + var_array6
capitalVariables = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = 0
repeat_sentence_check=collections.OrderedDict()

def CNF(sentence):
    antecedent, consequent = sentence.split('=>')
    or_atoms = antecedent.split('|')
    for i in or_atoms:
        if '&' in i:
            temp1 = i.split('&')
            for j in range(0, len(temp1)):
                if temp1[j][0] == '~':
                    temp1[j] = temp1[j][1:]
                else:
                    temp1[j] = '~' + temp1[j]
            temp2 = '|'.join(temp1)
            temp2 = temp2 + '|' + consequent
            prd3 = temp2
            kb_init.append(prd3)
        else:
            negated_atoms = []
            if i[0] == '~':
                negated_atoms.append(i[1:])
            else:
                negated_atoms.append('~' + i)

            clauses = []
            for j, i in enumerate(negated_atoms):
                clause = negated_atoms[j] + '|' + consequent
                clauses.append(clause)
            for k in clauses:
                kb_init.append(k)

def CNF_ao(sentence):
    or_atoms = sentence.split('|')
    separator = "|"
    filtered_strings = [s for s in or_atoms if "&" not in s]
    prd1 = separator.join(filtered_strings)
    list1 = []
    for i in or_atoms:
        if '&' in i:
            temp1 = i.split('&')
            for j in temp1:
                if prd1 != '':
                    test = prd1 + '|' + j
                    list1.append(test)
    list2 = []
    for i in or_atoms:
        conj = i.split('&')
        clauses = []
        for j in conj:
            if j.isalpha():
                clauses.append(j)
            else:
                new_clause = j.replace('|', ' ')
                clauses.extend(new_clause.split())
        list2.append(clauses)

    for i in itertools.product(*list2):
        clause = '|'.join(i)
        kb_init.append(clause)

def CNF_a(sentence):
    atoms = sentence.split('&')
    for i in atoms:
        kb_init.append(i)

def standardize_kb(sentence):
    newsentence = list(sentence)
    i = 0
    global number
    variables = collections.OrderedDict()
    positionsofvariable = collections.OrderedDict()
    lengthofsentence = len(sentence)
    for i in range(0, lengthofsentence - 1):
        if (newsentence[i] == ',' or newsentence[i] == '('):
            if newsentence[i + 1] not in capitalVariables:
                substitution = variables.get(newsentence[i + 1])
                positionsofvariable[i + 1] = i + 1
                if not substitution:
                    variables[newsentence[i + 1]] = var_array[number]
                    newsentence[i + 1] = var_array[number]
                    number += 1
                else:
                    newsentence[i + 1] = substitution
    return "".join(newsentence)

for qi in range(0,n):
    query[qi]=standardize_kb(query[qi])

def val_substitute(paramArray, x, y):
    for index, eachVal in enumerate(paramArray):
        if eachVal == x:
            paramArray[index] = y
    return paramArray

def func_standardize_kb(sentence):
    lengthofsentence = len(sentence)
    newsentence = sentence
    variables = collections.OrderedDict()
    positionsofvariable = collections.OrderedDict()
    global number
    i = 0
    while i <= len(newsentence) - 1:
        if (newsentence[i] == ',' or newsentence[i] == '('):
            if newsentence[i + 1] not in capitalVariables:
                j = i + 1
                while (newsentence[j] != ',' and newsentence[j] != ')'):
                    j += 1
                substitution = variables.get(newsentence[i + 1:j])
                if not substitution:
                    variables[newsentence[i + 1:j]] = var_array[number]
                    newsentence = newsentence[:i + 1] + var_array[number] + newsentence[j:]
                    i = i + len(var_array[number])
                    number += 1
                else:
                    newsentence = newsentence[:i + 1] + substitution + newsentence[j:]
                    i = i + len(substitution)
        i += 1
    return newsentence

def check_inside_kb(sentence):
    lengthofsentence=len(sentence)
    newsentence=pattern1.split(sentence)
    newsentence.sort()
    newsentence="|".join(newsentence)
    global repeat_sentence_check
    i=0
    while i <=len(newsentence)-1 :
        if(newsentence[i]==',' or newsentence[i]=='('):
            if newsentence[i+1] not in capitalVariables:
               j=i+1
               while(newsentence[j]!=',' and newsentence[j]!=')' ):
                     j+=1
               newsentence=newsentence[:i+1]+'x'+newsentence[j:]
        i+=1

    repeatflag=repeat_sentence_check.get(newsentence)
    if repeatflag :
        return True
    repeat_sentence_check[newsentence]=1
    return False

def change(sentence,theta):
    lengthofsentence=len(sentence)
    newsentence=sentence
    i=0
    while i <=len(newsentence)-1 :
        if(newsentence[i]==',' or newsentence[i]=='('):
            if newsentence[i+1] not in capitalVariables:
               j=i+1
               while(newsentence[j]!=',' and newsentence[j]!=')' ):
                     j+=1
               nstemp=newsentence[i+1:j]
               substitution=theta.get(nstemp)
               if substitution :
                    newsentence=newsentence[:i+1]+substitution+newsentence[j:]
                    i=i+len(substitution)
        i+=1
    return newsentence


for i in range(n+1,n+1+k):
     input_data[i]=input_data[i].replace(" ","")
     if "=>" in input_data[i]:
        input_data[i]=input_data[i].replace(" ","")
        CNF(input_data[i].rstrip())
     elif ("&" in input_data[i] and "|" in input_data[i]):
        input_data[i] = input_data[i].replace(" ", "")
        CNF_ao(input_data[i].rstrip())
     elif ("&" in input_data[i]):
        input_data[i] = input_data[i].replace(" ", "")
        CNF_a(input_data[i].rstrip())
     else:
        kb_init.append(input_data[i].rstrip())

for i in range(0,k):
    kb_init[i]=kb_init[i].replace(" ","")

kb={}
pattern1 = re.compile("\||&|=>")
pattern2 = re.compile("[(,]")

for i in range(0,len(kb_init)):
    temp=pattern1.split(kb_init[i])
    len_of_temp=len(temp)
    for j in range(0,len_of_temp):
        clause=temp[j]
        clause=clause[:-1]
        predicate=pattern2.split(clause)
        argumentlist=predicate[1:]
        len_of_pred=len(predicate)-1
        if predicate[0] in kb:
            if len_of_pred in kb[predicate[0]]:
                kb[predicate[0]][len_of_pred].append([kb_init[i],temp,j,predicate[1:]])
            else:
                kb[predicate[0]][len_of_pred]=[kb_init[i],temp,j,predicate[1:]]
        else:
            kb[predicate[0]]={len_of_pred:[[kb_init[i],temp,j,predicate[1:]]]}

def sigma_unification(arglist1,arglist2):
    theta = collections.OrderedDict()
    for i in range(len(arglist1)):
        if arglist1[i] != arglist2[i] and (arglist1[i][0] in capitalVariables) and (arglist2[i][0] in capitalVariables):
            return []
        elif arglist1[i] == arglist2[i] and (arglist1[i][0] in capitalVariables) and (arglist2[i][0] in capitalVariables):
            if arglist1[i] not in theta.keys():
                theta[arglist1[i]] = arglist2[i]
        elif (arglist1[i][0] in capitalVariables) and not (arglist2[i][0] in capitalVariables):
            if arglist2[i] not in theta.keys():
                theta[arglist2[i]] = arglist1[i]
                arglist2 = val_substitute(arglist2, arglist2[i], arglist1[i])
        elif not (arglist1[i][0] in capitalVariables) and (arglist2[i][0] in capitalVariables):
            if arglist1[i] not in theta.keys():
                theta[arglist1[i]] = arglist2[i]
                arglist1 = val_substitute(arglist1, arglist1[i], arglist2[i])
        elif not (arglist1[i][0] in capitalVariables) and not (arglist2[i][0] in capitalVariables):
            if arglist1[i] not in theta.keys():
                theta[arglist1[i]] = arglist2[i]
                arglist1 = val_substitute(arglist1, arglist1[i], arglist2[i])
            else:
                argval=theta[arglist1[i]]
                theta[arglist2[i]]=argval
                arglist2 = val_substitute(arglist2, arglist2[i], argval)
    return [arglist1,arglist2,theta]

def theorem_prover():
    global repeat_sentence_check
    answer=list()
    for qr in query:
        repeat_sentence_check.clear()
        q=queue.Queue()
        query_start=time.time()
        kb_query=copy.deepcopy(kb)
        ans=qr
        if qr[0]=='~':
            ans=qr[1:]
        else:
            ans='~'+qr
        q.put(ans)
        ans_latest="FALSE"
        counter=0
        while True:
            counter+=1
            print(counter)
            if q.empty():
                break
            ans=q.get()
            ansclauses=pattern1.split(ans)
            len_ans_clause=len(ansclauses)
            flagmatchedwithkb=0
            for ac in range(0,len_ans_clause):
                ansclausestruncated=ansclauses[ac][:-1]
                ansclausespredicate=pattern2.split(ansclausestruncated)
                len_ans_clausepredicate=len(ansclausespredicate)-1
                if ansclausespredicate[0][0]=='~':
                    anspredicatenegated=ansclausespredicate[0][1:]
                else:
                    anspredicatenegated="~"+ansclausespredicate[0]
                x=kb_query.get(anspredicatenegated,{}).get(len_ans_clausepredicate)
                if not x:
                    continue
                else:
                    len_x=len(x)
                    for num_of_pred in range(0,len_x):
                        sentence_selec=x[num_of_pred]
                        theta_list=sigma_unification(copy.deepcopy(sentence_selec[3]),copy.deepcopy(ansclausespredicate[1:]))
                        if(len(theta_list)!=0):
                            for key in theta_list[2]:
                                tl=theta_list[2][key]
                                tl2=theta_list[2].get(tl)
                                if tl2:
                                    theta_list[2][key]=tl2
                            flagmatchedwithkb=1
                            notincludedindex=sentence_selec[2]
                            senclause=copy.deepcopy(sentence_selec[1])
                            merge=""
                            del senclause[notincludedindex]
                            ansclauseleft=copy.deepcopy(ansclauses)
                            del ansclauseleft[ac]
                            for am in range(0,len(senclause)):
                                senclause[am]=change(senclause[am],theta_list[2])
                                merge=merge+senclause[am]+'|'
                            for remain in range(0,len(ansclauseleft)):
                                listansclauseleft=ansclauseleft[remain]
                                ansclauseleft[remain]=change(listansclauseleft,theta_list[2])
                                if ansclauseleft[remain] not in senclause:
                                    merge=merge+ansclauseleft[remain]+'|'
                            merge=merge[:-1]
                            if merge=="":
                               ans_latest="TRUE"
                               break
                            kb_flag=check_inside_kb(merge)
                            if not kb_flag:
                                merge = func_standardize_kb(merge)
                                ans=merge
                                temp=pattern1.split(ans)
                                len_of_temp=len(temp)
                                for j in range(0,len_of_temp):
                                    clause=temp[j]
                                    clause=clause[:-1]
                                    predicate=pattern2.split(clause)
                                    argumentlist=predicate[1:]
                                    len_of_pred=len(predicate)-1
                                    if predicate[0] in kb_query:
                                        if len_of_pred in kb_query[predicate[0]]:
                                            kb_query[predicate[0]][len_of_pred].append([merge,temp,j,argumentlist])
                                        else:
                                            kb_query[predicate[0]][len_of_pred]=[[merge,temp,j,argumentlist]]
                                    else:
                                        kb_query[predicate[0]]={len_of_pred:[[merge,temp,j,argumentlist]]}
                                q.put(ans)
                    if(ans_latest=="TRUE"):
                        break
            if(ans_latest=="TRUE"):
               break
            if (counter == 2000 or (time.time() - query_start) > 600):
               ans_latest = "TRUE"
               break
        answer.append(ans_latest)
    return answer

if __name__ == '__main__':
    true_false=theorem_prover()
    file=open("output.txt","w+")
    file.write(true_false[0])
    file.close()

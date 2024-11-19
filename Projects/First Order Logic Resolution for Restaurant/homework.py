import time
start_time = time.time()
import re
import itertools
import collections
import copy
import queue

p=open("input.txt","r")
data=list()
data1= p.readlines()
count=0

n=1
queries=list()
queries.append(data1[0].rstrip())

k=int(data1[1])
kbbefore=list()

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
            kbbefore.append(prd3)
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
                kbbefore.append(k)

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
        kbbefore.append(clause)

def CNF_a(sentence):
    atoms = sentence.split('&')
    for i in atoms:
        kbbefore.append(i)


variableArray = list("abcdefghijklmnopqrstuvwxyz")
variableArray2 = []
variableArray3 = []
variableArray5 = []
variableArray6 = []
for eachCombination in itertools.permutations(variableArray, 2):
    variableArray2.append(eachCombination[0] + eachCombination[1])
for eachCombination in itertools.permutations(variableArray, 3):
    variableArray3.append(eachCombination[0] + eachCombination[1] + eachCombination[2])
for eachCombination in itertools.permutations(variableArray, 4):
    variableArray5.append(eachCombination[0] + eachCombination[1] + eachCombination[2] + eachCombination[3])
for eachCombination in itertools.permutations(variableArray, 5):
    variableArray6.append(
        eachCombination[0] + eachCombination[1] + eachCombination[2] + eachCombination[3] + eachCombination[4])
variableArray = variableArray + variableArray2 + variableArray3 + variableArray5 + variableArray6
capitalVariables = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = 0


def standardizationnew(sentence):
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
                    variables[newsentence[i + 1]] = variableArray[number]
                    newsentence[i + 1] = variableArray[number]
                    number += 1
                else:
                    newsentence[i + 1] = substitution
    return "".join(newsentence)


def insidestandardizationnew(sentence):
    lengthofsentence = len(sentence)
    newsentence = sentence
    #print(newsentence)
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
                    variables[newsentence[i + 1:j]] = variableArray[number]
                    newsentence = newsentence[:i + 1] + variableArray[number] + newsentence[j:]
                    i = i + len(variableArray[number])
                    number += 1
                else:
                    newsentence = newsentence[:i + 1] + substitution + newsentence[j:]
                    i = i + len(substitution)
        i += 1
    #print(newsentence)
    return newsentence

capitalVariables = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def replace(sentence,theta):
    lengthofsentence=len(sentence)
    newsentence=sentence
    #print(newsentence)
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
    #print(newsentence)
    #input()
    return newsentence

repeatedsentencecheck=collections.OrderedDict()

def insidekbcheck(sentence):
    lengthofsentence=len(sentence)
    newsentence=pattern.split(sentence)
    newsentence.sort()
    newsentence="|".join(newsentence)
    global repeatedsentencecheck
    i=0
    while i <=len(newsentence)-1 :
        if(newsentence[i]==',' or newsentence[i]=='('):
            if newsentence[i+1] not in capitalVariables:
               j=i+1
               while(newsentence[j]!=',' and newsentence[j]!=')' ):
                     j+=1
               newsentence=newsentence[:i+1]+'x'+newsentence[j:]
        i+=1
    repeatflag=repeatedsentencecheck.get(newsentence)
    if repeatflag :
        return True
    repeatedsentencecheck[newsentence]=1
    return False

for i in range(n+1,n+1+k):
     data1[i]=data1[i].replace(" ","")
     if "=>" in data1[i]:
        data1[i]=data1[i].replace(" ","")
        CNF(data1[i].rstrip())
     elif ("&" in data1[i] and "|" in data1[i]):
        data1[i] = data1[i].replace(" ", "")
        CNF_ao(data1[i].rstrip())
     elif ("&" in data1[i]):
        data1[i] = data1[i].replace(" ", "")
        CNF_a(data1[i].rstrip())
     else:
        kbbefore.append(data1[i].rstrip())

for i in range(0,k):
    kbbefore[i]=kbbefore[i].replace(" ","")

kb={}
pattern=re.compile("\||&|=>")
pattern1=re.compile("[(,]")
for i in range(0,len(kbbefore)):
    temp=pattern.split(kbbefore[i])
    lenoftemp=len(temp)
    for j in range(0,lenoftemp):
        clause=temp[j]
        clause=clause[:-1]
        predicate=pattern1.split(clause)
        argumentlist=predicate[1:]
        lengthofpredicate=len(predicate)-1
        if predicate[0] in kb:
            if lengthofpredicate in kb[predicate[0]]:
                kb[predicate[0]][lengthofpredicate].append([kbbefore[i],temp,j,predicate[1:]])
            else:
                kb[predicate[0]][lengthofpredicate]=[kbbefore[i],temp,j,predicate[1:]]
        else:
            kb[predicate[0]]={lengthofpredicate:[[kbbefore[i],temp,j,predicate[1:]]]}


for qi in range(0,n):
    queries[qi]=standardizationnew(queries[qi])

def substituevalue(paramArray, x, y):
    for index, eachVal in enumerate(paramArray):
        if eachVal == x:
            paramArray[index] = y
    #print(paramArray)
    #input()
    return paramArray

def unificiation(arglist1,arglist2):
    theta = collections.OrderedDict()
    #print(theta)
    #input()
    for i in range(len(arglist1)):
        if arglist1[i] != arglist2[i] and (arglist1[i][0] in capitalVariables) and (arglist2[i][0] in capitalVariables): #if both are different constant cant substitute
            return []
        elif arglist1[i] == arglist2[i] and (arglist1[i][0] in capitalVariables) and (arglist2[i][0] in capitalVariables): #if both are same constants
            if arglist1[i] not in theta.keys():
                theta[arglist1[i]] = arglist2[i]
        elif (arglist1[i][0] in capitalVariables) and not (arglist2[i][0] in capitalVariables):#if kb is constant variable and ans is variable
            #print("Payaal")
            if arglist2[i] not in theta.keys():
                theta[arglist2[i]] = arglist1[i]
                arglist2 = substituevalue(arglist2, arglist2[i], arglist1[i])
        elif not (arglist1[i][0] in capitalVariables) and (arglist2[i][0] in capitalVariables):#if kb is variable and ans is constant
            #print("Eta?")
            #print(arglist1 + arglist2)
            if arglist1[i] not in theta.keys():
                theta[arglist1[i]] = arglist2[i]
                arglist1 = substituevalue(arglist1, arglist1[i], arglist2[i])
        elif not (arglist1[i][0] in capitalVariables) and not (arglist2[i][0] in capitalVariables):#if kb and ans both are variable
            if arglist1[i] not in theta.keys():
                theta[arglist1[i]] = arglist2[i]
                arglist1 = substituevalue(arglist1, arglist1[i], arglist2[i])
            else:
                argval=theta[arglist1[i]]
                theta[arglist2[i]]=argval
                arglist2 = substituevalue(arglist2, arglist2[i], argval)
    #print(arglist1,arglist2,theta)
    return [arglist1,arglist2,theta]

def resolution():
    global repeatedsentencecheck
    answer=list()
    qrno=0
    for qr in queries:
        qrno+=1
        repeatedsentencecheck.clear()
        q=queue.Queue()
        query_start=time.time()
        kbquery=copy.deepcopy(kb)
        #print(kbquery)
        #input()
        ans=qr
        #print(ans)
        #input()
        if qr[0]=='~':
            ans=qr[1:]
        else:
            ans='~'+qr
        q.put(ans)
        currentanswer="FALSE"
        counter=0
        while True:
            counter+=1
            print(counter)
            if q.empty():
                break
            ans=q.get()
            print(ans)
            #input()
            ansclauses=pattern.split(ans)
            lenansclauses=len(ansclauses)
            print(lenansclauses)
            flagmatchedwithkb=0
            innermostflag=0
            for ac in range(0,lenansclauses):###length of answer claus is 1
                insidekbflag=0
                ansclausestruncated=ansclauses[ac][:-1]
                ansclausespredicate=pattern1.split(ansclausestruncated)
                lenansclausespredicate=len(ansclausespredicate)-1
                if ansclausespredicate[0][0]=='~':
                    anspredicatenegated=ansclausespredicate[0][1:]
                else:
                    anspredicatenegated="~"+ansclausespredicate[0]
                x=kbquery.get(anspredicatenegated,{}).get(lenansclausespredicate)

                print(x)
                if not x:
                    continue
                else:
                    lenofx=len(x) #number of matching predicates in KB with that of ans query
                    print(lenofx)
                    payal = 0
                    for numofpred in range(0,lenofx):
                        insidekbflag=0
                        payal = payal + 1
                        #print(payal)
                        putinsideq=0
                        sentenceselected=x[numofpred]
                        #print(sentenceselected)
                        #print(ansclausespredicate)
                        thetalist=unificiation(copy.deepcopy(sentenceselected[3]),copy.deepcopy(ansclausespredicate[1:]))
                        #print(thetalist)
                        #input()
                        if(len(thetalist)!=0):
                            for key in thetalist[2]:
                                tl=thetalist[2][key]
                                tl2=thetalist[2].get(tl)
                                if tl2:
                                    thetalist[2][key]=tl2
                            flagmatchedwithkb=1
                            notincludedindex=sentenceselected[2]
                            senclause=copy.deepcopy(sentenceselected[1])
                            mergepart1=""
                            del senclause[notincludedindex]
                            ansclauseleft=copy.deepcopy(ansclauses)
                            del ansclauseleft[ac]
                            for am in range(0,len(senclause)):
                                senclause[am]=replace(senclause[am],thetalist[2]) #substitue a value eg: ['~Take(a,Warfarin)'] with ['~Take(Alice,Warfarin)']
                                mergepart1=mergepart1+senclause[am]+'|' #add | to senclause ~Take(Alice,Warfarin)|
                            for remain in range(0,len(ansclauseleft)):
                                listansclauseleft=ansclauseleft[remain]
                                ansclauseleft[remain]=replace(listansclauseleft,thetalist[2])
                                if ansclauseleft[remain] not in senclause:
                                    mergepart1=mergepart1+ansclauseleft[remain]+'|'
                            mergepart1=mergepart1[:-1]
                            #print(mergepart1)
                            #input()
                            if mergepart1=="":
                               currentanswer="TRUE"
                               break
                            ckbflag=insidekbcheck(mergepart1)
                            #print(len(mergepart1.split("|")))
                            #print(len(mergepart1))
                            #print("Payal")
                            #input()
                            #if not ckbflag and len(mergepart1.split("|")) <= 5:
                            if not ckbflag:
                                mergepart1 = insidestandardizationnew(mergepart1)
                                ans=mergepart1
                                temp=pattern.split(ans)
                                lenoftemp=len(temp)
                                for j in range(0,lenoftemp):
                                    clause=temp[j]
                                    clause=clause[:-1]
                                    predicate=pattern1.split(clause)
                                    argumentlist=predicate[1:]
                                    lengthofpredicate=len(predicate)-1
                                    if predicate[0] in kbquery:
                                        if lengthofpredicate in kbquery[predicate[0]]:
                                            kbquery[predicate[0]][lengthofpredicate].append([mergepart1,temp,j,argumentlist])
                                        else:
                                            kbquery[predicate[0]][lengthofpredicate]=[[mergepart1,temp,j,argumentlist]]
                                    else:
                                        kbquery[predicate[0]]={lengthofpredicate:[[mergepart1,temp,j,argumentlist]]}
                                print(kbquery)
                                input()
                                q.put(ans)
                    if(currentanswer=="TRUE"):
                        break
            if(currentanswer=="TRUE"):
               break
            #if(counter == 2000 or (time.time() - query_start) > 900):
            if (time.time() - query_start > 600):
               break
        answer.append(currentanswer)
    return answer

#print(kbbefore)
#input()
if __name__ == '__main__':
    finalanswer=resolution()
    o=open("output.txt","w+")
    o.write(finalanswer[0])
    o.close()

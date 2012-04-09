#!/usr/bin/python

from eliza_help import *
##from getpass import getpass #To make the passkey invisible

offen=0#To withstand abuse

def word_matching(user_in):
    global offen
    split_in=user_in.split()
    
    if "stop" in user_in or "bye" in user_in:
        
        print_special("It's been nice, chatting with you, Bye :)")
        return 2
    a=open('offensive.txt',"r")
    f=a.read()
    a.close()
    f=f.split('\n')
    greet=["hii","hello"]
    common_talk=["boring","just","plain","because"]
    for i in split_in:
        if i in f:
            if offen==0:
                offen=1
                
                print_special("I am very sensitive. Please don't use offensive language")
                return 1
            elif offen==1:
                offen=2
                
                print_special("This is the second time you used an offensive word. Another time --> Chat will be terminated")
                return 1
            else:
                print_special("Go *&$% yourself")
                return 2
    for i in greet:
        if i in user_in:
            print i.capitalize()
            return 1
    for i in common_talk:
        if i in user_in:
            print_special("ok, got it.")
            return 1
    if "question" in user_in:
        print_special("You ask the question, I will give answer")
        return 1
    if "oh" in user_in or "huh" in user_in:
        print_special("You look tired")
        return 1
        
    if "you" in user_in:
        print_special("I don't want to answer, let's talk about you")
        return 1

    if "ok" in user_in or "yes" in user_in:
        print_special("cool")
        return 1
  
    
    return 0
    
def pattern_matching(user_in):
    split_in=user_in.split()
    flag=0
    ques=["do you","what","who","how","where"]
    for i in ques:
        if i in user_in:
            print_special("Why do you want to know ?")
            return 1

    for i in range(0,len(split_in)):
        if split_in[i]=="i":
            split_in[i]="you"
        elif split_in[i]=="am" and flag==0:
            split_in[i]="are"
        elif split_in[i]=="me":
            split_in[i]="you"
        elif split_in[i]=="you":
            if i==(len(split_in)-1):
                split_in[i]="me"
            else:
                split_in[i]="I"
                flag=0
                if split_in[i+1]=="are":
                    split_in[i+1]="am"
                    flag=1
        elif split_in[i]=="they":
            split_in[i]="them"
    #print split_in    
    if len(split_in)>1:
        if split_in[1]=="are" and split_in[0]!="you":
            print_special("Tell me more about "+split_in[0])
            return 1
        if split_in[0]=="my" or (split_in[1]=="are" and split_in[0]=="you") or split_in[1]=="is" or ("I" in split_in and "am" in split_in):
            l='your '
            st=1
            if split_in[0]=="you":
                st=2
                l='you are '
            if split_in[1]=="is":
                st=0
                l=''
            if "I" in split_in:
                st=0
                l=''
            for j in range(st,len(split_in)):
                l+=split_in[j]+' '
            print_special("Why do you think "+l+'?')
            return 1

    if "why" in user_in and "do you" in user_in:
        print_special("I am trying to increase my knowledge")
        return 1

    f=word_matching(user_in)
    if f==2:
        return 2
    if f==1:
        return 1
    
    

    
    return 0


p=reload()#For reloading

pre_user_in=''
while True:
    print "\nYou:"
    user_in=raw_input()
    split_in=user_in.split()
    #print split_in
    print '\nEliza:'

    user_in=purify_string(user_in)
    user_in=user_in.replace(',','')#We are not replacing , while we are removing the punctuation chars


    if pre_user_in==user_in:

        print_special("Don't repeat the same words. Try something else")
        continue
    
    pre_user_in=user_in
    if user_in in p:
        
        print_special(p[user_in])
        continue
    if "learn" in user_in:
        p=Learn_new()
        continue
    flag=pattern_matching(user_in)
    if flag==1:
        continue
    elif flag==2:
        break

    #print split_in
    if len(split_in)<=1:
        print "I know you can speak more than that"
        continue




    print_special("Sorry, I didn't get you\n1. If you want to stop chatting, say stop\n2. If you want to make me learn something say - Learn")
    

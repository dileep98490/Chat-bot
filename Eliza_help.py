from getpass import getpass #To make the passkey invisible

def remove_punctuation(s):
    f=['.','(',')','"',"'",'[',']','{','}','?','!','*','&','^','%','$','#','@','-','|']
    for i in f:
        s=s.replace(i,'')
    return s
def print_special(s):
    print s
def remove_trailingwhitespace(s):
    p=len(s)-1
    while ord(s[p]) not in range(97,123):
            p-=1
    st=0
    while ord(s[st]) not in range(97,123):
        st+=1
    return s[st:p+1]
def purify_string(s):
    s=s.lower()
    s=remove_punctuation(s)
    s=remove_trailingwhitespace(s)
    return s
def Learn_new():
    print_special("Enter the passkey")
    print "\nYou:"
    pass_key=raw_input()
    print "\nEliza:"
    if pass_key.lower()!="elizaiscool":
        print_special("Get the passkey from my true master")
        p=reload()
        return p
    a=open('data.txt',"a")
    
    #a.write(EOF)
    a.write('\n')

    
    print_special("Welcome admin\n")
    
    print_special("Now tell me the type of question that may be asked, if there are similar questions (That have similar snswers) seperate them by a ,)")
    print "\nYou:"
    #print '\t'
    f1=raw_input()
    f1=purify_string(f1)
    a.write(f1)
    a.write('-')
    print "\nEliza:"
    
    print_special("Answer that should be given?")
    print "\nYou:"
    #print '\t'
    f1=raw_input()
    #f1=purify_string(f1)
    a.write(f1)
    #a.write('\n')
    a.close()
    print "\nEliza:"
    
    print_special("Successfully Updated")
    p=reload()
    return p
def reload():
    a=open('data.txt',"r")
    f=a.read()
    a.close()

    q=f.split('\n')
    ln=[]
#exit
    for i in q:
        ln.append(i.split('-'))
    
#print ln
    p={}
    for i in ln:
        l=i[0].split(',')
        for j in l:
            p[j]=i[1]
    return p

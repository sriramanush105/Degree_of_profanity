
#steps followed
#1.read the file line by line
#2.calculate degree of profanity and display



#Defining prof() func to return degree of profanity of a sentece
def prof(line,r_words):
    
    ''' inputs
        line: sentence from file
        r_words: racial words
        
        1.line is split in to words and converted to lower case
        2.we iterate through words to find r_words count
        NOTE: lower() method is to remove case sensitvity'''
    words=[i.lower() for i in line.split()]
    r_score=0
    for word in words:
        if  word.lower() in r_words:
            r_score=r_score+1
    return r_score/len(words)        
        
    
r_words=['terror','attack']
#Read file using open()and iterate through lines  to find degree of profanity
with open(r'C:\Users\Sriram\Desktop\tweets.txt','r') as f:
    for line in f:
        line=line.rstrip('\n')#rstrip() used to eliminate \n at the endline
        print(line,' score -',prof(line,r_words))
        


from collections import defaultdict
from random import randint

alphabet = defaultdict(list)

#Letter that can follow another letter
A = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']
B = ['a','e','i','l','o','r','u','y']
C = ['a','e','h','i','k','l','o','r','u','y']
D = ['a','e','i','o','r','u','y']
E = ['a','b','c','d','e','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
F = ['a','e','i','l','o','r','u','y']
G = ['a','e','h','i','l','o','r','u','y']
H = ['a','e','i','o','u','y']
I = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
J = ['a','e','i','o','u','y']
K = ['a','e','i','l','o','r','u','y']
L = ['a','e','i','o','u','y']
M = ['a','e','i','o','u','y']
N = ['a','e','i','o','u','y']
O = ['a','b','c','d','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
P = ['a','e','i','l','o','r','u','y']
Q = ['u']
R = ['a','e','i','o','u','y']
S = ['a','c','e','h','i','k','l','m','n','o','p','q','t','u','w','y']
T = ['a','e','h','i','o','r','u','w','y']
U = ['a','b','c','d','e','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
V = ['a','e','i','o','r','u','y']
W = ['a','e','i','o','r','u','y']
X = ['a','e','i','o','u','y']
Y = ['a','e','i','o','u']
Z = ['a','e','i','o','u','y']

alphabet[0] = A
alphabet[1] = B
alphabet[2] = C 
alphabet[3] = D
alphabet[4] = E
alphabet[5] = F
alphabet[6] = G
alphabet[7] = H
alphabet[8] = I
alphabet[9] = J
alphabet[10] = K
alphabet[11] = L
alphabet[12] = M
alphabet[13] = N
alphabet[14] = O
alphabet[15] = P
alphabet[16] = Q
alphabet[17] = R
alphabet[18] = S
alphabet[19] = T
alphabet[20] = U
alphabet[21] = V
alphabet[22] = W
alphabet[23] = X
alphabet[24] = Y
alphabet[25] = Z

def random_word(letter="a",length=1):

    cletter = letter.lower()
    string = letter

    for i in  range(0,length):
    
        letter = ord(letter) - 97

        #Get the next char to add to the string
        letter = alphabet[letter][randint(0,len(alphabet[letter])-1)]

        string += letter
        char = letter

    return string

def all_words(min_length,max_length):

    #Loop through the lengt of word you want
    for length in range(min_length,max_length+1):
        
        #Loop through the alphabet
        for i in range(0,len(alphabet)):
            
            #Recursivly find all words of length starting with chr(i+97)
            recursive_word(chr(i+97),length)
        
def recursive_word(string,length):

    #Print word if correct length
    if len(string) == length:

        print string
        
    #Else add to the word
    elif len(string) < length:

        letter = string[-1:].lower()
        letter = ord(letter) - 97

        for item in alphabet[letter]: 

            new_string = string + item
            recursive_word(new_string,length)
        
print random_word(chr(randint(97,123)),randint(3,10))
#all_words(3,4)



          

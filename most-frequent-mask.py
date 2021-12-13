import re,argparse
from collections import Counter

### Masking each individual password; returning a string
def maskPassword(password):
    masked_password= []
    for char in password:
        if char.islower():
            masked_password.append('?l')
        elif char.isupper():
            masked_password.append('?u')
        elif re.search("^[0-9]+",char):
            masked_password.append('?d')
        else:
            masked_password.append('?s')
        
    return "".join(masked_password)
            
### defining most occuring word function
def mostFrequent(list):
    maskedpassword_list = []
    
    ### masking each password with the help of another function
    for password in list:
        maskedpassword= maskPassword(password)
        maskedpassword_list.append(maskedpassword)
    
    ### storing numbers with their frequencies in counter as dictionary KV pairs
    c = Counter(maskedpassword_list)
    top_5_masks= c.most_common(5)
    return top_5_masks

    ### adding input file argument as an option
def argumentPars():
    parser = argparse.ArgumentParser(description='Finds the most occuring mask pattern from a supplied input file. ')
    parser.add_argument('-f','--file',type=str,help='specify a custom passwords file')
    args=parser.parse_args()
    filename= args.file
    return filename
    
def readFile(filename=r'100k-most-used-passwords.txt'):
    with open (filename,'r',encoding='latin-1') as f:
        huge_list= f.read().split()
        return(huge_list)

# main function
def main():
    filename= argumentPars()
    if filename:
        huge_list=readFile(filename)
    else:
        huge_list= readFile()
    top_5_masks= mostFrequent(huge_list)
    print("Top 5 Password Masks    \n" "-----------------------")
    i = 0
    for j,k in top_5_masks:
        i +=1 
        print("{}{} {:<20}{}   {:<10}".format(i, ".", j, ":", k))

### main program 
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Keyboard interrupted ... exiting program')
    except FileNotFoundError:
        print('File does not exist! \nPlease ensure you have the file in the same directory as this script.')


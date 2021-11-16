import os

def counter(fname):

    num_words = 0

    num_charc = 0
      
    num_spaces = 0

    different = set()
      
    with open("Стивен Кинг.txt", 'r', encoding="utf-8") as f:
          
        for line in f:
              
            line = line.strip(os.linesep)
              
            wordslist = line.split()
              
            num_words = num_words + len(wordslist)
              
            num_charc = num_charc + sum(1 for c in line 
                          if c not in (os.linesep, ' '))
              
            num_spaces = num_spaces + num_charc + sum(1 for s in line 
                                if s in (os.linesep, ' '))
              
            different |= set(line.split()) 
        

    print("Number of characters without spaces in text file: ", num_charc)

    print("Number of characters with spaces in text file: ", num_spaces)

    print("Number of words in text file: ", num_words)

    print(f"the total number of different words (no repetitions): {len(different)}")



  
if __name__ == '__main__': 
    fname = 'File1.txt'
    try: 
        counter(fname) 
    except: 
        print('File not found')
# python3

from collections import namedtuple


Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))

        elif next in ")]}":
            # if it is an empty list, means no left bracket
            if not opening_brackets_stack: 
                return i+1
            
            # if not empty, pop the last element, then check if there is a left bracket can be matched
            top = opening_brackets_stack.pop()
            # if doesn't match, then return the position
            if not are_matching(top.char, next):
                return i+1
    
    # if not empty, means only has a left bracket
    if opening_brackets_stack:
        top = opening_brackets_stack.pop()
        return top.position+1
    
    return "Success"
  
          
def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)



if __name__ == "__main__":
    main()



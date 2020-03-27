#for question 4
def examGrade(score):
    if score >= 95:
        return "Top Score"
    elif score >= 60 and score < 95:
        return "Pass"
    else:
        return "Fail"

print(examGrade(95))    #Top Score
print(examGrade(65))    #Pass
print(examGrade(40))    #Fail

def name(first_name, last_name):
    if(first_name == '' and last_name == ''):
        return ""

    name = last_name + "," + first_name
    if(first_name == '' or last_name ==''):
        name = name.replace(',', '')
    return "Name: " +  name

print(name("dan", ""))          #Name: dan
print(name("dan", "flanagan"))  #Name: flanagan,dan
print(name("", "flanagan"))     #Name: flanagan
print(name("","")) #

def longest_word(word1, word2, word3):
    array = [word1, word2, word3]
    longest = ""
    for word in array:
        if(len(word)> len(longest)):
            longest = word
    return longest

print(longest_word("chair", "table", "couch"))          #chair
print(longest_word("bed", "bath", "beyond"))            #beyond
print(longest_word("laptop", "notebook", "desktop"))    #notebook

def fractal_part(numerator, denominator):
    if(denominator == 0): return 0
    value = numerator/denominator
    return abs(int(value) - value)

print(fractal_part(5,5)) #0
print(fractal_part(5,4)) #0.25
print(fractal_part(5,3)) #0.66 ...
print(fractal_part(5,2)) #0.5
print(fractal_part(5,0)) #0
print(fractal_part(0,5)) #0.0
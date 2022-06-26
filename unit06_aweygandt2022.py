############################################################
#     Aidan Weygandt                        05/07/21       #
#     Unit 6 Problems                                      #
#     Sum of Digits, sort 3 numbers, Display Characters    #
#     Palindrome Number, Palindromic Prime, Emirp          #
############################################################

print("Problem #1 - Sum of Digits")
def sumdigits(numb): #adds every character together from string
  output = 0
  for each in numb:
    output += int(each)
  return output
numP1 = input("Enter a number: ")
print("The sum of it's digits is", sumdigits(numP1))


print("\n\nProblem #2 - Sort three numbers")
def displaySortedNumbers(num1, num2, num3):
  print(num1, num2, num3)
  switch = 0
  while num1 > num2 or num2 > num3 or num3 < num1: #while not in numerical order it will keep switching numbers
    if num1 > num2:
      switch = num1
      num1 = num2
      num2 = switch
    if num2 > num3: 
      switch = num2
      num2 = num3
      num3 = switch
    if num3 < num1:
      switch = num3
      num3 = num1
      num1 = switch
  num_sort = str(num1) + " " + str(num2)+ " " + str(num3)
  return num_sort
unsorted = input("Enter three integers (1,2,3): ")
#a,b,c = input("Enter three integers (1,2,3): ").split(",")
#a,b,c = input("Enter three integers (1 2 3): ").split()


sorter = ""
for character in unsorted: #seperates numbers from commas
  if character != ",":
    sorter = sorter + character

print("The sorted number are", displaySortedNumbers(int(sorter[0:1]), int(sorter[1:2]), int(sorter[2:])))
#print("The sorted number are", displaySortedNumbers(a,b,c))


print("\n\nProblem #3 - Display Characters")
def printChars(ch1, ch2, numPerLine): 
  char1 = ch1 if ord(ch1) < ord(ch2) else ch2 #incase they aren't ordered
  char2 = ch2 if ord(ch1) < ord(ch2) else ch1
  counter = 0
  for every in range(0, ord(char2) - ord(char1) + 1): #prints every letter between the two
    print(chr(ord(char1) + every), end=" ")
    if counter == numPerLine - 1: #end line if it reaches whatever the user input
      print()
      counter = -1
    counter += 1

letters = input("Enter two letters to display the letters inbetween (a z): ")
PerLine = int(input("How many characters would you like per line?: "))
printChars(letters[0:1], letters[2:], PerLine)


print("\n\n\nProblem #4 - Palindrome Number")
def reverseInt(inp): #reverses input
  output = inp[::-1]
  return output

def isPalindrome(inp): #compares input to itself reversed
  if inp == reverseInt(inp):
    return "true"
  else: return "false"

numP4 = (input("Enter a number: ")) 
print("It is", isPalindrome(numP4), "that", numP4, "is a palindrome number.")


print("\n\nProblem #5 - Palindromic Prime")

def isPrime(num): 
  output = "true"
  for every in range(2, int(num/2) + 1): 
    if int(num)//every == int(num)/every: #if divisable by anything less than it
      output = "false"
  return output


def isPrime2(num):
  num = int(num)
  if num < 2: return False
  if num == 2: return True 
  if num % 2 == 0: return False
  for every in range(3, num//2 + 1, 2): 
    if num % every == 0: #if divisable by anything less than it
      return False
  return True

def PalindromicPrime(NumOfPrimes): #prints number that are both palindromic and prime
  NumOfNums = 0
  NumP5 = 2
  Line = 0
  while NumOfNums < NumOfPrimes: #while it hasnt printed all the numbers
    if isPrime(NumP5) == "true" and isPalindrome(str(NumP5)) == "true": #if number is both prime and palindromic
      print(format(NumP5, "5d"), end=" ")
      NumOfNums += 1
      Line += 1
    NumP5 += 1
    if Line >= 10:
      print()
      Line = 0
print("I suggest a max of around 20.") 
NumOfPrimes = input("How many palindromic primes would you like?: ")
PalindromicPrime(int(NumOfPrimes))
print("\ndone")


print("\n\n\nProblem #6 - Emirp - Non Palindromic Primes Whos Reverse Is Prime")
numP6 = 0
Line = 0
prints = 0
while prints < 100: #prints 100 numbers
  numP6 += 1
  if isPrime(numP6) == "true" and isPalindrome(str(numP6)) == "false" and isPrime(int(str(numP6)[::-1])) == "true": #only if its prime palindromic and the reverse is prime it prints
    Line += 1
    prints += 1
    print(format(numP6, "5d"), end=" ")
  if Line >= 10: #if ten are on one line then it moves down
    print()
    Line = 0
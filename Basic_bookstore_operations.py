"""
Baic bookstore operations
Code by: Simran Naryani
"""

print("Basic Bookstore Operations")
input("a) Delete the duplicate entries\n"
"b) Display books in ascending order based on cost of books\n"
"c) Count number of books with cost more than 500\n"
"d) Copy books in a new list which has cost less than 500\n")

n = int(input("Enter number of books: "))

class library: 
  name = []
  bookid = []
  cost = []
  
  def getdata(self):  #to get book details
    for i in range(n):
      self.name.append(input("Enter the name of the book:"))  #adding data to the list
      self.bookid.append(int(input("Enter the book id:")))
      self.cost.append(int(input("Enter the cost of the book:")))
      
  def duplicate(self):  #for checking duplicate values
    templist = []
    for x in self.name:
      if x not in templist:
        templist.append(x)
    self.name = templist
    print("List after deleting duplicate values is",templist)
    
  def costcheck(self): #to check and compare the cost of books
    cost_less = []
    cost_high = []
    for j in self.cost:
      if(j<500):
        cost_less.append(j)
      else:
        cost_high.append(j)
    print("The total count of books with price greater than 500 is:",len(cost_high))
    for x in cost_less:
      print("Cost of books less than 500 is:",x)
      
  def ascending_order(self): #displaying cost of books in ascending order
    self.cost.sort()
    print("Cost of books in ascending order is",self.cost)
    
  def display_data(self):  
    print("Name \t\t Book id \t Cost")
    for i in range(n):
      print(self.name[i],"\t\t",self.bookid[i],"\t\t",self.cost[i])
      
l=library()  #function calls
l.getdata()
l.display_data()
l.ascending_order()
l.duplicate()
l.costcheck()

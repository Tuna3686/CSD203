from Node import*
from Student import*
class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    #end def
    def isEmpty(self):
        return self.head == None
    def addFirst(self,name,age):
        if(name[0]=="X"):
            return
        node = Node(Student(name,age))
        if (self.isEmpty()):
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size +=1
    #end def
    def addLast(self,name,age):
        if (name[0]=="X"):
            return
        node = Node(Student(name,age))
        if(self.isEmpty()):
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size +=1
        
    def display(self):
        if (self.isEmpty()): return
        cur = self.head
        while cur:
            print(f"{cur.data}", end=" ")
            cur = cur.next
        print()
    def delFirst(self):
        if self.isEmpty():
            return None
        temp = self.head.data
        self.head = self. head.next
        self.size -=1
        return temp

    def check(self,x):
        '''Viet cang nhieu ham check cang tot it nhat 20
        định nghĩa số x, viết chương trình kiểm tra số x có phải số mà ta đã định nghĩa hay ko ?
        '''
        return x % 2 == 0
    
    def is_positive(x):
        """Checks if the number is strictly greater than zero."""
        return x > 0

    def is_negative(x):
        """Checks if the number is strictly less than zero."""
        return x < 0

    def is_even(self,x):
        """Checks if the number is even."""
        return x % 2 == 0

    def is_integer(x):
        """Checks if the number is a whole number (no decimals)."""
        return isinstance(x, int)  

    def is_float(x):
        """Checks if the number has decimal places (is a floating-point number)."""
        return isinstance(x, float)

    def is_divisible_by_5(x):
        """Checks if the number is divisible by 5 (leaves no remainder when divided by 5)."""
        return x % 5 == 0

    def is_divisible_by_3_and_5(x):
        """Checks if the number is divisible by both 3 and 5."""
        return x % 3 == 0 and x % 5 == 0

    def is_divisible_by_any(x, divisors):
        """Checks if the number is divisible by any of the numbers in the provided list of divisors."""
        return any(x % divisor == 0 for divisor in divisors)

    def is_prime(x):
        """Checks if the number is a prime number (only divisible by 1 and itself)."""
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    def is_perfect_square(x):
        """Checks if the number is a perfect square (the result of squaring an integer)."""
        return int(x**0.5) ** 2 == x

    def is_perfect_cube(x):
        """Checks if the number is a perfect cube (the result of cubing an integer)."""
        return round(x ** (1/3)) ** 3 == x

    def is_triangular(x):
        """Checks if the number is a triangular number (1, 3, 6, 10, ...)."""
        n = (8 * x + 1) ** 0.5 - 1
        return n == int(n)

    def has_even_number_of_digits(x):
        """Checks if the number has an even number of digits."""
        return len(str(x)) % 2 == 0

    def has_odd_number_of_digits(x):
        """Checks if the number has an odd number of digits."""
        return len(str(x)) % 2 != 0

    def has_all_different_digits(x):
        """Checks if all the digits in the number are unique (no repeated digits)."""
        return len(set(str(x))) == len(str(x))

    def is_palindrome(x):
        """Checks if the number is a palindrome (reads the same backward as forward)."""
        return str(x) == str(x)[::-1]

    def is_within_range(x, min_value, max_value):
        """Checks if the number falls within a specified range (inclusive)."""
        return min_value <= x <= max_value

    def is_power_of_2(x):
        """Checks if the number is a power of 2 (e.g., 2, 4, 8, 16)."""
        return x > 0 and (x & (x - 1)) == 0
    
    def is_prime(n):
      """Checks if a number is prime."""
      if n <= 1:
        return False 

      for i in range(2, n):
        if n % i == 0:
          return False  

      return True  
    
    def delLast(self):
        if self.isEmpty(): return
        if self.head.next == None:
            temp = self.head.data
            self.head = None 
            self.size = 0
            return temp
        cur = self.head
        while cur.next.next:
            cur = cur.next
        temp = cur.data
        cur.next = None
        self.tail = cur
        self.size -=1
        return temp

    def addIndex1(self,name , age , index):
        if (index < 0 ): return
        if (index == 0):
            self.addFirst(name,age)
            return
        count = 0
        cur = self.head
        while cur :
            if (index == count):
                break
            count +=1
            cur = cur.next
        if  cur == None:
            if (index==count):
                self.addLast(name,age)
            else:
                return
        else:
            temp = cur.data
            cur.data = Student(name,age)
            node = Node(temp)
            node.next = cur.next
            cur.next = node
            self.size += 1
            
        #end def
            
    def delIndex(self,index):
        if index < 0 : return
        if index == 0: return self.delFirst()
        count = 0
        cur = self.head
        while cur :
            if index == count + 1:
                break
            count += 1
            cur = cur.next
        if cur == None or cur.next == None :
            return
        elif cur.next.next == None:
            return self.delLast()
        else :
            temp = cur.next.data
            cur.next = cur.next.next
            self.size -= 1
            return temp

    def findIndex(self,k):
        count = 0
        cur = self.head
        index = 0
        post = 0
        while cur:
            if count == k:
                return index
            index += 1
            if self.check(cur.data.Age):
                count += 1
                post = index
            cur = cur.next
        if k == -1:
            return post
        else:
            return -1
    
    def sort(self):
        if self.isEmpty() or self.head == self.tail : return
        i = self.head
        while i.next :
            j = i.next
            while j:
                if i.data.Age > j.data.Age :
                    temp = i.data
                    i.data = j.data
                    j.data = temp
                j = j.next
            i = i.next

    def sortEven(self):
        if self.isEmpty() or self.head == self.tail : return
        i = self.head
        while i.next :
            j = i.next
            while j:
                x1 = i.data.Age
                x2 = j.data.Age
                change = False
                if self.is_even(x1) and self.is_even(x2) :
                    if x1>x2:
                        change = True
                    elif x1 == x2:
                        if i.data.Name < j.data.Name:
                            change = True
                    if change:
                    temp = i.data
                    i.data = j.data
                    j.data = temp
                j = j.next
            i = i.next
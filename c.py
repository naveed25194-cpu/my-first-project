# class A:
#     def __init__(self, name):
#         self.name = name
#     def display(self):
#         print("Hello," + self.name)
    
#     def Reg_No(self, reg_no):
#         print("My Reg No is " + reg_no)

#     def sum(self, a, b):
#         print(a + b)

# a = A("Naveed")
# a.display()
# a.Reg_No("25194")
# a.sum(5, 10)

# class B(A):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#     def display(self):
#         print("Hello," + self.name + "Your" + "age is" + self.age)
# b = B("Naveed", '20')
# b.display()



# Add two arrays representing numbers digit by digit
# def add_arrays(num1, num2):
#     length = len(num1)
#     result = [0] * (length + 1)
#     carry = 0

#     # Process each digit from right to left
#     for i in range(length - 1, -1, -1):
#         digit_sum = num1[i] + num2[i] + carry
#         result[i + 1] = digit_sum % 10  # Store ones place
#         carry = digit_sum // 10  # Calculate carry for next iteration

#     result[0] = carry  # Store final carry
#     return result

# print(add_arrays([1, 2, 3], [4, 5, 6]))  # Output: [0, 5, 7, 9]






# Fibbonacci series up to a given limit
# # Start
# n = int(input("Enter the limit: "))
# a = 0
# b = 1
# print(a)

# while b <= n:
#     print(b)
#     c = a + b
#     a = b
#     b = c
# # Stop


# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk

# def is_palindrome(number):
#     return str(number) == str(number)[::-1]

# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# def check_palindrome():
#     number = entry_number.get()
#     if number.isdigit():
#         if is_palindrome(int(number)):
#             messagebox.showinfo("Result", f"{number} is a palindrome!")
#         else:
#             messagebox.showinfo("Result", f"{number} is not a palindrome.")
#     else:
#         messagebox.showerror("Error", "Please enter a valid number.")

# def find_gcd():
#     num1 = entry_num1.get()
#     num2 = entry_num2.get()
#     if num1.isdigit() and num2.isdigit():
#         result = gcd(int(num1), int(num2))
#         messagebox.showinfo("Result", f"The GCD of {num1} and {num2} is {result}.")
#     else:
#         messagebox.showerror("Error", "Please enter valid numbers.")

# def animate_bg(colors, index=0):
#     color = colors[index]
#     root.config(bg=color)
#     index = (index + 1) % len(colors)
#     root.after(500, animate_bg, colors, index)

# root = tk.Tk()
# root.title("Palindrome and GCD Checker")
# root.geometry("400x300")

# colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#A133FF"]
# animate_bg(colors)

# style = ttk.Style()
# style.configure("TButton", font=("Helvetica", 12), padding=10)
# style.configure("TLabel", font=("Helvetica", 12))

# frame_palindrome = ttk.Frame(root)
# frame_palindrome.pack(pady=10)

# label_number = ttk.Label(frame_palindrome, text="Enter a number:")
# label_number.pack(side=tk.LEFT, padx=5)

# entry_number = ttk.Entry(frame_palindrome)
# entry_number.pack(side=tk.LEFT, padx=5)

# button_check = ttk.Button(frame_palindrome, text="Check Palindrome", command=check_palindrome)
# button_check.pack(side=tk.LEFT, padx=5)

# frame_gcd = ttk.Frame(root)
# frame_gcd.pack(pady=10)

# label_num1 = ttk.Label(frame_gcd, text="Enter first number:")
# label_num1.pack(side=tk.LEFT, padx=5)

# entry_num1 = ttk.Entry(frame_gcd)
# entry_num1.pack(side=tk.LEFT, padx=5)

# label_num2 = ttk.Label(frame_gcd, text="Enter second number:")
# label_num2.pack(side=tk.LEFT, padx=5)

# entry_num2 = ttk.Entry(frame_gcd)
# entry_num2.pack(side=tk.LEFT, padx=5)

# button_gcd = ttk.Button(frame_gcd, text="Find GCD", command=find_gcd)
# button_gcd.pack(side=tk.LEFT, padx=5)

# root.mainloop()





number = int(input("Enter the number to check: "))

original_number = number
reversed_number = int(str(number)[::-1])

if original_number == reversed_number:
    print("This is a palidrome number")
else:
    print("This is not a palidrome number")


number_large = int(input("Enter the large number to check ➡️ "))
number_small = int(input("Enter the small number to check ➡️ "))

while number_small !=0 :
    number_large,number_small = number_small, number_large % number_small
print(number_large)




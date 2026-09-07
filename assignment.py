#Matorwa Victor K.
#REG.No R254334H

#QUESTION NUMBER 1

while True:
    try:
        age = int(input('[ENTER YOUR AGE]'))
        print('[YOUR AGE IS]', age)
        break
    except ValueError:
        print('Invalid input, please enter the correct value')


#QUESTION NUMBER 2

with open("fruits.txt", "w")as file:
    print('[THE FRUITS]')
    file.write('Matohwe\n')
    file.write('Mazhanje\n')
    file.write('Tsvubu\n')
    file.write('Masau\n')
    file.write('Matamba\n')
  
with open("fruits.txt", "r")as file:
    for line in file:
        print(line.strip())

#QUESTION NUMBER 3

students = {
    "Kufa":"17",
    "Chamunorwa":"54",
    "Chimudende":"48",
    "Madenyaya":"67",
    "Madekufa":"78"
         }
print('[STUDENT MARKS]')
for student in students:
    print(students[student])

highest_mark = 0
top_student =""

for student in students:
    mark =int(students[student])

    if mark > highest_mark:
        highest_mark = mark
        top_student = student

print("THE BEST STUDENT IS:", student)

#QUESTION (3ii)

class Book():
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print('Title:', self.title)
        print('Author:', self.author)
        print('Price:', self.price)
#creating instances
book1 = Book('Readers Sunrise', 'Shelton Stifla', 11)
book2 = Book(' Tambaoga', 'Yeukai Tinotenda', 10)
print('[BOOKS]')
book1.display_details()
book2.display_details()

#QUESTION NUMBER 4: 

def find_peak_usage(logs):
    counts = [0] * 24 
    for log in logs:
        dt = datetime.fromisoformat(log)
        hour = dt.hour
        counts[hour] = counts[hour] + 1 
        max_logins = max(counts)
        return counts.index(max_logins)

logs = [
    "2025-09-03T08:16:40",
    "2025-09-05T07:12:11",
    "2025-09-03T13:07:44",
    "2025-09-03T12:22:18",
    "2025-09-05T11:15:01",
    "2025-09-05T14:11:50"
]

print('PEAK HOUR =', find_peak_usage(logs))

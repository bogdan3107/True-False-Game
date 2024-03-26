import csv
question = ""
indexes = []
with open('Questions.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    questions = [row for row in reader]
    for q in questions:
        question = q[0]
        #print(question)

print(questions)

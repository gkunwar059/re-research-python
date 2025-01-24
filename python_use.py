# """
# To ignore the defined varaiable please
# """

# data = [(1, "one"), (2, "two"), (3, "three")]

# for a, _ in data:
#     print(a)

# # _______________


# # lambda function


# people = [
#     {"name": "Ganesh", "age": 21},
#     {"name": "Ram", "age": 20},
#     {"name": "Shyam", "age": 22},
# ]

# # use the lambda to sort the list of the dictonaries by the age filed

# people.sort(key=lambda person: person["age"])
# print(people)
# "learn when required , this approach is defiend when needed "
# for person in people:
#     print(f"{person['name']} is {person['age']} years old")

# # ZIP le 2 ota list lai join garxa create a pair banaunxa hai

# student = ["nitesh", "david", "ganesh"]
# grade = [99, 98, 97]
# nic_name = ["nitu", "dabu", "ganu"]

# """
# here it just create a pair from the above existing list   #NEED-FULL

# """
# for s, g, n in zip(student, grade, nic_name):
#     print(f"{s} : {g} : {n}")

# "Yesle common field lanxa hai -- pair count garx list ko value haru pani count garxa"

# print(list(zip(student, grade, nic_name)))  #key-value pair here


# student_grade={}
# student_grade=student_grade.setdefault("Ram",19)    #use need to make the key value in dict you can    #key is important and you can use anything too 
# student_grade["age"]=21  # set key value in dict above 
# student_grade["name"]="ganesh"
# student_grade=student_grade.get("gender",5) # get method first search the gender that it doesnot find then set the --Male, second parameter works for the set 
# print(student_grade)



# numbers=[1,2,3,4,55,6,7,8,9,10]
# print(*numbers,sep=" ")     # unpacking the list all the and print

# print(numbers,end="5gfdjkagda")

#negative indexing of the list

# events=["pre_execute","post_execute","pre_run_cell","post_run_cell"]
# print(events[::-1])

# for event in events[::-1]:   # reverse
#     print(event)


# if else statement in one line 
age=21
print("You are eligible to vote") if age>=18 else print("You are not eligible to vote")


age=21
smoke=True

#ternary operator
can_smoke= "poor" if age>60 and smoke else ("rich" if age >21 and not smoke else "young")
print(can_smoke)
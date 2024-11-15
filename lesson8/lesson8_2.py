import random 

def get_names(num:int=2)->list[str] :
    with open("names.txt",encoding="utf-8",) as file:
        names_str = file.read()
    names= names_str.split(sep="\n")
    names= random.choices(names,k=num)
    return names

def generate_names(names:list[str]) -> list[dict]:
    students:list[dict] =[]
    for student in names :
        chinese = random.randint(50,100)
        english = random.randint(50,100)
        math    = random.randint(50,100)
        score = {"name":student,"chinese":chinese,"english":english,"math":math}
        students.append(score)
    return students

num = int(input("請輸入學生的數量(最多十位)"))
nums:list[str] = get_names(num=num)
students:list[dict] = generate_names(names=nums)
print(students)
import random

Film = ("film class")
ps = ("public space class")
m = ("minecraft workshop")
b = ("bookmaking class")

Mary = ("Mary", Film)

Shane = ("Shane", ps)

Alder = ("Alder", ps)

Logan  = ("Logan", Film)

Solyana = ("Solyana", ps)

Kj = ("Korbin", ps)

Lindsy = ("Lindsy", Film)

Chiron = ("Chiron", ps)

Ilan = ("Ilan", ps)

studentamchoices = [Mary, Shane, Ilan, Alder, Lindsy, Logan, Kj, Chiron, Solyana]

psclass = []

fclass = []

psclass2 = []

fclass2 = []

for student in studentamchoices:
    if student[1] == ps:
        psclass.append(student[0])
    if student[1] == ps:
        fclass.append(student[0])

Mary2 = ("Mary", m)

Shane2 = ("Shane", m)

Alder2 = ("Alder", m)

Logan2  = ("Logan", m)

Solyana2 = ("Solyana", b)

Kj2 = ("Korbin", m)

Lindsy2 = ("Lindsy", b)

Chiron2 = ("Chiron", m)

Ilan2 = ("Ilan", m)

mclass = []

bclass = []

mclass2 = []

bclass2 = []

studentpmchoices = [Mary2, Shane2, Ilan2, Alder2, Lindsy2, Logan2, Kj2, Chiron2, Solyana2]

for student in studentpmchoices:
    if student[1] == ps:
        mclass.append(student[0])
    if student[1] == ps:
        bclass.append(student[0])

if len(psclass)>5:
    psclass2 = random.sample(psclass, 5)

if len(fclass)>5:
    fclass2 = random.sample(fclass, 5)

if len(mclass)>5:
    mclass2 = random.sample(mclass, 5)

if len(bclass)>5:
    bclass2 = random.sample(bclass, 5)

print("these are the people in the Minecraft class", mclass2)

print("these are the people in the Public space class", psclass2)

print("these are the people in the Film class", fclass2)

print("these are the people in the Book making class", bclass2)

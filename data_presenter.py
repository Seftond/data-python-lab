import matplotlib.pyplot as plt
import numpy as np

file = open('CupcakeInvoices.csv')
#3
for line in file:
    print(line)

file.seek(0)


#4
for line in file:
    line = line.rstrip('\n').split(',')
    print(line[2])

file.seek(0)

#5
total = 0
for line in file:
    line = line.rstrip('\n').split(',')
    total = float(line[3]) * float(line[4])
    total = round(total, 2)
    print(total)

file.seek(0)

#6
total = 0
for line in file:
    line = line.rstrip('\n').split(',')
    total = total + (float(line[3]) * float(line[4]))

total = round(total, 2)
print(total)

file.seek(0)

#part 3
chocolate_total = 0
strawberry_total = 0
vanilla_total = 0

for line in file:
    line = line.rstrip('\n').split(',')
    if line[2] == "Chocolate":
        chocolate_total = chocolate_total + (float(line[3]) * float(line[4]))
    elif line[2] == "Strawberry":
        strawberry_total = strawberry_total + (float(line[3]) * float(line[4]))
    elif line[2] == "Vanilla":
        vanilla_total = vanilla_total + (float(line[3]) * float(line[4]))
chocolate_total = round(chocolate_total, 2)
strawberry_total = round(strawberry_total, 2)
vanilla_total = round(vanilla_total, 2)

chocolate_profits = [chocolate_total]
strawberry_profits= [strawberry_total]
vanilla_profits = [vanilla_total]

labels = ['Types']

x = np.arange(len(labels))
width = .35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, chocolate_profits, width, label='Chocolate')
rects2 = ax.bar(x +  width, strawberry_profits, width, label='Strawberry')
rects3 = ax.bar(x, vanilla_profits, width, label='Vanilla')


ax.set_ylabel('Profits')
ax.set_title('Profits by type')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)

fig.tight_layout()

plt.show()



file.close()
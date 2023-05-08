from generate_random_phrase import generate_random_phrase
from HashTable import HashTable
import random
import matplotlib.pyplot as plt


values = [100, 1000, 5000, 10000, 20000]
max_length = 20
results = {}
table_size = 100

for value in values:
    keys = [generate_random_phrase(max_length) for _ in range(value)]
    ht = HashTable(table_size)
    for key in keys:
        ht.insert(key)

    index = random.randint(0, value - 1)
    (result, operations) = ht.search(keys[index])
    results[value] = operations

print(results)
fig, ax = plt.subplots(1, 1, figsize=(
    8, 6), layout='constrained')
fig.suptitle(
    f"Search on different data sizes", fontsize=16)
fig.tight_layout(pad=5.0)
fig.subplots_adjust(left=0.15,
                    bottom=0.1,
                    right=0.9,
                    top=0.87,
                    wspace=.3)
ax.grid(zorder=0)
ax.plot([0, 100], [0, results[100]], color='g',
        label='100 elements', linewidth=2.5, marker='o')
ax.plot([0, 100], [0, results[1000]], color='r',
        label='1000 elements', linewidth=2.5, marker='o')
ax.plot([0, 100], [0, results[5000]], color='b',
        label='5000 elements', linewidth=2.5, marker='o')
ax.plot([0, 100], [0, results[10000]], color='m',
        label='10000 elements', linewidth=2.5, marker='o')
ax.plot([0, 100], [0, results[20000]], color='k',
        label='20000 elements', linewidth=2.5, marker='o')
ax.set_ylabel('Operations')
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False)  # labels along the bottom edge are off
ax.legend()
plt.show()

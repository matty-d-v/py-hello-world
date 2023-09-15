grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)

print()

for count, item in enumerate(grocery):
  print(count, item)

print()

# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)
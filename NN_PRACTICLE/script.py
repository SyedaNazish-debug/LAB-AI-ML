import os

cat_count = len(os.listdir("dataset1/cat"))
dog_count = len(os.listdir("dataset1/dog"))

print("Cat images:", cat_count)
print("Dog images:", dog_count)
print("Total images:", cat_count + dog_count)
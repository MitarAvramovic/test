a = "hello"
print(type(a))
b = 400
print(type(b))
c = True
print(type(c))
d = None
print(type(d))
f = 400

# print(f"Ovo je string {a}")

# if b is f:
#     print("Y")
# else:
#     print("N")

# for n in range(10):
#     print(n)

# list (MUTABLE)

l1 = ["jedan", "dva", "tri"]

print(type(l1))

l1[0] = "one"

l1.append("cetiri")  # ["one", "dva", "tri", "cetiri"]

for item in l1:
    print(item)

print(l1[:2])
print(l1[1:3])

l2 = [l1[:3]]

l3 = l1[::]

print(l3)

# tuple # (IMUTABLE)

t1 = (1, 2)  # t1 = 1, 2

print(type(t1))

print(t1)

# dict # key / value pairs (MUTABLE)

d1 = {"jedan": 1, "dva": 2, "tri": 3}
print(type(d1))
print(d1)
d1["tri"] = 100
print(d1["tri"])
print(d1.keys())
print(d1.values())

for k, v in d1.items():
    d1[k] += 100

print(d1)

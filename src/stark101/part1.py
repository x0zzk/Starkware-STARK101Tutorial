from field import FieldElement

FieldElement(3221225472) + FieldElement(10)

a = [FieldElement(1), FieldElement(3141592)]
while len(a) < 1023:
    a.append(a[-2] * a[-2] + a[-1] * a[-1])
print(a)
len(a)

g = FieldElement.generator() ** (3 * 2 ** 20)
print(g)


# previous_char = ""
# result = highest_result = 0
# for sequence in (dna_sequence := input()):
#     if sequence == previous_char:
#         result += 1
#     else:
#         highest_result = max(highest_result, result)
#         result = 1
#     previous_char = sequence
# highest_result = max(highest_result, result)
#
# print(highest_result)

# dna_sequence = input()
# d = {k:0 for k in"ACGT"}
# for s in "ACGT":
#     d[s] += dna_sequence.count(s)
# print(max(d.values()))

pc = ""
r = hr = 0
for s in input():
    r = r + 1 if s == pc else 1
    hr = max(hr, r)
    pc = s

print(hr)

# n = int(input())
# sequence = input()

# missing_number = n

# for s, i in zip(sorted(map(int, sequence.split())), range(1, n + 1)):
#     if s != i:
#         missing_number = i
#         break

# print(missing_number)

# n = int(input())
# sequence = input()

# missing_number = n

# for i, s in enumerate(sorted(map(int, sequence.split())), start=1):
#     if s != i:
#         missing_number = i
#         break

# print(missing_number)

n=input()
print(([*(i+1for i,s in enumerate(sorted(map(int,input().split())))if 1+i!=s)]or[n])[0])

# print("c49trg11")
# Hinh9
# n = 5
# for dong in range(1,n):
#     for cot in range(2*n):
#         if (dong+cot>=n+1) and (dong<=cot) :
#             print("* ",end='')
#         else:
#             print("  ",end='')
#     print("")

# Hinh10 - fixed
# n = 5
# for dong in range(1,n+1):
#     for cot in range(1,2*n):
#         if (dong+cot<=2*n) and (dong<=cot):
#             print("* ",end='')
#         else:
#             print("  ",end='')
#     print("")

# Hinh11 - fixed
# n = 5
# for dong in range(1,n+1):
#     for cot in range(1,2*n):
#         if dong==n or (dong+cot==n+1) or cot-dong==n-1:
#             print("* ",end='')
#         else:
#             print("  ",end='')
#     print("")

# Hinh12 - fixed
# n = 5
# for dong in range(1,n+1):
#     for cot in range(1,2*n):
#         if dong==1 or (dong==cot) or dong+cot==2*n:
#             print("* ",end='')
#         else:
#             print("  ",end='')
#     print("")

# Hinh13 - fixed
# n = 5
# for dong in range(1,2*n):
#     for cot in range(1,n+1):
#         if dong==cot or dong+cot==2*n or cot == 1 :
#             print("* ",end='')
#         else:
#             print("  ",end='')
#     print("")

# Hinh14 - fixed
# n = 5
# for dong in range(1,2*n):
#     for cot in range(1,n+1):
#         if dong+cot==n+1 or dong-cot==n-1 or cot==n:
#             print("* ",end='')
#         else:
#             print("  ",end='')
#     print("")

# Hinh15 - fixed
# n = 5
# for dong in range(1,2*n):
#     for cot in range(1,n+1):
#         if dong>=cot and dong+cot<=2*n:
#             print("* ",end='')
#         else:
#             print("  ",end='')
#     print("")

# Hinh16 - fixed
# n = 5
# for dong in range(1,2*n):
#     for cot in range(1,n+1):
#         if dong+cot>=n+1 and dong-cot<=n-1:
#             print("* ",end='')
#         else:
#             print("  ",end='')
#     print("")


import matplotlib.pyplot as plt

def enumerate_two_dice_sum():
    comb_list = []
    for i in range(1, 7):
        for j in range(1, 7):
            comb_list.append(i + j)
    return comb_list


sums = enumerate_two_dice_sum()
plt.hist(sums, bins=range(1, max(sums)+2), density=True)
plt.show()


# def enumerate_dice(num_dice):
    
#     if num_dice == 1:
#         return range(1, 7)
#     else:
#         my_list = enumerate_dice(num_dice - 1)

#         dice_list = []

#         for i in range(1, 7):
#             for item in my_list:
#                 dice_list.append(i + item)
        
#         return dice_list


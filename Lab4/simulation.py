import random
import matplotlib.pyplot as plt


# Tar antalet tärningar som input och returnerar summan av n kast
def roll_dice_sum(num_dice):
    return sum([random.randint(1, 6) for _ in range(num_dice)])


# Tar antalet tärningar (1-6) och försök som input och returnerar
# en lista med summor
def simulate_dice_sum(num_dice, trials):
    return [roll_dice_sum(num_dice) for _ in range(trials)]


sums = simulate_dice_sum(2, 100000)
plt.hist(sums, bins=range(1, max(sums)+2), density=True)
plt.show()

# Tar antalet tärningar (1-6) och försök som input och returnerar
# en lista med antalet försök som har en viss summa 
def simulate_dice_sum_hist(num_dice, trials):
    # Skapa lista med summor för försöken
    sum_list = [roll_dice_sum(num_dice) for _ in range(trials)]

    # Skapa tom lista med nollor
    hist_list = [0] * (6*num_dice + 1)

    # Loopa igenom listan och räkna ut antalet försök med i som summa
    for i in range(len(hist_list)):
        hist_list[i] = sum_list.count(i)
    
    # Normalisera genom att dela antalet försök med totalt antal försök
    hist_list = [item/trials for item in hist_list]
    return hist_list


y = simulate_dice_sum_hist(2, 100000)
x = [i for i in range(0, len(y))]
plt.bar(x, y, tick_label=x)
plt.show()

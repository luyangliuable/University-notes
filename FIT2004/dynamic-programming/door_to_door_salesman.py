def door_to_door(houses: int, price: list):
    total_profit = [0]*houses

    prev = None
    for i in range(len(price)):
        for j in range( len(price)):
            if prev != None and i != prev + 1:
                total_profit[j] = max(total_profit[j], total_profit[i] + price[j])

                print(total_profit)

            prev = i

    return total_profit


price = [50, 10, 12, 65, 40, 95, 100, 12, 20, 30]
house = 10

door_to_door(house, price)



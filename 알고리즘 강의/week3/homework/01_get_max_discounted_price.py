shop_prices = [30000, 2000, 1500000] 
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort()
    coupons.sort()
    sum = 0
    for i in range(len(shop_prices)):
        if not coupons:
            sum += prices[-1]
        else:
            sum += prices[-1] * ((100 - coupons[-1])/100)
            
            prices.pop()
            coupons.pop()
       
    return int(sum)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
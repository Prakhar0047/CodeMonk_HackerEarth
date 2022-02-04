from dis import dis
from multiprocessing.spawn import old_main_modules


def taxi_cost(distance, online, offline):
    online_cost = online[0]+(distance-online[1])*online[2]
    offline_cost = offline[1]+(distance/4)*offline[2]+distance*offline[3]

    if online_cost < offline_cost:
        print("Online Taxi")
    else:
        print("Classic Taxi")

D = int(input())
CostFirstDistance = list(map(int,input().split()))
SpeedBasefareMinuteDistance = list(map(int,input().split()))
taxi_cost(D,CostFirstDistance,SpeedBasefareMinuteDistance)
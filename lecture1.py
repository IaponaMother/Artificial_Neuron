#1 задание
# import random
# r = int(input())
# n = int(input())
# k = int(input())
# l = [random.randint(n, k) for i in range(r)]
# print(l)


#2 задание
# import random
# print(list(map(lambda x: x + random.choice([1, -1]) if x % 2 == 0 else x, l)))


#3 задание
# N = int(input())
# m = [i for i in range(2, N + 1) if i % 2 == 0]
# print(m)


#4 задание
# import pandas as pd
# df = pd.read_csv('test.csv')
#1 print(df.loc[df['Age'] > 50]['Name'])

#2 print(df.max()['Age'] - df.min()['Age'])

#3 print(df.mean()['Age'])

#4 men = df.loc[df['Sex'] == 'male']['Name'].count()
# women = df.loc[df['Sex'] == 'female']['Name'].count()
# print(f'{men} - мужчин \n{women} - женщины')
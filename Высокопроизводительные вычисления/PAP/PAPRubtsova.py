import time

#Функция для считывания данных из файла
def read_weights_from_file(filename):
    file = open(filename, 'r')
    data = file.read().strip().split(',')
    count = int(data[0])
    weights = list(map(int, data[1:]))
    if len(weights) != count:
        raise ValueError("Количество весов не соответствует указанному количеству предметов.")
    return weights
    
#Функиця проверки на разделение
def can_partition(nums):
    total_sum = sum(nums)

    # Если сумма всех элементов нечетная, то разделить
    # пополам невозможно
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    n = len(nums)

    # Создаем таблицу для динамического программирования
    dp = [False] * (target + 1)
    dp[0] = True

    # Обновляем таблицу dp
    for num in nums:
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True

    return dp[target]
    

#Main 
filename = "weights.txt"

try:
  start_time = time.time()
  weights = read_weights_from_file(filename)
  end_time = time.time()
  time = end_time - start_time
  print('Веса: ', weights)
  print('Время затраченное на чтение: ',time)
  if can_partition(weights):
    print("Можно разделить на две группы с равной суммой весов.")
  else:
    print("Невозможно разделить на две группы с равной суммой весов.")
except Exception as e:
  print(f"Произошла ошибка: {e}")
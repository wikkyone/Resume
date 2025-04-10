import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


def website_analyse(file_path):
    data = pd.read_csv(file_path)
    lists_mean = np.mean(data["Просмотренные страницы"])
    print(f"1) Среднее количество просмотренных таблиц: {lists_mean}")
    std_time = np.std(data["Время на сайте (сек)"])
    print(f"2) Стандартное отклонение: {std_time}")
    time_mean = np.mean(data["Время на сайте (сек)"])
    var_co = std_time/time_mean
    var_status = ""
    if var_co > 0.25: var_status = "Высокая вариабельность"
    elif var_co <= 0.25 & var_co > 0.1: var_status = "Умеренная вариабельность"
    elif var_co <= 0.1: var_status = "Слабая вариабельность"
    print(f"3) {var_status}: {var_co}")  
    mobile = data[data["Тип устройства"] == "Мобильное"]["Просмотренные страницы"]
    desktop = data[data["Тип устройства"] == "Десктоп"]["Просмотренные страницы"]
    t_stat, p_value = ttest_ind(mobile, desktop)
    p_status = ""
    if p_value > 0.05: p_status = "Есть статистически значимая разница в количестве страниц"
    else: p_status = "Нет статистически значимой разницы"
    print(f"{p_status}: {p_value}")  
website_analyse('website_visits_december_2024.csv')
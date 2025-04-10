from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import root_mean_squared_error
import pandas as pd


def lin_regression(file_name):
    data = pd.read_csv(file_name)
    #data.info() использовали для проверки пропущенных значений
    #"Engine HP" "Engine Cylinders" ("Number of Doors","Market Category", не входит в наши предикторы) 
    target = data['MSRP']
    predictors = data[["Year","Engine HP","Engine Cylinders","highway MPG","city mpg","Popularity"]]
    predictors_non_null = predictors.fillna(predictors.mean())
    #использую random_state=11 для удобства проверки результатов работы программы
    predictors_train, predictors_test, target_train, target_test = train_test_split(predictors_non_null, target, train_size=0.75, random_state=11)
    model = LinearRegression()
    model.fit(predictors_train, target_train)
    result = model.predict(predictors_test)
    #я использовал метод "root_mean_squared_error", а не mean_squared_error, так как в задании необходимо рассчитать именно RMSE
    rmse = root_mean_squared_error(target_test, result)
    dull_model = [target_train.mean()] * len(target_test)
    rmse_dull = root_mean_squared_error(target_test, dull_model)
    print(f"RMSE модели: {rmse}\nRMSE глупой модели: {rmse_dull}\nRMSE модели - RMSE глупой модели: {rmse - rmse_dull}")
lin_regression("data.csv") 
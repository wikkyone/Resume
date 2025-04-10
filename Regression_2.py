import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import recall_score 
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

def table_preprocessing(filename):

    data = pd.read_csv(filename)   
    data = data.drop("Booking_ID", axis=1) 
    labelencoder = LabelEncoder()
        
    # Преобразование категориальных переменных
    data["type_of_meal_plan"] = labelencoder.fit_transform(data["type_of_meal_plan"])
    data["room_type_reserved"] = labelencoder.fit_transform(data["room_type_reserved"])
    data["market_segment_type"] = labelencoder.fit_transform(data["market_segment_type"])
    data["booking_status"] = labelencoder.fit_transform(data["booking_status"])

    X = data.drop("booking_status", axis=1)
    Y = data["booking_status"]
    return X, Y

def hotel_booking_analyze(X, Y):
    #Стандантизируем данные, тк из-за логистической регрессии программа превышает количество итераций
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.25, random_state=42)
    
    #Логистическая регрессия
    lreg = LogisticRegression()
    lreg.fit(X_train, Y_train)
    y_lreg_pred = lreg.predict(X_test)

    # Дерево решений
    clf_tree = DecisionTreeClassifier()
    clf_tree.fit(X_train, Y_train)
    y_clf_tree_pred = clf_tree.predict(X_test)

    # SVC
    svc = SVC()
    svc.fit(X_train, Y_train)
    y_svc_pred = svc.predict(X_test)

    # Расчет метрик
    rec_lreg = recall_score(Y_test, y_lreg_pred)
    rec_clf = recall_score(Y_test, y_clf_tree_pred)
    rec_svc = recall_score(Y_test, y_svc_pred)

    return f"Бинарная логистическая регрессия: {rec_lreg}. Дерево решений: {rec_clf}. SVC: {rec_svc}."

X, Y = table_preprocessing("hotel_reservations.csv")
result = hotel_booking_analyze(X, Y)
print(result)

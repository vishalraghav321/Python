from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4],[5]]
y = [40,50,60,70,80]

model = LinearRegression()
model.fit(X, y)

h = float(input("Hours: "))
print("Predicted Marks:", model.predict([[h]])[0])

import pandas
import numpy
import matplotlib.pyplot as pyplot
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pandas.read_csv('employee_login_attempt_data.csv')
print(data)

x = data[['Login_Attempts']]
y = data['Security_Risk_Score']

poly = PolynomialFeatures(degree=2)
polynomial_x = poly.fit_transform(x)

model = LinearRegression()
model.fit(polynomial_x,y)
predicted_y = model.predict(polynomial_x)

pyplot.figure(figsize = (12,8))
pyplot.title('Polynomial Regression: Login Attempts vs Security Risk Score')
pyplot.scatter(x,y,color='blue',label='actual data')
pyplot.scatter(x,predicted_y,color='red',label='predicted data')

x_sorted = numpy.sort(x.values, axis=0)
x_sorted_poly = poly.transform(x_sorted)
y_sorted_pred = model.predict(x_sorted_poly)
pyplot.plot(x_sorted, y_sorted_pred, color='green', linewidth=2, label='Regression Line')

pyplot.xlabel('Login Attempts')
pyplot.ylabel('Security Risk Score')
pyplot.legend()
pyplot.show()

r2 = model.score(polynomial_x, y)
print("R2 Score:", r2)

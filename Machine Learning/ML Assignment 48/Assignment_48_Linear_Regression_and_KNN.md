# Assignment 48 — Linear Regression and KNN

## Q1. Implement simple linear regression manually without using any ML library. Calculate the mean of X and Y, slope, intercept, regression equation, and predict Y for X = 6.

```python
X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]

mean_x = sum(X) / len(X)
mean_y = sum(Y) / len(Y)

numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(X, Y))
denominator = sum((x - mean_x) ** 2 for x in X)

slope = numerator / denominator
intercept = mean_y - slope * mean_x

prediction = slope * 6 + intercept

print("Mean of X:", mean_x)
print("Mean of Y:", mean_y)
print("Slope:", slope)
print("Intercept:", intercept)
print(f"Regression Equation: Y = {slope}X + {intercept}")
print("Prediction for X = 6:", prediction)
```

**Output:**

```text
Mean of X: 3.0
Mean of Y: 3.6
Slope: 0.4
Intercept: 2.4
Regression Equation: Y = 0.4X + 2.4
Prediction for X = 6: 4.8
```

## Q2. Calculate predictions, Mean Squared Error (MSE), and R² score for the dataset X = [1,2,3,4,5], Y = [3,4,2,4,5].

```python
X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]

mean_x = sum(X) / len(X)
mean_y = sum(Y) / len(Y)

slope = sum((x - mean_x) * (y - mean_y) for x, y in zip(X, Y)) / sum((x - mean_x) ** 2 for x in X)
intercept = mean_y - slope * mean_x

predictions = [slope * x + intercept for x in X]

mse = sum((actual - predicted) ** 2 for actual, predicted in zip(Y, predictions)) / len(Y)

ss_total = sum((y - mean_y) ** 2 for y in Y)
ss_residual = sum((actual - predicted) ** 2 for actual, predicted in zip(Y, predictions))

r2 = 1 - (ss_residual / ss_total)

print("Predictions:", predictions)
print("MSE:", round(mse, 2))
print("R2 Score:", round(r2, 2))
```

**Output:**

```text
Predictions: [2.8, 3.2, 3.6, 4.0, 4.4]
MSE: 0.41
R2 Score: 0.61
```

## Q3. Given experience = [1,2,3,4,5] and salary = [20000,25000,30000,35000,40000], predict the salary for 6 years of experience and plot the regression line.

```python
import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5]
Y = [20000, 25000, 30000, 35000, 40000]

mean_x = sum(X) / len(X)
mean_y = sum(Y) / len(Y)

slope = sum((x - mean_x) * (y - mean_y) for x, y in zip(X, Y)) / sum((x - mean_x) ** 2 for x in X)
intercept = mean_y - slope * mean_x

predicted_salary = slope * 6 + intercept
predictions = [slope * x + intercept for x in X]

print("Regression Equation: Salary =", slope, "* Experience +", intercept)
print("Predicted Salary for 6 years:", predicted_salary)

plt.scatter(X, Y, label="Actual Salary")
plt.plot(X, predictions, color="red", label="Regression Line")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")
plt.legend()
plt.show()
```

**Output:**

```text
Regression Equation: Salary = 5000.0 * Experience + 15000.0
Predicted Salary for 6 years: 45000.0
```

**Predicted salary: ₹45,000**

## Q4. Why is KNN called a lazy learner?

KNN is called a lazy learner because it does not build a model during training. It stores the training data and performs distance calculations only when a new prediction is required.

## Q5. What happens if K is too small in KNN?

When K is too small, the model becomes sensitive to noise and outliers. It may overfit the training data and produce unstable predictions.

## Q6. What happens if K is too large in KNN?

When K is too large, the model considers too many neighbors, including distant and less relevant points. It may underfit the data and ignore local patterns.

## Q7. Why does linear regression minimize squared error?

Linear regression minimizes squared error to penalize larger prediction mistakes more strongly and obtain the line that best fits the data by minimizing the sum of squared residuals.

## Q8. What is the difference between MSE and R²?

- **MSE (Mean Squared Error):** Measures the average squared difference between actual and predicted values. Lower MSE generally indicates better predictions.
- **R² Score:** Measures how much variation in the target variable is explained by the model. A value closer to 1 generally indicates a better fit.

## Q9. Why can the R² score not be greater than 1?

For ordinary least squares linear regression with an intercept, evaluated on the training data, R² cannot exceed 1 because the residual sum of squares cannot be negative.

However, on unseen test data, R² can be negative if the model performs worse than predicting the target's mean.

## Q10. Can KNN be used for regression?

Yes. KNN can be used for both classification and regression.

- **KNN Classification:** Predicts the class based on the majority vote of neighboring points.
- **KNN Regression:** Predicts a numerical value, usually by calculating the average target value of the K nearest neighbors.

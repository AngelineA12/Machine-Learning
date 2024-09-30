# -*- coding: utf-8 -*-
"""2348409_Lab3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YKmywYJey77grAzCTt9Uc39mfwBUF7Ft

**Lab 03- LINEAR REGRESSION**

* *Created by: Angeline A*
* *Reg No: 2348409*

* Edited on: 29/02/2024

In the below code,
* import pandas as pd:
 *  This line imports the Pandas library and assigns it the alias pd.
 *  Pandas is a powerful library for data manipulation and analysis in Python.
 *  By importing it as pd, you can use pd as a shorthand when calling Pandas functions.

* import numpy as np:
 * This line imports the NumPy library and assigns it the alias np.
 * NumPy is a library for numerical computing with Python, providing support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.
 * By importing it as np, you can use np as a shorthand when calling NumPy functions.

* import matplotlib.pyplot as plt:
 * This line imports the pyplot module from the Matplotlib library and assigns it the alias plt.
 *  Matplotlib is a plotting library for creating static, animated, and interactive visualizations in Python.
 * By importing pyplot as plt, you can use plt as a shorthand when calling Matplotlib's plotting functions.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""In the below code,
* pd.read_csv():
 * This is a Pandas function used to read data from a CSV file.
* '/content/happyscore_income.csv':
 * This is the file path pointing to the location of the CSV file.
 * In this case, it seems like the CSV file is located in the '/content' directory.
* df:
 * This is the variable name chosen to store the data read from the CSV file.
 * It's a common convention to name it df, short for DataFrame, when working with Pandas.
"""

df = pd.read_csv('/content/Salary Data.csv')

"""In the below code, I am storing the Years of Experience and the Salary of the particular person in the variable df."""

df = df[['YearsExperience','Salary']]
print(df)

"""In the below code,
* plt.scatter(df['YearsExperience'],df['Salary']):
 * This line creates a scatter plot using the scatter() function from Matplotlib's pyplot module (plt).
 * It takes two main arguments: the x-values (df['YearsExperience']) and the y-values (df['Salary']).
 * This plots each data point with the x-coordinate being the Years of experience and the y-coordinate being the Salary.

* plt.xlabel("YearsExperience"):
 * This line sets the label for the x-axis of the plot to "Years of Experience" using the xlabel() function.
 * This provides a description of what the x-axis represents.

* plt.ylabel("Salary"):
 * This line sets the label for the y-axis of the plot to "Salary of the respective person" using the ylabel() function.
 * This provides a description of what the y-axis represents.
"""

#Scatter plot
plt.scatter(df['YearsExperience'],df['Salary'])
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

"""From the above graph,
* we can infer that based on the years of experience of the person, their Salary increases.
* Evidence is found from the plot that there is an increase in the Salary of the person based on their Years of Experience

In the below code, we can get the correlation co-efficients of all the variabes available in the dataset.
"""

df.corr()

"""In the above result,
* we can see the correlation between the factors present in the dataset,i.e., Years of Experinece and Salary of the person
* We are going to explore more about the Years of Experience and the Salary of the particular person in deep.

The below code explains,
* A grid of scatterplots showing the relationships between all pairs of numerical variables in the DataFrame df.
* This can be useful for exploring correlations and patterns in the data.
"""

import seaborn as sns
sns.pairplot(df)

"""From the above plot,
* we infer that the scatter plot shows a positive relationship between years of experience and salary.
* This means that as the number of years of experience increases, the salary also tends to increase.
* However, it is important to note that this is just a correlation and does not necessarily mean that there is a causal relationship between the two variables.

In the below code,
* we are defining the independent and dependent variables.
* Here we take Years of Experience of a person as the independent variable and Salary of a person as dependent variable.
* We are storing the indepedent and dependent variable in the variables called x and y.
"""

x = df[['YearsExperience']] #Independent variable
y = df['Salary']  #Dependent Variable

"""In the below code, we
* Extract the Years of Experience (YearsExperience) from the dataframe df.
* The shape of the NumPy array created from the x_series pandas Series.
* It tells us about the dimensions of the array, such as the number of elements along each axis.
"""

x_series = df['YearsExperience']
np.array(x_series).shape

"""From the above code, we can infer that there are 30 no of elements along each axis(rows).

In the below code, we import the function sklearn.model_selection, so that we  can use it to split the dataset into training and testing sets
"""

from sklearn.model_selection import train_test_split

"""In the below code, we can see
* x_train, x_test, y_train, y_test:
 * These variables represent the resulting training and testing sets for the features (input variables) and the target (output variable).
 * The convention is to prefix x_ to the feature sets and y_ to the target sets.

* train_test_split(x, y, test_size=0.25, random_state=42):
 * This function call splits the data into training and testing sets.
 * It takes several arguments:

* x: The features (input variables) of the dataset.
* y: The target variable (output variable) of the dataset.
* test_size:
 * The proportion of the dataset to include in the testing split.
 * Here, it's set to 0.25, meaning 25% of the data will be used for testing, and the remaining 75% will be used for training.
* random_state:
 * This is an optional parameter that controls the random seed used to shuffle the data before splitting.
 * Setting it to a specific value (e.g., 42) ensures reproducibility, as the same random splits will be generated each time the code is run.
"""

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)

""" In the below code,
 * we import sklearn.preprocessing.StandardScaler, so that we can create an instance of StandardScaler and use it to scale our data before feeding it into machine learning algorithms.
 * This preprocessing step can often improve the performance and convergence of machine learning models.
"""

from sklearn.preprocessing import StandardScaler

"""In the below code, we perform,
* The features in the training set (x_train) will be standardized, with each feature having a mean of 0 and a standard deviation of 1.
* This standardized data is often preferred for training machine learning models, as it can lead to improved performance and convergence, especially for algorithms that are sensitive to feature scaling.





"""

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)

"""The below code,
we can get a tuple representing the shape of the array x_train, where the first value indicates the number of rows (samples) and the second value indicates the number of columns (features) in the array.
"""

x_train.shape

"""From the above result, we can infer that there are 22 rows and 1 column in the training dataset for the independent variable, which means 22 values are taken to train the model."""

print(x_train) #Printing the value of x_train

"""* After running the below code, the features in the testing set x_test will be standardized using the mean and standard deviation computed from the training set.
* This ensures that both the training and testing data are scaled consistently, which is important for making accurate predictions with machine learning models.
"""

x_test = scaler.transform(x_test)

x_test

"""In the below code, we get a tuple representing the shape of the array x_test, where the first value indicates the number of rows (samples) and the second value indicates the number of columns (features) in the array."""

x_test.shape

"""From the above result, we can say there are 8 values taken in the test dataset

* After importing the below mentioned sklearn.linear_model.LinearRegression library, we can create an instance of LinearRegression and use it to fit a linear regression model to your data.
* This model can then be used to make predictions or analyze the relationship between the independent and dependent variables in your dataset.
"""

from sklearn.linear_model import LinearRegression

"""In the below code, we see that
* The LinearRegression class from scikit-learn implements linear regression using the least squares method.
* It fits a linear model to the training data by minimizing the residual sum of squares between the observed and predicted target values.

* After creating the LinearRegression instance, you can use it to fit the model to your training data and make predictions on new data.
"""

regression = LinearRegression(n_jobs = -1)

"""After running the below line of code, the regression object will contain the fitted linear regression model, and it can be used to make predictions on new data or evaluate the model's performance."""

regression.fit(x_train,y_train)

"""In the below code,
* we can inspect the learned parameters of the linear regression model, which describe the relationship between the features and the target variable.
* These coefficients and intercept are estimated during the training process to best fit the training data.
"""

print("Regression Co-efficient/Slope: ",regression.coef_)
print("Intercept:",regression.intercept_)

"""From the above code, we infer that,
* Regression Coefficient/Slope:
 * The coefficient represents the slope of the linear relationship between the feature(s) and the target variable.
 * In this case, the coefficient is approximately 25063.15.
 * This means that for every unit increase in the feature(s), the target variable is expected to increase by approximately 25063.15 units, all else being equal.

* Intercept:
 * The intercept represents the value of the target variable when all predictor variables are zero.
 * In this case, the intercept is approximately 70417.41.
 * This means that when all predictor variables are zero, the predicted value of the target variable is approximately 70417.41.

After running the below code,
*  we'll have a scatter plot showing the actual data points from the training set, as well as a line representing the predictions made by the linear regression model.
* This can help you visualize how well the model fits the training data.
"""

plt.scatter(x_train,y_train)
plt.plot(x_train,regression.predict(x_train))
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

"""From the above graph, we can say that there is a positive realtionship between the Years of Experience and the salary of a particular person for the training dataset.

After running the below code,
* y_pred will be an array containing the predicted values of the target variable for the testing set x_test.
* These predicted values can be compared with the actual values (y_test) to evaluate the performance of the linear regression model on unseen data.
"""

y_pred = regression.predict(x_test)

y_pred

"""The above values are the respective Salary values based on the the respective Years of Experience of the person present in the test dataset.

After importing the below function, we can use them to evaluate the performance of the linear regression model by comparing its predictions with the actual target values.
"""

from sklearn.metrics import mean_absolute_error,mean_squared_error

"""In the below code, we are finding the
* Mean Squared Error:
 * Calculates the mean squared error (MSE) between the actual target values (y_test) and the predicted values (y_pred) using the mean_squared_error function imported from sklearn.metrics.
 * MSE measures the average squared difference between the actual and predicted values.
* Mean Absolute Error:
  * Calculates the mean absolute error (MAE) between the actual target values (y_test) and the predicted values (y_pred) using the mean_absolute_error function imported from sklearn.metrics.
  * MAE measures the average absolute difference between the actual and predicted values.
* Root mean Squared Error:
 * Calculates the root mean squared error (RMSE) from the MSE by taking the square root.
 * RMSE is a more interpretable metric than MSE, as it is in the same units as the target variable.

"""

mse = mean_squared_error(y_test,y_pred)
mae = mean_absolute_error(y_test,y_pred)
rmse = np.sqrt(mse)
print("The mean Squared Error:",mse)
print("The mean Absolute Error: ",mae)
print("The root mean Squared Error is: ",rmse)

"""* The MAE value of approximately 5056.99 indicates that, on average, the model's predictions are off by around Rs 5056.99.
* The RMSE value of approximately 6229.17 provides an estimate of the typical difference between the predicted and actual values. Since RMSE is larger than MAE, it suggests that there are some larger errors in the predictions that contribute to the overall error.
* The MSE value of approximately 38802588.99 is relatively large, indicating that there may be some outliers or larger errors in the predictions.
* In summary, the model's predictions have a relatively high error rate, as indicated by the values of MSE, MAE, and RMSE. This suggests that the model may not be accurately capturing all the underlying patterns in the data, and there may be room for improvement in the model's performance. Further analysis and refinement of the model may be necessary to improve its accuracy.

After importing the below function, we can use it to compute the R-squared score to evaluate the performance of our regression model.
"""

from sklearn.metrics import r2_score

"""For the below code,
* The R-squared score ranges from 0 to 1, where a score closer to 1 indicates that the model explains a larger proportion of the variance in the target variable, while a score closer to 0 indicates that the model does not explain much of the variance.

* Therefore, the printed score represents how well the linear regression model fits the testing data, with higher scores indicating better model performance.
"""

score = r2_score(y_test,y_pred)
print("The Score is:", score)

"""From the above result, we get The R-squared score of approximately 0.9347 indicates that the linear regression model explains approximately 93.47% of the variance in the target variable on the testing set

The adjusted R-squared formula in the below code,
* Adjusts the R-squared value based on the number of predictors and observations in the model.
* It penalizes the R-squared value for using a larger number of predictors, which helps prevent overfitting.
"""

adjusted_r_squared = 1 - (1 - score) * (len(y_test) - 1) / (len(y_test) - x_test.shape[1] - 1)
print("The Adjusted R-Squared is:", adjusted_r_squared)

"""From the above result, we can infer that
* A high adjusted R-squared value, such as 0.9238, suggests that the linear regression model provides a good fit to the testing data, even after accounting for the number of predictors in the model.
* This indicates that the model's predictions closely match the actual values and that the model effectively captures the underlying patterns in the data.

After importing statsmodels,
* we can use it to perform Ordinary Least Squares (OLS) linear regression and analyze the results.
* This library provides more detailed statistics and information about the regression model, including coefficient estimates, p-values, confidence intervals, and more.
"""

#OLS Linear Regression
import statsmodels.api as sm

"""After running the below code, model will contain the fitted OLS regression model, which can be used to obtain summary statistics and analyze the results of the regression."""

model = sm.OLS(y_train,x_train).fit()

"""After running the below code,
* Prediction will be an array containing the predicted values of the target variable for the testing set x_test.
* These predicted values can be compared with the actual values (y_test) to evaluate the performance of the OLS regression model on unseen data.
"""

prediction = model.predict(x_test)
print(prediction)

"""* It's important to note that some predicted values appear to be negative, which might not make sense depending on the context of your data.
* Negative predictions can occur in certain situations, especially when dealing with extrapolation beyond the range of observed data or when the model is not well-suited to the underlying patterns in the data.

* We may want to further evaluate the performance of the OLS regression model and investigate any unexpected predictions to ensure the model's validity and reliability.

The model summary in the below code provides valuable insights into the performance and significance of the regression model, helping us interpret the results and assess the reliability of the estimated coefficients.
"""

print(model.summary())

"""From the above results, we can infer the following,
* Dependent Variable: Salary

* R-squared (uncentered):
 *  The R-squared value measures the proportion of the variance in the dependent variable (Salary) explained by the independent variable(s).
 * In this case, the uncentered R-squared value is 0.112, indicating that approximately 11.2% of the variance in Salary is explained by the independent variable(s).

* Adjusted R-squared (uncentered):
 * The adjusted R-squared value adjusts the R-squared value based on the number of predictors in the model.
 * It is a more conservative measure of model fit. Here, the adjusted R-squared (uncentered) is 0.070.
* F-statistic:
 * The F-statistic tests the overall significance of the regression model. It measures whether at least one of the predictors has a non-zero coefficient.
 * The F-statistic is 2.645, and the associated probability (Prob (F-statistic)) is 0.119, which indicates that the model's overall fit is not statistically significant at the conventional significance level of 0.05.

* Coefficients:
 * The coefficient represents the estimated effect of the independent variable(s) on the dependent variable.
 * Here, the coefficient for x1 (the independent variable) is 2.506e+04 (approximately 25060), with a standard error of 1.54e+04 (approximately 15400).
 * The t-statistic tests the null hypothesis that the coefficient is equal to zero, and the associated p-value (P>|t|) indicates the statistical significance of the coefficient.
 * In this case, the p-value is 0.119, which is greater than 0.05, suggesting that the coefficient is not statistically significant at the conventional significance level.

In the below code , we predicting the Salary of a person by giving some random Years Of Experience
"""

# Scale the input feature(s) using the scaler
scaled_input = scaler.transform([[12]])

# Make a prediction using the scaled input feature(s)
predicted_salary = model.predict(scaled_input)

# Print the predicted salary
print("Predicted Salary:", predicted_salary)

"""From the above result,
* We can say that the model prediction about the Salary of the person who is having 12 years of Experience in his field is Rs 65513.91130, which is not a correct detail.
* The model needs to be developed/taken care more to improve the results.
* The reason for this is because the data has many outliers.

The below code predicts the Salary of a person based on their experience.
"""

regression.predict(scaler.transform([[12]]))

"""From the above result, we can see that the predicted Salary for 12years of experience is Rs137930.32039 which is correct."""
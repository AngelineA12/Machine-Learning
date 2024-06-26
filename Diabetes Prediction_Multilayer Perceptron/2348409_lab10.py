# -*- coding: utf-8 -*-
"""2348409_Lab10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wMUYiRhNOkC4UxC8g98G9Ajp_19KipzQ

**Multi-Layer Perceptron**

***LAB 10***
* *Created by: Angeline A*
* *Reg No: 2348409*
* *3-MDS 'B'*
* Submitted on: 19/04/2024

In the below code, we are importing the necessary datasets for performing mathematical operations, data manipulation and data visualization.
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

"""In the below code, we are loading the dataset into the runtime environment of colab and reading the dataset and storing it the the variable diabetes_data."""

diabetes_data = pd.read_csv("/content/diabetes.csv")
diabetes_data

"""The below code tells us the basic information about the dataset."""

# Display basic information about the dataset
print("Number of samples:", diabetes_data.shape[0])
print("Number of features:", diabetes_data.shape[1])
print("\nData types of features:")
print(df.dtypes)

"""From the above result,
* Number of samples:
  * It prints the total number of rows in the dataset, which represents the number of samples or instances.
  * In this case, the dataset contains 768 samples.
* Number of features:
  * It prints the total number of columns in the dataset, excluding the target variable.
  * Each column represents a feature or attribute of the dataset.
  * In this case, the dataset contains 9 features.
* Data types of features:
  * It prints the data types of each feature in the dataset.
  * This information is helpful for understanding the nature of the data and determining any necessary data preprocessing steps.
  * In this case, the features include integer and float data types, indicating numerical data.
  * The target variable (Outcome) is also included in the list, which is of integer data type.

The below code snippet returns the first five rows of the dataset.
"""

# Display the first few rows
print("\nFirst few rows of the dataset:")
diabetes_data.head()

"""In the below code snippet we are storing the numerical variables in a seperate variable."""

# Univariate Analysis for numerical variables
numerical_variables = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

"""In the below code, we are getting the statistical information about the dataset."""

# Calculate basic descriptive statistics
print("\nDescriptive statistics for numerical variables:")
diabetes_data[numerical_variables].describe()

"""From the above result, we can infer that,
* Pregnancies:
  * The 'Pregnancies' feature in the dataset represents the number of pregnancies each individual has experienced.
  * On average, individuals have undergone approximately 3.85 pregnancies, with a standard deviation of 3.37, indicating some variability in pregnancy numbers.
  * The range of pregnancies varies from 0 to 17, with the majority falling within 1 to 6 pregnancies.
* Glucose:
  * The 'Glucose' feature denotes the glucose concentration levels in the blood of individuals.
  * The mean glucose level is approximately 120.89 mg/dL, with a standard deviation of 31.97, reflecting a considerable spread in glucose concentrations among the population.
  * Glucose levels range from 0 to 199 mg/dL, with most values concentrated between 99 and 140 mg/dL.
* BloodPressure:
  * 'BloodPressure' represents the systolic blood pressure measurements of individuals.
  * The average blood pressure is around 69.11 mm Hg, with a standard deviation of 19.36.
  * Blood pressure values range from 0 to 122 mm Hg, with the majority clustered between 62 and 80 mm Hg.
* SkinThickness:
  * The 'SkinThickness' feature signifies the thickness of skin folds on individuals' bodies.
  * On average, skin thickness is approximately 20.54 mm, with a standard deviation of 15.95.
  * Skin thickness varies widely, ranging from 0 to 99 mm, with a notable number of observations falling within the range of 0 to 32 mm.
* Insulin:
  * 'Insulin' levels represent the concentration of insulin in individuals' blood serum.
  * The mean insulin level is approximately 79.80 μU/ml, with a significant standard deviation of 115.24, indicating substantial variability in insulin concentrations.
  * Insulin levels range from 0 to 846 μU/ml, with the majority of observations concentrated at lower values.
* BMI:
  * The 'BMI' feature denotes individuals' Body Mass Index, calculated from their weight and height measurements.
  * The average BMI is around 31.99 kg/m^2, with a standard deviation of 7.88.
  * BMI values range from 0 to 67.1 kg/m^2, with most falling within the range of 27.3 to 36.6 kg/m^2.
* DiabetesPedigreeFunction:
  * 'DiabetesPedigreeFunction' represents a function that scores the likelihood of diabetes based on family history.
  * On average, this function scores approximately 0.47, with a standard deviation of 0.33, suggesting some variability in the likelihood scores.
  * The range of scores varies from 0.078 to 2.42, with the majority falling below 1.
* Age:
  * The 'Age' feature indicates the age of individuals in years.
  * The average age is approximately 33.24 years, with a standard deviation of 11.76, reflecting some variability in ages among the population.
  * Age ranges from 21 to 81 years, with most individuals falling between 24 and 41 years old.

The below code generates a grid of histograms, with each histogram representing the distribution of values for a specific numerical variable in the dataset.
"""

# Visualize the distribution using histograms
plt.figure(figsize=(15, 10))
for i, var in enumerate(numerical_variables):
    plt.subplot(3, 3, i+1)
    sns.histplot(diabetes_data[var], kde=True)
    plt.title(var)
plt.tight_layout()
plt.show()

"""From the shapes of the histograms and KDE lines, we can make a few observations about the distributions of these variables:

* Pregnancies: This histogram shows a right-skewed distribution, indicating that a higher number of observations have fewer pregnancies, with counts decreasing as the number of pregnancies increases.

* Glucose: The distribution appears to be approximately normal with a slight right skew, centering around a range that could be considered a typical blood glucose level.

* BloodPressure: The histogram for blood pressure also looks roughly normal with a slight right skew. There is a peak where most of the observations are concentrated, which could represent an average blood pressure reading for this population.

* SkinThickness: This variable also shows a right-skewed distribution with a long tail to the right. The data has a concentration of lower values with fewer observations of higher skin thickness.

* Insulin: The distribution of insulin is highly right-skewed, with most observations having lower insulin levels and very few observations with high insulin levels.

* BMI: The BMI histogram appears to be approximately normally distributed with a slight right skew. There's a noticeable central peak where most values are concentrated.

* DiabetesPedigreeFunction: This variable shows a highly right-skewed distribution with a long tail, indicating that most observations have lower values for the diabetes pedigree function.

* Age: The age distribution is right-skewed, indicating a younger population with fewer older individuals in the sample.

The below code generates a grid of kernel density plots, with each representing the distribution of values for a specific numerical variable in the dataset.
"""

# Visualize the distribution using kernel density plots
plt.figure(figsize=(12, 8))
for i, column in enumerate(diabetes_data.columns[:-1]):
    plt.subplot(3, 3, i + 1)
    sns.kdeplot(data=diabetes_data, x=column, fill=True)
    plt.title(f"{column} Distribution")
plt.tight_layout()
plt.show()

"""Here's a brief description of each plot based on their titles:

* Pregnancies Distribution:
  * This histogram shows the distribution of the number of pregnancies among a population.
  * It is skewed to the right, indicating that most of the data falls on the lower end of the scale (fewer pregnancies).

* Glucose Distribution:
  * This plot illustrates the distribution of glucose levels.
  * The data seems normally distributed with a peak around 100-125 mg/dL, which could potentially indicate the average blood glucose levels in this cohort.

* BloodPressure Distribution:
  * The distribution of blood pressure readings among the population is displayed here.
  * The histogram is roughly bell-shaped, suggesting a normal distribution around the 60-80 mmHg range.

* SkinThickness Distribution:
  * This histogram shows the distribution of skin thickness measurements.
  * It is right-skewed, with a peak at the lower end of the scale.

* Insulin Distribution:
  * The insulin distribution histogram is also right-skewed, meaning most values are on the lower end but there are some higher values as well.

* BMI Distribution:
  * The Body Mass Index (BMI) distribution is fairly normally distributed with the bulk of the values centered around 20-40.

* DiabetesPedigreeFunction Distribution:
  * This histogram represents the distribution of a metric called the Diabetes Pedigree Function.
  * The data is right-skewed, indicating that most individuals have lower values for this metric.

* Age Distribution:
  * Lastly, the age distribution histogram shows that a larger portion of the population is on the younger side, with fewer individuals in the older age brackets.

The below code generates a grid of box plots, with each box plot representing the distribution of values for a specific feature in the dataset.
"""

# Visualize the distribution using box plots
plt.figure(figsize=(12, 8))
for i, column in enumerate(diabetes_data.columns[:-1]):
    plt.subplot(3, 3, i + 1)
    sns.boxplot(data=diabetes_data, y=column)
    plt.title(f"{column} Distribution")
plt.tight_layout()
plt.show()

"""Here's what can be noted from each box plot in general terms:

* Pregnancies Distribution: This plot indicates the distribution of the number of times pregnant. The median is around 3, with a few outliers indicated by dots.

* Glucose Distribution: The distribution of glucose concentrations in the blood. The median glucose level is roughly in the mid-to-high 100s (mg/dl), with some outliers on both the lower and higher ends.

* BloodPressure Distribution: This displays the distribution of blood pressure measurements. The median appears to be around 70–80 mmHg, with a few outliers.

* SkinThickness Distribution: The distribution of skin fold thickness measurements. The median is near the lower end of the range, with a wide spread and some outliers.

* Insulin Distribution: This shows the distribution of insulin levels. There are many outliers, and the median is close to the lower end of the data range.

BMI Distribution: BMI, or Body Mass Index, has its distribution showcased here. The median BMI is around the high 20s to low 30s, which suggests a population that may range from normal weight to overweight, with some outliers.

* DiabetesPedigreeFunction Distribution: This plot represents some form of a diabetes pedigree function score. The median is closer to the lower end, with several outliers on the upper side.

* Age Distribution: The distribution of ages is shown, with the median age appearing to be in the late 20s to the early 30s, and with fewer outliers compared to other metrics.

The below code snippet generates a pair plot that allows for a visual exploration of the relationships between pairs of numerical variables in the dataset.
"""

# Bivariate Analysis
# Explore relationships between pairs of numerical variables using scatter plots or pair plots
sns.pairplot(diabetes_data)
plt.suptitle("Pairplot of Numerical Variables", y=1.02)
plt.show()

"""The diagonal of the grid typically shows histograms, which are the distributions of individual variables. Off-diagonal plots are scatter plots representing the relationship between two variables — one variable plotted on the X-axis and the other on the Y-axis.

Looking into more detail:

* Histograms: These show the frequency distribution of a single variable. Taller bars represent a higher frequency of that value or range of values in the dataset.

* Scatter Plots: These plots reveal patterns or correlations between two variables. If the points form a discernible line or curve, it indicates a relationship between the X and Y axes variables.

The below code snippet calculates the correlation coefficients between numerical variables and visualizes them using a heatmap, providing insights into the relationships and dependencies among the variables in the dataset.
"""

# Calculate correlation coefficients between numerical variables
correlation_matrix = diabetes_data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

"""In this heatmap:

* The colors range from dark blue to dark red, indicating the strength and direction of the correlation. Dark red signifies a strong positive correlation, dark blue signifies a strong negative correlation, and white or lighter colors represent a low or no correlation.
* The variables included in the matrix are Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI (Body Mass Index), DiabetesPedigreeFunction, Age, and Outcome.
* Diagonal cells (from the top left to the bottom right) are all colored dark red, indicating a perfect positive correlation of 1. This is typical for correlation matrices because it's where each variable intersects with itself.
* The 'Outcome' variable is likely the presence or absence of diabetes, as it has varying degrees of correlation with other variables. Notably, it has a moderately positive correlation with Glucose, which is a critical factor in diabetes.

In the below code, we are seperating the independent and dependent variables.
"""

# Separate the features (X) and the target variable (y)
X = diabetes_data.drop(columns=['Outcome'])
y = diabetes_data['Outcome']

"""In the below code we are importing library to perform the standardization."""

# Perform Standardization or normalization on the features as required
from sklearn.preprocessing import StandardScaler

"""This code performs standardization on the features of the dataset using the StandardScaler from Scikit-learn to bring all the features to a similar scale which improves the performance and convergence of the model."""

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

"""In the below code we are importing library necessary for splitting the dataset into training and splitting."""

# Split the dataset into training and testing sets
from sklearn.model_selection import train_test_split

"""In the below code snippet, we are splitting the dataset into training and testing of the independent and dependent variable"""

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

"""In the below code, we are printing the shape of the independent and dependent variables of training and testing dataset."""

# Display the shapes of the training and testing sets
print("Shape of X_train:", X_train.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of y_train:", y_train.shape)
print("Shape of y_test:", y_test.shape)

"""From the result we can see that,
* Shape of X_train: (614, 8):
  * This line indicates that the training set for the features (X_train) has a shape of (614, 8).
  * The shape (614, 8) means that there are 614 samples (rows) in the training set, and each sample has 8 features (columns).
* Shape of X_test: (154, 8):
  * This line indicates that the testing set for the features (X_test) has a shape of (154, 8).
  * The shape (154, 8) means that there are 154 samples (rows) in the testing set, and each sample has 8 features (columns).
* Shape of y_train: (614,):
  * This line indicates that the training set for the target variable (y_train) has a shape of (614,).
  * The shape (614,) means that there are 614 samples (rows) in the training set for the target variable, and there is only one column (representing the target variable).
* Shape of y_test: (154,):
  * This line indicates that the testing set for the target variable (y_test) has a shape of (154,).
  * The shape (154,) means that there are 154 samples (rows) in the testing set for the target variable, and there is only one column (representing the target variable).

The below code imports the necessary components for building an MLP classifier, evaluating its performance using various metrics, and performing PCA for dimensionality reduction if needed. These components are essential for developing and evaluating machine learning models effectively.
"""

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.decomposition import PCA

"""The below code initializes and trains a Multilayer Perceptron (MLP) classifier with specified parameters using the training data. The trained model can then be used to make predictions on new data."""

# a. Train the MLP model using the training data
mlp_model = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='adam', random_state=46)
mlp_model.fit(X_train, y_train)

"""The below code snippet evaluates and prints the training and testing accuracy scores of the MLP model, providing insights into its performance on both the training and testing datasets."""

# b. Evaluate the performance of the trained model using appropriate metrics
train_accuracy = mlp_model.score(X_train, y_train)
test_accuracy = mlp_model.score(X_test, y_test)
print("Training Accuracy:", train_accuracy)
print("Testing Accuracy:", test_accuracy)

"""Here's an explanation of the results:

* Training Accuracy: 0.8159609120521173:
  * The training accuracy is approximately 81.60%.
  * This indicates that the MLP model correctly classified around 81.60% of the instances in the training dataset.
  * A training accuracy of 81.60% suggests that the model is performing reasonably well on the data it was trained on.
  * However, it's essential to consider whether this level of accuracy is sufficient for the specific task and domain.
* Testing Accuracy: 0.7597402597402597:
  * The testing accuracy is approximately 75.97%.
  * This indicates that the MLP model correctly classified around 75.97% of the instances in the testing dataset.
  * The testing accuracy provides an estimate of how well the model generalizes to new, unseen data.
  * A testing accuracy of 75.97% suggests that the model's performance on unseen data is slightly lower than its performance on the training data.
  * This is expected, as models typically perform better on data they were trained on compared to unseen data.

The provided code snippet is suggesting to vary the number of hidden layers and neurons in the Multilayer Perceptron (MLP) classifier and tune hyperparameters. Specifically, it suggests trying different configurations of hidden layer sizes.
"""

# c. Vary the number of hidden layers and neurons and tune hyper-parameters
# For example, try different hidden layer sizes
hidden_layer_sizes = [(50,), (100,), (50, 50), (100, 50)]

"""This code initializes variables to keep track of the best accuracy achieved during hyperparameter tuning and the corresponding best model configuration."""

best_accuracy = 0
best_model = None

"""The below code iterates over different configurations of hidden layer sizes, trains MLP models with each configuration, evaluates their performance on the testing data, and keeps track of the best performing model configuration (best_model) along with its accuracy (best_accuracy). At the end of the loop, best_model will contain the best MLP model configuration, and best_accuracy will contain its corresponding accuracy score."""

for hidden_layers in hidden_layer_sizes:
    mlp_model = MLPClassifier(hidden_layer_sizes=hidden_layers, activation='relu', solver='adam', random_state=42)
    mlp_model.fit(X_train, y_train)
    test_accuracy = mlp_model.score(X_test, y_test)

    if test_accuracy > best_accuracy:
        best_accuracy = test_accuracy
        best_model = mlp_model

print("Best Testing Accuracy:", best_accuracy)
print("Best Model Configuration:", best_model)

"""From the above result,
* Best Testing Accuracy: 0.7597402597402597:
  * This line indicates the best testing accuracy achieved during the hyperparameter tuning process.
  * The value displayed, approximately 0.7597, represents the highest accuracy score obtained among all tested model configurations on the testing data.
  * The testing accuracy provides an estimate of how well the model generalizes to new, unseen data.
* Best Model Configuration: MLPClassifier(random_state=42):
  * This line indicates the configuration of the best performing model that corresponds to the highest testing accuracy.
  * The displayed model configuration, MLPClassifier(random_state=42), specifies the Multilayer Perceptron (MLP) classifier with a single hidden layer, using the default values for activation function ('relu'), solver ('adam'), and a random state of 42.
  * While the displayed configuration is minimal and does not provide detailed information about the hidden layer sizes or other hyperparameters, it represents the best-performing model configuration found during the hyperparameter tuning process.

The below code snippet evaluates the performance of the best performing model on the testing data and provides a classification report and confusion matrix, allowing for a detailed analysis of the model's performance in terms of precision, recall, and confusion between classes.
"""

# e. Display the classification report and confusion matrix
y_pred = best_model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

"""From the above result we can infer that, Let's interpret each part:

* Classification Report:
  * Precision:
    * Precision measures the accuracy of positive predictions.
    * In this context:
      * Precision for class 0 (non-diabetic) is approximately 0.81, indicating that 81% of instances predicted as non-diabetic are actually non-diabetic.
      * Precision for class 1 (diabetic) is approximately 0.67, indicating that 67% of instances predicted as diabetic are actually diabetic.
  * Recall:
    * Recall measures the proportion of actual positives that were correctly identified.
    * In this context:
      * Recall for class 0 is approximately 0.82, indicating that 82% of actual non-diabetic instances were correctly classified as non-diabetic.
      * Recall for class 1 is approximately 0.65, indicating that 65% of actual diabetic instances were correctly classified as diabetic.
  * F1-score:
    * F1-score is the harmonic mean of precision and recall, providing a balance between the two metrics.
    * In this context:
      * F1-score for class 0 is approximately 0.81.
      * F1-score for class 1 is approximately 0.66.
  * Support:
    * Support indicates the number of actual occurrences of each class in the test data.
    * In this context, there are 99 instances of class 0 and 55 instances of class 1.
  * Accuracy:
    * Accuracy is the proportion of correctly classified instances among all instances.
    * The overall accuracy of the model is approximately 0.76, or 76%.
  * Macro Avg:
    * Macro average calculates the average of precision, recall, and F1-score across all classes.
  * Weighted Avg:
    * Weighted average calculates the average of precision, recall, and F1-score, weighted by the support of each class.
* Confusion Matrix:
  * The confusion matrix provides a tabular representation of the model's predictions versus the actual labels.
  * In this confusion matrix:
    * The top-left cell (81) represents true negatives (TN), indicating the number of non-diabetic instances correctly classified as non-diabetic.
    * The top-right cell (18) represents false positives (FP), indicating the number of non-diabetic instances incorrectly classified as diabetic.
    * The bottom-left cell (19) represents false negatives (FN), indicating the number of diabetic instances incorrectly classified as non-diabetic.
    * The bottom-right cell (36) represents true positives (TP), indicating the number of diabetic instances correctly classified as diabetic.

The below code snippet performs PCA to reduce the dimensionality of the feature space to 4 principal components and applies the transformation to both the training and testing datasets, resulting in reduced-dimensional representations of the original data. This reduction can help improve model efficiency and mitigate the curse of dimensionality while preserving most of the variance in the dataset.
"""

# Apply PCA
pca = PCA(n_components=4)  # Assuming to reduce to 4 principal components
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

"""The below code snippet develops an MLP classifier with a specified architecture and trains it using the training data transformed by PCA. The resulting model (mlp_model_pca) is then ready to be used for making predictions on new data. Applying PCA before training the MLP model can help reduce the dimensionality of the feature space and potentially improve the model's performance and computational efficiency."""

# g. Develop / apply MLP Classifier after PCA model
mlp_model_pca = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='adam', random_state=24)
mlp_model_pca.fit(X_train_pca, y_train)

"""The below code snippet evaluates and prints the training and testing accuracies of the MLP model after PCA dimensionality reduction, providing insights into its performance on both the training and testing datasets. Comparing these accuracies with those obtained without PCA can help assess the impact of dimensionality reduction on the model's performance."""

# h. Observe the variations in the performance of the trained model after PCA using appropriate metrics
train_accuracy_pca = mlp_model_pca.score(X_train_pca, y_train)
test_accuracy_pca = mlp_model_pca.score(X_test_pca, y_test)
print("Training Accuracy after PCA:", train_accuracy_pca)
print("Testing Accuracy after PCA:", test_accuracy_pca)

"""Here's an explanation of the results:

* Training Accuracy after PCA: 0.755700325732899:
  * This line indicates the training accuracy of the MLP model after PCA dimensionality reduction.
  * The value, approximately 0.7557, represents the proportion of correctly classified instances in the training data after reducing its dimensionality with PCA.
  * A training accuracy of 0.7557 means that around 75.57% of the instances in the training dataset were classified correctly by the model after PCA dimensionality reduction.
* Testing Accuracy after PCA: 0.7207792207792207:
  * This line indicates the testing accuracy of the MLP model after PCA dimensionality reduction.
  * The value, approximately 0.7208, represents the proportion of correctly classified instances in the testing data after reducing its dimensionality with PCA.
  * A testing accuracy of 0.7208 means that around 72.08% of the instances in the testing dataset were classified correctly by the model after PCA dimensionality reduction.

The below code snippet evaluates and prints the classification report and confusion matrix for the MLP model after applying PCA dimensionality reduction. These metrics provide insights into the model's performance, including precision, recall, F1-score, and confusion between classes, after reducing the dimensionality of the feature space using PCA.
"""

# Display the classification report and confusion matrix after PCA
y_pred_pca = mlp_model_pca.predict(X_test_pca)
print("Classification Report after PCA:")
print(classification_report(y_test, y_pred_pca))
print("Confusion Matrix after PCA:")
print(confusion_matrix(y_test, y_pred_pca))

"""The provided output consists of the classification report and confusion matrix for the MLP model after applying PCA (Principal Component Analysis) dimensionality reduction. Let's interpret each part:

* Classification Report after PCA:
  * Precision:
    * Precision measures the accuracy of positive predictions.
    * In this context:
      * Precision for class 0 (non-diabetic) is approximately 0.76, indicating that 76% of instances predicted as non-diabetic are actually non-diabetic.
      * Precision for class 1 (diabetic) is approximately 0.62, indicating that 62% of instances predicted as diabetic are actually diabetic.
  * Recall:
    * Recall measures the proportion of actual positives that were correctly identified.
    * In this context:
      * Recall for class 0 is approximately 0.82, indicating that 82% of actual non-diabetic instances were correctly classified as non-diabetic.
      * Recall for class 1 is approximately 0.55, indicating that 55% of actual diabetic instances were correctly classified as diabetic.
  * F1-score:
    * F1-score is the harmonic mean of precision and recall, providing a balance between the two metrics.
    * In this context:
      * F1-score for class 0 is approximately 0.79.
      * F1-score for class 1 is approximately 0.58.
  * Support:
    * Support indicates the number of actual occurrences of each class in the test data.
    * In this context, there are 99 instances of class 0 and 55 instances of class 1.
  * Accuracy:
    * Accuracy is the proportion of correctly classified instances among all instances.
    * The overall accuracy of the model is approximately 0.72, or 72%.
  * Macro Avg: Macro average calculates the average of precision, recall, and F1-score across all classes.
  * Weighted Avg: Weighted average calculates the average of precision, recall, and F1-score, weighted by the support of each class.
* Confusion Matrix after PCA:
  * The confusion matrix provides a tabular representation of the model's predictions versus the actual labels after PCA dimensionality reduction.
  * In this confusion matrix:
    * The top-left cell (81) represents true negatives (TN), indicating the number of non-diabetic instances correctly classified as non-diabetic.
    * The top-right cell (18) represents false positives (FP), indicating the number of non-diabetic instances incorrectly classified as diabetic.
    * The bottom-left cell (25) represents false negatives (FN), indicating the number of diabetic instances incorrectly classified as non-diabetic.
    * The bottom-right cell (30) represents true positives (TP), indicating the number of diabetic instances correctly classified as diabetic.

The below code visualizes the comparison of accuracy scores before and after PCA using a bar plot, allowing for a clear comparison of the performance of the MLP model with and without PCA dimensionality reduction.
"""

# Accuracy scores before and after PCA
accuracy_scores = [accuracy_score(y_test, y_pred), accuracy_score(y_test, y_pred_pca)]
labels = ['Without PCA', 'With PCA']

# Plotting the bar plot
plt.figure(figsize=(8, 6))
plt.bar(labels, accuracy_scores, color=['blue', 'green'])
plt.xlabel('Model')
plt.ylabel('Accuracy Score')
plt.title('Comparison of Accuracy Scores Before and After PCA')
plt.ylim(0.0, 1.0)
plt.show()

"""Upon observation from the above graph,
* It is clear that the bar representing the model without PCA (blue) has achieved a higher accuracy score compared to the bar representing the model with PCA (green). Both accuracy scores are high, but the model without PCA has a higher accuracy score.

* Therefore, the correct conclusion from the bar chart is that the model without PCA achieved a higher accuracy score than the model with PCA. This indicates that in this particular case, the use of PCA did not improve the accuracy of the model and that the original model without PCA performed better in terms of accuracy.
"""
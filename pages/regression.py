import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
import numpy as np

def load_data():

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.title("Regression")

    st.subheader("Data cleaning and preprocessing")

    df = pd.read_csv('data\csv\suicide2019_cleaned.csv')

    st.write("The data has already been cleaned a bit. We have removed some columns like the generation and country-year columns, because we dont need them for the regression part of the analysis. We have also removed the HDI for year column because it had too many missing values. Some of the columns have been converted to a numeric type, so we can use them in our analysis. The column 'sex' and 'age' have been converted to a numeric type.")
    st.write("First 10 rows of the dataset:")
    st.write(df.head(10))

    st.write("Shape:")
    st.write(df.shape)
    st.write("Columns:")
    st.write(df.columns)

    st.write("We will do some additional cleaning for our regression analysis. We will change the column names and make sure that all columns are numeric")
    df.columns = ['country', 'year', 'gender', 'age', 'suicides_no', 'population', 'suicide_100_pop','gdp_year', 'gdp_capita']

    st.write("Changing the column names:")
    st.write(df.columns)

    st.write("Data types:")
    st.write(df.dtypes)

    st.write("We change the column 'GDP_year' to be numeric: ")
    # Ensuring all columns are numeric
    df['gdp_year'] = df['gdp_year'].str.replace(',', '').str.replace('"', '')
    df['gdp_year'] = pd.to_numeric(df['gdp_year'], errors='coerce')

    st.write(df.dtypes)

    st.write("The dataset after the cleaning process:")
    st.write(df.head(5))

    st.divider()

    #######################################################################################################################################

    # CORRELATION MATRIX

    # Dropping country because it is not numeric
    df_numeric = df.drop('country', axis=1)

    # Display correlation matrix
    st.subheader("Correlation Matrix")
    st.write("We are using the correlation matrix to display the correlation coefficients between the different variables. A lot of the variables are close to 0 which means that there are no correlation or a weak correlation between them. Some of the variables, like suicides_no and GPD pr year, do have a correlation closer to 1 which means that there is a stronger positive correlation.")

    correlation_matrix = df_numeric.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="RdBu_r", center=0, linewidths=.5)
    plt.title("Correlation Matrix")
    st.pyplot(plt)

    st.divider()

    #######################################################################################################################################

    st.subheader("Description of the data")

    st.write(df.describe())

    st.divider()

    #######################################################################################################################################

    # Linear regression model based on year and suicides_no

    st.subheader("Regression")

    st.write("We have choosen to group the data by year and sum all of the suicides for that year.")
    st.write("First 30 rows of the new dataset:")

    # First we filter 'year' in the dataset because we dont want 2016 (it is a bad year)
    filtered_year = df[(df['year'] >= 1987) & (df['year'] <= 2015)]

    # Now we group year
    grouped_year = filtered_year.groupby('year')

    # Now we have the sum of suicides for each year 

    suicides_year_sum = grouped_year['suicides_no'].sum()

    st.write(suicides_year_sum.head(30))

    ########################################################################################################################################

    st.write("We will begin by seeing if we can fit a linear regression model on our dataset.")

    suicides_year_sum_reset = suicides_year_sum.reset_index()
    
    X = suicides_year_sum_reset[['year']]
    y = suicides_year_sum_reset['suicides_no']

    # Scatter plot
    fig, ax = plt.subplots()
    ax.scatter(X, y)
    st.write("A scatter plot of the sum of suicides for each year from 1987 to 2015. 2016 is not included because the data is not complete for that year")
    st.pyplot(fig)

    # Calculate linear regression statistics
    slope, intercept, r, p, std_err = stats.linregress(X['year'], y)

    # Linear regression model
    def myfunc(X):
        return slope * X + intercept

    mymodel = list(map(myfunc, X['year']))

    # With the linear regression line
    fig, ax = plt.subplots()
    ax.scatter(X, y)
    ax.plot(X, mymodel, color='red')  

    st.write("Scatter plot with a linear regression line:")

    st.pyplot(fig)

    st.write("Above we can see that the red line represents a linear regression attempt. It is clear that a linear model does not capture the underlying pattern in the data effectively. The line does not align well with the data points, indicating that a linear relationship is not suitable for this dataset. If we contionue with a linear model, we would likely have a low variance and be underfitting our data. We will try a polynomial regression model instead.")

    st.divider()

    ########################################################################################################################################

    st.subheader("Polynomial regression")

    # Polynomial regression model
    st.write("We will now try to fit a polynomial regression model to our data. We will use a 3rd degree polynomial, which is defined as:")
    
    st.latex("f(x) = ax^3 + bx^2 + cx + d")

    X = suicides_year_sum_reset['year'].values
    y = suicides_year_sum_reset['suicides_no'].values

    # Scatter plot
    fig, ax = plt.subplots()
    ax.scatter(X, y)
    st.write("Scatter plot with total suicides from 1987 - 2015:")
    st.pyplot(fig)

    model = np.poly1d(np.polyfit(X, y, 3))

    polyline = np.linspace(1987, 2015, 50)
    
    # Scatter plot after fitting the polynomial regression model
    fig, ax = plt.subplots()
    ax.scatter(X, y)
    ax.plot(polyline, model(polyline), color='red')
    st.write("Scatter plot with a polynomial regression curve:")
    st.pyplot(fig)

    # Test sets and predictions
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # Visualize train and test sets
    fig, ax = plt.subplots()
    ax.scatter(X_train, y_train, label='Train set')
    ax.scatter(X_test, y_test, label='Test set')
    ax.legend()
    st.write("Visualizing the training and testing sets:")
    st.pyplot(fig)

    # Predictions
    y_pred_train = model(X_train)
    y_pred_test = model(X_test)

    # Assuming your polynomial coefficients are stored in the 'model' variable
    a, b, c, d = model.coefficients

    # Our equation based on the coefficients becomes:
    # st.write("The equation for the polynomial regression model based on our data becomes: ")
    # st.latex(f"f(x) = {a:.2f}x^3 + {b:.2f}x^2 + {c:.2f}x + {d:.2f}")

    # Model evaluation

    st.subheader("Model evaluation")
    st.write("What we need to consider about our model to avoid overfitting is: ")
    st.write("- If the model is too complex and fits the training data too well. It will not generalize well to new data.")
    st.write("- If the curve is too complex. Maybe the curve is to wiggly and not smooth")
    st.write("- If the variance in R-squares between the test set and the training set should be minimal. A significant difference suggests potential overfitting")
    

    st.subheader("Evaluation:")

    # We are doing 5 interations because we want to see if the model is overfitting by comparring the R-squared values for the training and test sets
    st.write("We are doing 10 iterations because we want to check if the model is overfitting by comparing the R-squared values for the training and test sets")
    num_iterations = 10

    train_r2_scores = []
    test_r2_scores = []

    for _ in range(num_iterations):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

        # Fit the model (rest of your model fitting code remains the same)
        model = np.poly1d(np.polyfit(X_train, y_train, 3)) 

        # Predictions
        y_pred_train = model(X_train)
        y_pred_test = model(X_test)

        # Store R-squared Values
        train_r2_scores.append(r2_score(y_train, y_pred_train))
        test_r2_scores.append(r2_score(y_test, y_pred_test))

    st.write("R-squared for training sets across iterations:", train_r2_scores) 
    st.write("R-squared for test sets across iterations:", test_r2_scores)

    st.write("Most of the R-sqaures for both the training sets and the test sets are close to 1. This is a good sign because a higher R square score indicates that a larger portion of the variance is captured by the model. However we have to compare the R square from the test set to the training set to see if the model is overfitting. If the R square for the test set is much lower than the training set, it is a sign of overfitting. For the 10 iterations the R square for the test set and training set are generally close. However some of them are not close enough and a few are very far apart, which is a sign of overfitting, so we should consider making a simpler model. We tried to change the degree from '3' to '2' but the r sqaure for the test set was even lower and the difference between the test and training sets were even bigger.")

    st.subheader("Error metrics")
    st.write("We can use the mean squared error (MSE), mean absolute error (MAE) and root mean squared error (RMSE) to evaluate the performance of our model. We will calculate these metrics for both the training and test sets.")

    # Calculate metrics on the test set
    mse = mean_squared_error(y_test, y_pred_test)
    mae = mean_absolute_error(y_test, y_pred_test)
    rmse = np.sqrt(mse)
    st.write("Mean Squared Error (test set):", mse)
    st.write("Mean Absolute Error (test set):", mae)
    st.write("Root Mean Squared Error (test set):", rmse)

    # Calculate metrics on the training set
    mse_train = mean_squared_error(y_train, y_pred_train)
    mae_train = mean_absolute_error(y_train, y_pred_train)
    rmse_train = np.sqrt(mse_train)
    st.write("Mean Squared Error (training set):", mse_train)
    st.write("Mean Absolute Error (training set):", mae_train)
    st.write("Root Mean Squared Error (training set):", rmse_train)

    st.divider()

    #######################################################################################################################################

def show():
    load_data()
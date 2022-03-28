from sklearn.metrics import mean_squared_error

def rmse(y, y_hat):
    return mean_squared_error(y, y_hat) ** 0.5
import math
import random

def is_number(x):
    try:
        float(x)
        return True
    except (ValueError, TypeError):
        return False

def activation_function():
    x = input("Input x = ")
    if not is_number(x):
        raise ValueError("x must be a number")
    
    name = input("Input activation Function (sigmoid|relu|elu): ")
    if name not in ['sigmoid', 'relu', 'elu']:
        raise ValueError(f"{name} function is not supported")
    x = float(x)
    if name == 'sigmoid':
        fx = 1 / (1 + math.exp(-x))
    elif name == 'relu':
        fx = max(0.0, x)
    elif name == 'elu':
        fx = x if x > 0 else 0.01 * (math.exp(x) - 1)
    print(f'{name}: f({x}) = {fx}')
    
def loss_functions():
    """
    Generates random targets and predictions, then computes the specified loss (MAE, MSE, RMSE).
    """
    n = input("Input number of samples (integer number) which are generated: ")
    if not is_number(n):
        raise ValueError("n samples must be an integer")
    n = int(n)

    name = input("Input loss name (MAE|MSE|RMSE): ").upper()
    if name not in ("MAE", "MSE", "RMSE"):
        raise ValueError(f"{name} loss is not supported. Choose MAE, MSE, or RMSE.")

    for i in range(n):
        target = random.uniform(0, 10)
        predict = random.uniform(0, 10)
        if name == "MAE":
            loss = abs(target - predict)
        elif name == "MSE":
            loss = (target - predict) ** 2
        elif name == "RMSE":
            loss = math.sqrt((target - predict) ** 2)
        print(f"{name}: target = {target:.3f}, predict = {predict:.3f}, loss = {loss:.3f}")

def evaluate_f1_components(tp, fp, fn):
    if not all(isinstance(val, int) for val in (tp, fp, fn)):
        raise TypeError("tp, fp, and fn must be integers")
    if tp < 0 or fp < 0 or fn < 0:
        raise ValueError("tp, fp and fn must be >= 0")
    sum_tp_fp = tp + fp
    sum_tp_fn = tp + fn
    if sum_tp_fp == 0 or sum_tp_fn == 0:
        raise ZeroDivisionError("The sum of tp&fp or tp&fn must not be 0")
    precision = tp / sum_tp_fp
    recall = tp / sum_tp_fn
    f1_score = 2 * ((precision * recall) / (precision + recall))
    print (f"precision = {precision:.3f}, recall = {recall:.3f}, f1 = {f1_score:.3f}")
    return precision, recall, f1_score
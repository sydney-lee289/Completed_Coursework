#hannah and i worked together, code should be very similar

import random

file_path = '/Users/sydneylee/Library/CloudStorage/OneDrive-UniversityofMontevallo/FALL 2024 CLASSES/CS 325 AI/ml-100k/u.data'

def transpose(A):
    nRows = len(A[0])
    nCols = len(A)
    AT= []
    for i in range(nRows):
        AT.append([])
        for j in range(nCols):
            AT[i].append(None) 
    
    for i in range(nRows):
        for j in range(nCols):
            AT[i][j] = A[j][i]
    return AT

def dot_function_matrix(A, B):
    nRows = len(A)
    nCols = len(B[0])
    nFeatures = len(A[0]) 
    C= []
    for i in range(nRows):
        C.append([])
        for j in range(nCols):
            C[i].append(None)
    
    for i in range(nRows):
        for j in range(nCols):
            c_ij = 0
            for k in range(nFeatures):
                c_ij += A[i][k]*B[k][j]
            C[i][j] = c_ij
    return C

def dot_function_vector(X, Y):
    Z = 0
    for i in range(len(X)):
        Z += X[i]*Y[i]
    return Z

def matrix_factorization(R, P, Q, K, steps, alpha):
    #print(f"Starting matrix factorization for K = {K}")
    Q = transpose(Q)
    for s in range(steps):
        for i in range(len(R)):
            for j in range(len(R[0])):
                if R[i][j] > 0:
                    Q_j = []
                    for x in range(K):
                        Q_j.append(Q[x][j])
                    R_pred_ij = dot_function_vector(P[i], Q_j)
                    e_ij = R[i][j] - R_pred_ij
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha*2*e_ij*Q[k][j]
                        Q[k][j] = Q[k][j] + alpha*2*e_ij*P[i][k]
        
        error = 0
        for i in range(len(R)):
            for j in range(len(R[0])):
                if R[i][j] > 0:
                    Q_j = []
                    for x in range(K):
                        Q_j.append(Q[x][j])
                    R_pred_ij = dot_function_vector(P[i], Q_j)
                    error = error + pow(R[i][j] - R_pred_ij, 2)
        if error < 0.01:
            break
    return P, Q   

num_users = 943  
#num_users = 100 
num_movies = 1682  
#num_movies = 100         

R = [[0 for _ in range(num_movies)] for _ in range(num_users)]
training_rating = {}

with open(file_path, 'r') as file:
    print("File opened successfully.")
    for line in file:
        user_id, movie_id, rating, _ = line.split('\t')
        user_id = int(user_id) - 1  
        movie_id = int(movie_id) - 1  
        rating = float(rating)
        R[user_id][movie_id] = rating
        if user_id not in training_rating:
            training_rating[user_id] = []
        training_rating[user_id].append(movie_id)

test_data = []
for user_id, rated_movies in training_rating.items():
    if len(rated_movies) >= 20:
        selected_movies = random.sample(rated_movies, 5)
        for movie_id in selected_movies:
            test_data.append(f"{user_id + 1}\t{movie_id + 1}\t{R[user_id][movie_id]}\t0")


with open('u.test', 'w') as test_file:
    for entry in test_data:
        test_file.write(entry + "\n")

steps = 1000
alpha = 0.001
best_k = 0
lowest_error = float('inf')

k_values = [1, 5, 10, 20, 55, 120, 277, 430, 942]
for K in k_values:
    P = [[random.random() for _ in range(K)] for _ in range(num_users)]
    Q = [[random.random() for _ in range(K)] for _ in range(num_movies)]

    nP, nQ = matrix_factorization(R, P, Q, K, steps, alpha)
    nR = dot_function_matrix(nP, nQ)
   
    predicted_missing_values = []


    for i in range(num_users):
        user_predictions_count = 0
        for j in range(num_movies):
            if R[i][j] == 0:  
                predicted_rating = nR[i][j]
                print(f"Predicted rating for user {i + 1} on movie {j + 1}: {predicted_rating:.2f}")
                predicted_missing_values.append((i + 1, j + 1, predicted_rating))
                user_predictions_count += 1 
                if user_predictions_count >= 5:  # Stop after 5 predictions
                    break
#'''

#print('next try pleeeeeeeeeeeease')
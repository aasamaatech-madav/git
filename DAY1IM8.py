
import numpy as np

score_list=[12,45,67,689]

score_array=np.array(score_list)

print("list type: ",type(score_list))
print("array type: ",type(score_array))

result_list=[]

for s in score_list:
    result_list.append(s+10)

print("python list + 10 : ",result_list)


array_result=score_array+10;
print("Numpy array + 10: ",array_result)


import time

size=1_000_000

python_list=list(range(size))
numpy_array=np.arange(size)

start_time=time.time()

result_list=[]

for s in python_list:
   result_list.append(s**2)

list_duration=time.time()-start_time

print(f"python list time: {list_duration:.5f} seconds")

#numpy calculation

start_time=time.time()

array_result=numpy_array**2

array_duration=time.time()-start_time

print(f"numoy array time: {array_duration:.5f} seconds")


#datatype of mumpy arrat=y

nums=np.array([1,2,3,4,5])

print(nums.dtype)

#mixed type of numpy

miced=np.array([1,2.5,"three"])
print(miced.dtype)

#creating 2D array

grades=np.array([
     [87,98],
     [76,90],
     [23,89]
])

print(grades)

print(grades.shape)

#reshaping

reshaped=grades.reshape(2,3)
print(reshaped)

#differemce between 1D and 2D array

vector=np.array([1,2,4,5,6])
print(vector.shape)

new_vector=np.array([[1],[2],[3],[4],[5]])
print(new_vector.shape)

#transpose

new_grades=np.array([
    [1,2],
    [3,4],
    [5,6]
])

print(new_grades.shape)

reshaped=new_grades.reshape(6, )
print(reshaped)

#datascience tip reshape(-1,1)

#creating 3D array

new_A=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(new_A.shape)

print(new_A[1])


#creating passing mask
test_scores=np.array([12,35,67,89,99])

passing_mask=test_scores>=60

print(passing_mask)

#extracting data

passing_scores=test_scores[passing_mask]
print(passing_scores)

#code usimg mean

grade_matrix=np.array([
    [89,90,95],
    [95,85,92],
    [60,70,65]
])

#columnwise addition and mean
subject1_mean=np.sum(grade_matrix,axis=0)
student_mean=np.mean(grade_matrix,axis=1)

print(subject1_mean)

#pandas starting

#pd.series similar to np.array

import pandas as pd

city_temps=pd.Series(
    [28,32,45,65],
    index=["Bangalore","chennai","Madurai","New Delhi"]
)


#accessing using index

print(city_temps['chennai'])

print(city_temps+2)

#REAL WORLD SCENARIO dictionary to datframe

hr_data={
    "name":["John","Smith","Alice"],
    "age":[28,34,29],
    "score":[85,90,95],
    "screen_passing":[True,False,True]
}

pd_hr_data=pd.DataFrame(hr_data)

print(pd_hr_data)

#accessing column

score_column=pd_hr_data["score"]
print(score_column)



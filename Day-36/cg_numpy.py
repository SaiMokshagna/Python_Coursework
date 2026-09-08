import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print("One dimensional array:", arr1, sep='\n', end='\n\n')

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Two dimensional array:", arr2, sep='\n', end='\n\n')

arr3 = np.array([[[1, 2], [3,4]], [[5, 6], [7, 8]]])
print("Three dimensional array:", arr3, sep='\n', end='\n\n')

zeros = np.zeros((3, 4))
print("zeros:", zeros)

ones = np.ones((3, 4))
print("ones:", ones)

identity = np.eye(4)
print(identity)

fullarray = np.full((4, 2), 20)
print(fullarray)

range_arr=np.arange(2,51,2)
print(range_arr)

lin_space=np.linspace(0,54,13)
print(lin_space)

#np.random.seed(40)
rand_arr=np.random.randint(100)
print(rand_arr)

rand_float=np.random.rand()
print(rand_float)

rand_float=np.random.rand(3)
print(rand_float)

rand_int=np.random.randint(1,6,(4,3))
print(rand_int)

rand_int=np.random.randint(1,6,3)
print(rand_int)

l=['html','css','javascript','python','mysql']
rand_choice=np.random.choice(l,3)
print(rand_choice)

arr=np.array([[1,2],[3,4],[5,6],[7,8]])
print(arr.shape)

reshaped=arr.reshape(2,1,4)
print(reshaped)

a=np.array([[1,2,3,4],[1,2,3,4]])
flattened=a.flatten()
print(flattened)

transposed=arr.T
print(transposed)

arr=np.array([10,20,30,40,50,60])
print(arr[0])
print(arr[0:3])
print(arr[:2])
print(arr[3:])
print(arr[::2])

matrix=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(matrix[0:3,1])
print(matrix[1:3,0:2])
print(matrix[0:3,2])

arr=np.array([4,9,16,25,36,49,64])
print(arr+10)
print(arr*3)
print(arr**0.5)

print(np.sum(arr))
print(np.mean(arr))
print(np.median(arr))

a=np.array([1,2,3,4,5])
print(np.mean(a))
print(np.var(a))
print(np.std(a))

print(np.cumsum(a))
print(np.cumprod(a))

arr=np.array([1,2,3,4,4,5,2,6,2,3,8])
print(arr%2==0)
print(arr[arr%2==0])

sorted_arr=np.sort(arr)
print(sorted_arr)

unique_vals=np.unique(arr)
print(unique_vals)

arr=np.array([10,20,30])
view_arr=arr.view()
view_arr[0]=100
print(arr,view_arr)

copy_arr=arr.copy()
copy_arr[0]=200
print(arr,copy_arr)

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
print(A.dot(B))

print(np.linalg.det(A))

print(np.linalg.inv(A))

eigenvalues,eigenvectors=np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)

C=np.array([5,11])
solution=np.linalg.solve(A,C)
print(solution)

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
ver_stack=np.vstack((A,B))
hor_stack=np.hstack((A,B))
print(ver_stack)
print(hor_stack)

split_arr=np.split(np.array([1,2,3,4,5,6]),3)
print(split_arr)
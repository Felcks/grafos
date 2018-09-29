array = [5,2,4,6,1,3]

for j in range(1, len(array)):
	chave = array[j]
	i = j - 1
	while(i >= 0 and array[i] > chave):
		array[i+1] = array[i]
		i = i - 1

	array[i + 1] = chave

print(array)

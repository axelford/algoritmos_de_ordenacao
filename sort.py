def comb(vetor):
    troca = 0
    intervalo = len(vetor)
    while intervalo > 1 or troca == 1:
        intervalo = int(intervalo/1.3)
        intervalo = 11 if 8 < intervalo <= 10 else intervalo
        intervalo = 1 if intervalo < 1 else intervalo
        troca = 0
        j = 0
        for i in range(intervalo, len(vetor)):
            if vetor[i] < vetor[j]:
                vetor[i], vetor[j] = vetor[j], vetor[i]
                troca = 1
            j += 1
    return vetor


def buble(vetor):
    for i in range(1, len(vetor)):
        for j in range(len(vetor) - 1):
            if vetor[i] < vetor[j]:
                vetor[i], vetor[j] = vetor[j], vetor[i]
    return vetor


def selection(vetor):

    for i in range(len(vetor) - 1):
        troca = 0
        temp = i
        for j in range(i + 1,len(vetor)):
            if vetor[temp] > vetor[j]:
                temp = j
                troca = 1

        vetor[i], vetor[temp] = vetor[temp] if troca == 1 else vetor[i], vetor[i] if troca == 1 else vetor[temp]
    return vetor


if __name__ == "__main__":
    x = [3, 1, 9, 3.2, 2, 4, 8, 6, 7, 5, 8]
    print()
    print(f' combsort: {comb(x)}')

    x = [3, 1, 9, 3.2, 2, 4, 8, 6, 7, 5, 8]
    print()
    print(f' bublesort: {buble(x)}')

    x = [3, 1, 9, 3.2, 2, 4, 8, 6, 7, 5, 8]
    print()
    print(f'selectionsort: {selection(x)}')




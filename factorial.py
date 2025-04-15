def factorial(n):
    if n<=1:
        return 1
    else:
        counter = n-1
        return n * factorial(counter)

#ho definito una funzione in modo ricorsivo, ossia richiamo la funzione stessa nella funzione
#è importante avere SEMPRE una condizione terminale, altrimenti la funzione viene richiamata
#all'infinito


if __name__ == '__main__':
    print(factorial(4))
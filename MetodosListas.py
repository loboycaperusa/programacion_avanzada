class Metodos:
    def ingreso_elementos(self,Lis,tam):
        i=0
        while(i<tam):
            print("ingrese el elemento en la lista Lis[",i,"]")
            num=int(input("numero "))
            Lis.append(num)
            i=i+1
    def imprimir_elementos(self,Lis,tam):
        for i in range(tam):
            print(Lis[i])
class A:
    atributo_a = 'valor A'

    def metodo(self):
        print('metodo A')

class B(A):
    atributo_b = 'valor B'

    def metodo(self):
        print('metodo B')
        return super().metodo()
    
class C(B):
    atributo_c = 'valor C'

    def metodo(self):
        print('metodo C')
        return super().metodo()
 
c = C()

c.metodo()
import sys
PI=3.14159265358979323643380288
def funcion(n):
  if (n!=0):
    suma=0.0
    for i in range(1,n+1):
      a=(i-0.5)/n
      b=float(i)/n
      xi=(i-0.5)/n	
      fxi=4.0/(1.0+xi*xi)
      suma=suma+fxi
    resultado=suma/n
    return resultado
    
if __name__=="__main__":

 if(len(sys.argv)==1) or (len(sys.argv)==2):
  print '\nNo se han introducido datos,usaremos los valores por defecto de la funcion:\nResultados:'
  n=10
  m=10
 else:
  n=int(sys.argv[1])
  m=int(sys.argv[2])

 l=[]
 for j in range(1, m+1):
  aproximacion=funcion(j*n)
  l=l+[aproximacion]
 print l

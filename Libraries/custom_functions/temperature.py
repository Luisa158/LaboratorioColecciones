
import statistics as stats

def prom (a):
    pro=0
    cont=len(a)
    for i in a:
        pro=pro+i

    final_pro=pro/cont
    return final_pro

def desviacion_estandar(a):
    b= stats.stdev(a)
    return b





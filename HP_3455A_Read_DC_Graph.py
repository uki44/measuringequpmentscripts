import pyvisa
import matplotlib.pyplot as plt
import time


n = 10
rm = pyvisa.ResourceManager()
instrument = rm.open_resource('GPIB1::11::INSTR')
instrument.timeout = 5000
results = [0 for i in range(n)] 
y = [0 for i in range(n)] 

for x in range(n):
    value = instrument.query("F1 R7 A0 H1 M3 T1?")
    results[x] = float(value)
    y[x] = x
    time.sleep(1)
    print(x)

    
plt.plot(y,results, marker = 'o')
ax = plt.gca()
ax.ticklabel_format(useOffset=False)
plt.xlabel('sample number')
plt.ylabel('voltage')
plt.title("3455A DC voltage measurement")
plt.savefig("3455A_Graph.png")
plt.show()

    


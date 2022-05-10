import numpy as np
import matplotlib.pyplot as plt
#np.random.seed(649)
np.random.seed(648)
fs = 60

x = np.random.rand(150)

plt.figure(1,dpi=250)
ax = plt.gca()
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])
plt.xlabel("$\\nu$",fontsize=fs)
plt.ylabel("$\Omega$",fontsize=fs,rotation=0,labelpad=28)
plt.ylim(-0.5,1.5)
plt.plot(x,lw=2)
plt.tight_layout()
#plt.show()
plt.savefig('prop.png',transparent=True)

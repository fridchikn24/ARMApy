import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as sm
df = pd.DataFrame


nsim = 1
nvec = [25,50,100,250,500]
betahat = [-1,-1,-1,-1,-1]
var_betahat = [-1,-1,-1,-1,-1]
output = np.ones([nsim,len(nvec)])
for ns in range(len(nvec)):
    n = nvec[ns]
    for isim in range(nsim):
        n       
        simbase = df({'xt':np.random.normal(size=n, )})
        simbase['lag'] = simbase.shift(-1)
        simbase['error'] = np.random.normal(size=n, )
        olsreg = sm.ols(formula="xt~ lag",data=simbase) 
        result = olsreg.fit()
        betahat = result.params[1]
        print(olsreg.predict(x))       
        output[isim,ns] = betahat
#print(output.mean(0))
#print(output.var(0))
#for ns in range(len(nvec)):
#    sns.kdeplot(output[:,ns],label=nvec[ns])

#goes towards a limit of at least[0.44572748 0.21610177 0.10147593 0.04079261 0.02027238] everytime
#bias for model w/o endogineity
#probably due to error and lag variables not being correlated in any way
# Code for roughness statistics

def pWeibull(r, sigma, eta):
    ''' Weibull function '''
    from numpy import exp
    mu = 1-r
    ret = 2*eta/sigma**2/mu**3 * \
        (((mu**(-2)-1)/sigma**2)**(eta-1)) * \
        exp(-((mu**(-2)-1)/sigma**2)**eta)
    return ret

def sigma2meanr(sigma):
    ''' Converting sigma to <r> 
        Usage: 
        
        sigmalist = np.linspace(.01,.9)
        meanr = sigma2meanr(sigmalist)
        plt.figure()
        plt.plot(sigmalist,meanr,'o')
        plt.grid(True)        
    '''
    import numpy as np
    p = np.array([ 4.57899291e-01, -2.27236062e+00,  4.72080621e+00, -5.09338608e+00,
        2.57626515e+00,  1.77811151e-01, -8.38705493e-01,  1.49765369e-02,
        4.98822342e-01,  3.87112620e-05, -3.41914362e-07])
    meanr = np.polyval(p,sigma)
    return meanr


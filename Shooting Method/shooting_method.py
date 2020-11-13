import matplotlib.pyplot as plt
import numpy as np
import seaborn

a, b = 0, 1
A, B = -1, -2


def f(x, u):
    return u[1] - x

def F(f):
  return lambda x, u: np.append(u[1:], f(x, u))

def adams4(f, a, b, u0, h):
    func = F(f)
    x = a
    u = np.array(u0)
    res = [(x, u[0])]
    prev = [(x, u)]
    while x + h <= b:
        if len(prev) == 1:
            u = u + h * func(*prev[-1])
        elif len(prev) == 2:
            u = u + h / 2 * (3 * func(*prev[-1]) - func(*prev[-2]))
        elif len(prev) == 3:
            u = u + h / 12 * (23 * func(*prev[-1]) - 16 * func(*prev[-2]) + 5 * func(*prev[-3]))
        else:
            u = u + h / 24 * (55 * func(*prev[-1]) - 59 * func(*prev[-2]) + 37 * func(*prev[-3]) - 9 * func(*prev[-4]))
        x = x + h
        res.append((x, u[0]))
        prev.append((x, u))
    return res


def err(actual, res):
  return actual - res[-1][1]

eta_1 = 0
eta_2 = (B - A) / (b - a)

def solve(f, a, b, A, B, eta_1, eta_2, h=0.01, eps=0.01):
  eta = (eta_1 + eta_2) / 2
  hist = [
      (eta_1, adams4(f, a, b, [A, eta_1], h)),
      (eta_2, adams4(f, a, b, [A, eta_2], h))
  ]
  errors = {
      eta_1: err(B, hist[0][1]),
      eta_2: err(B, hist[1][1])
  }
  hist.append((eta, adams4(f, a, b, [A, eta], h)))
  errors[eta] = err(B, hist[-1][1])
  while (abs(errors[eta]) > eps):
    if (errors[eta] * errors[eta_1] < 0):
      eta_1, eta_2 = min(eta, eta_1), max(eta, eta_1)
    else:
      eta_1, eta_2 = min(eta, eta_2), max(eta, eta_2)
    eta = (eta_1 + eta_2) / 2
    hist.append((eta, adams4(f, a, b, [A, eta], h)))
    errors[eta] = err(B, hist[-1][1])
  return hist[-1], hist

res, hist = solve(f, a, b, A, B, eta_1, eta_2, h=0.1, eps=0.01)
arr = np.array(res[1])
seaborn.set()
plt.rcParams["figure.figsize"] = (20, 15)

fig, ax = plt.subplots()

arr = np.array(res[1])
x = arr[:, 0]
y = arr[:, 1]
line = ax.plot(x, y, label='result', linewidth=3, color='black')

for eta, r in hist[:-1]:
  arr = np.array(r)
  x = arr[:, 0]
  y = arr[:, 1]
  line = ax.plot(x, y, label='eta = {:f}'.format(eta))

ax.legend()
plt.show()

import math
def left_riemann_sum(f, a, b, n):
    delta_x = (b - a) / n
    return delta_x * sum([f(a + i*delta_x) for i in range(n)])

def right_riemann_sum(f, a, b, n):
    delta_x = (b - a) / n
    return delta_x * sum([f(a + i * delta_x) for i in range(1,n+1)])

def midpoint_riemann_sum(f, a, b, n):
    delta_x = (b - a) / n
    return delta_x * sum([f(a + (i + .5) * delta_x) for i in range(n)])

def trapezoidal_riemann_sum(f, a, b, n):
    delta_x = (b - a) / n
    return round(0.5 * delta_x * (f(a) + f(b) + sum([2 * f(a + i * delta_x) for i in range(1,n)])),9)

def definite_integral(f, a, b):
    return trapezoidal_riemann_sum(f, a, b, 500000)

# f, g, h are some example functions to test the code
def f(x):
    return math.exp(x)

def g(x):
    return x*x + 2*x + 1

def h(x):
    return math.sin(x)

# derivative function (at a point)
def d_dx(f, x):
    h = 0.00000001
    return (f(x + h) - f(x)) / h


# Some tests
# print(left_riemann_sum(f, 0, 2, 4))
# print(right_riemann_sum(f,0,2,4))
# print(midpoint_riemann_sum(f,0,2,4))
# print(trapezoidal_riemann_sum(f,0,2)) 

print(definite_integral(f, 0, 6)) # Basically the same as the TI-84 fnInt function 
print(d_dx(h, math.pi))

#градиентный метод постоянным шагом для конкретной функции
import math
imya = 6
otch = 32
fami = 12


def for_eps(num):
    return 0.5 * (float(16) ** (-num))


eps = for_eps(3)


def func(mass):
    x, y, z, w = mass
    return imya * x + imya * x**2 + \
           otch * y**2 + fami * y + \
           fami * z**2 + otch * z + \
           fami * w + otch * w**2 + otch * w + imya * w**2


def der_x(x):
    return 2 * (imya * x) + imya


def der_y(y):
    return 2 * (otch * y) + fami


def der_z(z):
    return 2 * (fami * z) + otch


def der_w(w):
    return 2 * ((imya + otch) * w) + otch + fami


def vych_vec(vec1, vec2):
    vec3 = []
    if len(vec1) == len(vec2):
        for i in range(len(vec1)):
            vec3.append(vec1[i] - vec2[i])
    return vec3


def mul_vec(a, vec):
    vec_n = []
    for i in range(len(vec)):
        vec_n.append(vec[i]*a)
    return vec_n


def del_vec(vec1, vec2):
    vec3 = []
    if len(vec1) == len(vec2):
        for i in range(len(vec1)):
            vec3.append(float(vec1[i]) / vec2[i])
    return vec3


def my_grad(x):
    my_g = []
    lenht = len(x)
    if lenht > 0:
        my_g.append(der_x(x[0]))
    if lenht > 1:
        my_g.append(der_y(x[1]))
    if lenht > 2:
        my_g.append(der_z(x[2]))
    if lenht > 3:
        my_g.append(der_w(x[3]))
    return my_g


def norma_vec(vec):
    itog = 0
    for i in range(len(vec)):
        itog += vec[i] ** 2
    return math.sqrt(itog)


def my_entr_4(vec):
    vec_new = []
    for i in range(len(vec)):
        st = float(vec[i]).hex()
        if st[0] != '-':
            vec_new.append(st[2:7] + st[17:])
        else:
            vec_new.append('-' + st[3:8] + st[18:])
    return vec_new


x_pre = [1, 1, 1, 1]#[int(i) for i in input().split()]
grad_f = my_grad(x_pre)
a = (1 - eps) / 43
l_krit = [float(2*imya), float(2*otch), float(2*fami), float(2*(imya + otch))]
x_now = vych_vec(x_pre, mul_vec(a, grad_f))
ite = 1


#print("№       градиент(Xk)                                               Xk                                            " +
#      "                  Xk+1                                                f(Xk+1)" +
#      f"          труд. градиента")
#print(f"{ite}       {my_entr_4(grad_f)}       {x_pre}                                   {my_entr_4(x_now)} " +
#      f"                 {func(x_now).hex()}        {ite}")
while max(del_vec(grad_f, l_krit)) > eps:
    ite += 1
    x_pre = x_now
    grad_f = my_grad(x_pre)
    x_now = vych_vec(x_pre, mul_vec(a, grad_f))
    #print(f"{ite}       {my_entr_4(grad_f)}       {my_entr_4(x_pre)}        {my_entr_4(x_now)} " +
    #      f"                 {func(x_now).hex()}       {ite}")
print("x min:", my_entr_4(x_now))
print("f min:", func(x_now).hex())
print("кол-во итераций:", ite)









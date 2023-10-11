#покоординатный спуск для конкретной функции
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


def my_newt_raf(b, f_first_df, d2fx):
    x = b
    while abs(f_first_df(x)) > eps:
        x = (float(x * d2fx) - float(f_first_df(x))) / float(d2fx)
    return x


x_now = [0, 1, 1, 1]
ite = 0
razm = len(x_now)
x_pre = [-10000 for _ in range(razm)]
f_now = func(x_now)
f_pre = func(x_pre)
df = [der_x, der_y, der_z, der_w]
d2f = [float(2*imya), float(2*otch), float(2*fami), float(2*(imya + otch))]
grad_f = my_grad(x_now)
shagi = ['x', 'y', 'z', 'w']

while max(del_vec(grad_f, d2f)) > eps:
    ite += 1
    x_pre, f_pre = x_now, f_now
    x_now = []
    #print("№    Шаг           Значение шага")
    for i in range(razm):
        x_now.append(my_newt_raf(x_pre[i], df[i], d2f[i]))
        #print(f"{ite}    Шаг по {shagi[i]}:     {x_now[i] - x_pre[i]}")
    f_now = func(x_now)
    grad_f = my_grad(x_now)
    #print("№                               Xk                                fk           " +
    #      "                    Xk+1                                                  fk+1")
    #print(f"{ite}    {my_entr_4(x_pre)}        {float(f_pre).hex()}        {my_entr_4(x_now)}         {f_now.hex()}")
    #print()
print("x min:", my_entr_4(x_now))
print("f min:", func(x_now).hex())




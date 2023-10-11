#минимизация заданной одномерной функции
import math
import hex

name = 0.9
surname = 0.9
ot = 0.7
poln = 25


def f(x):
    return math.exp(name*x) + math.exp(surname*x) + \
           math.exp(ot*x) - poln * (math.sin(x))


def f_first_df(x):
    return name * math.exp(name*x) + surname * math.exp(surname*x) + \
           ot * math.exp(ot*x) - poln * (math.cos(x))


def f_second_df(x):
    return name * name * math.exp(name*x) + surname * surname * math.exp(surname*x) + \
           ot * ot * math.exp(ot*x) + poln * (math.sin(x))


def my_entr_4(st):
    if st[0] != '-':
        return st[2:7] + st[17:]
    else:
        return '-' + st[3:8] + st[18:]


def my_entr_pr(st):
    if st[0] != '-':
        return st[2:8] + st[17:]
    else:
        return '-' + st[3:9] + st[18:]



def my_dichotomy(a, b, ep):
    n = 0
    #print("Итерации метода дихотомии:")
    #print("n    левая граница         xm         f(x - eps)       f(x + eps)    xp           Правая граница    Трудоемкость")
    xp = (a + b) / 2.0 + ep/4.0
    xm = (a + b) / 2.0 - ep/4.0
    while abs(abs(b) - abs(a)) > ep:

        n += 1
        xp = (a + b) / 2.0 + ep/4.0
        xm = (a + b) / 2.0 - ep/4.0
        #print(n, "  ", my_entr_pr(a.hex()), "    ", my_entr_pr(xm.hex()), "    ", my_entr_pr(f(xm).hex()), "    ",
        #      my_entr_pr(f(xp).hex()), "     ", my_entr_pr(xp.hex()), "    ", my_entr_pr(b.hex()), "    ", 2 * n)
        if f(xp) > f(xm):
            b = xp
        else:
            a = xm

    res_x = (a + b) / 2.0
    res = f(res_x).hex()
    #print("Метод дихотомии, результат:       хmin,       f(xmin),    итерации")
    return my_entr_4((res_x).hex()), my_entr_4(res), n


def my_pass_search(a, b, ep):
    fm = f(a)
    m = a
    x = a
    n = 0
    #print("Итерации метода пассивного поиска")
    #print("n    Зн-е x   Зн-е f    Min x на данный момент   Зн-е f в min     Трудоемкость")
    #print(n, "  ", x.hex(), "    ", my_entr_pr(f(x).hex()), "    ", m.hex(), "    ", my_entr_pr(f(m).hex()), "     ", n+1)
    while x <= b:
        fx = f(x)
        #print(n, " ", my_entr_pr(x.hex()), "    ", my_entr_pr(fx.hex()), "    ", my_entr_pr(m.hex()), "    ",
        #      my_entr_pr(fm.hex()), "     ", n + 1)
        if fx <= fm:
            fm = fx
            m = x
        else:
            break
        x += ep
        n += 1

        #if n % 50 == 0:
        #    y = input()
    return my_entr_4(x.hex()), my_entr_4(fm.hex()), n


#дробим отрезок по золотому сечению
def my_gold_cut(a, b, ep):
    n = 0
    cnst = math.sqrt(5.0) / 2.0 - 0.5
    left = a + (1 - cnst)*(b - a)
    right = a + cnst*(b - a)
    fl = f(left)
    fr = f(right)
    #print("Итерации метода золотого сечения")
    #print("n   a               c               f(c)              f(d)             d              b        Трудоемкость")
    while abs(abs(b) - abs(a)) > ep:
        #print(n, " ", my_entr_pr(a.hex()), "   ", my_entr_pr(left.hex()), "   ", my_entr_pr(fl.hex()), "   ",
        #      my_entr_pr(fr.hex()), "  ",
        #      my_entr_pr(right.hex()), "   ", my_entr_pr(b.hex()),
        #      "   ", n + 2)
        if fl < fr:
            b = right
            right = left
            fr = fl
            left = a + (1 - cnst)*(b - a)
            fl = f(left)
        else:
            a = left
            left = right
            fl = fr
            right = a + cnst * (b - a)
            fr = f(right)

        n += 1
    res_x = (a + b) / 2.0
    res = f(res_x).hex()

    return my_entr_4((res_x).hex()), my_entr_4(res), n



#почти касательные, он ищет экстремум
def my_newt_raf(b, ep):
    x = b
    n = 0
    l = a*a + b * b
    #print("Итерации метода Ньютона-Рафсона")
    #print("n      приближение х         f(x)    Трудоем. df  Трудоем. d^2f")
    #print(n, "     ", my_entr_pr(x.hex()), "    ",  my_entr_pr(f(x).hex()), "     ", 0, "    ", 0)
    while abs(f_first_df(x)) > l*ep:
        d2fx = f_second_df(x)
        x = (float(x * d2fx) - float(f_first_df(x))) / float(d2fx)
        n += 1
        #print(n, "     ",  my_entr_pr(x.hex()), "    ",  my_entr_pr(f(x).hex()), "    ",n +2, "     ", 2 + n)
        if n > 100:
            break
    res = f(x).hex()
    return my_entr_4(x.hex()), my_entr_4(res), n


#он же касательные, на вход только выпуклые и дифф. функции
def my_newton(a, b, ep):
    c = b - a
    n = 0
    fa = f(a)
    fb = f(b)
    dfa = f_first_df(a)
    dfb = f_first_df(b)
    #print("Метод касательных")
    #print("n      a         fa             dfa           dfb          fb          b      c            f(c)      Тр f    Тр df")
    while (abs(abs(a) - abs(b)) > ep):
        n += 1
        c = float(fb - fa - dfb * b + dfa * a) / float(dfa - dfb)
        fc = f_first_df(c)
        #print(n, "     ", my_entr_pr(a.hex()), "    ",my_entr_pr(fa.hex()), "    ", my_entr_pr(dfa.hex()),
        #      "    ", my_entr_pr(dfb.hex()),  "    ", my_entr_pr(fb.hex()),  "    ",my_entr_pr(b.hex()),
        #      "    ", my_entr_pr(c.hex()),  "    ",
        #      my_entr_pr(f(c).hex()), "    ", my_entr_pr(fc.hex()),
        #      "    ", n + 2, "    ", n + 2)
        if fc > 0:
            b = c
            fb = f(b)
            dfb = fc
        elif fc < 0:
            a = c
            fa = f(a)
            dfa = fc
        else:
            break

        if n > 200:
            break
    res = f(c).hex()
    return my_entr_4(c.hex()), my_entr_4(res), n


#метод секущих
def my_chords(a, b, ep):
    n = 0
    x0 = a
    x1 = b
    #print("Итерации метода хорд")
    #print("n       x0                        x1                             f(x1)          Трудоемкость df")
    #print(n, "     ", x0.hex(), "                ", x1.hex(), "         ", f(x1).hex(), "         ", 0)
    while abs(f_first_df(x1)) > ep:
        dfx = f_first_df(x1)
        x2 = x1 - dfx * (float(x1 - x0) / float(dfx - f_first_df(x0)))
        x0 = x1
        x1 = x2
        n += 1
        #print(n, "     ", my_entr_pr(x0.hex()), "    ", my_entr_pr(x1.hex()), "    ", my_entr_pr(f(x1).hex()),
        #      "   ", n * 3)
        if n > 50:
            break
    res = f(x1).hex()
    return my_entr_4(x1.hex()), my_entr_4(res), n


def for_eps(num):
    return 0.5 * (float(16) ** (-num))
eps = for_eps(3)

a = 0.0; b = math.pi

print("Поиск минимума функции")
print("Метод:                               (x min, f min, кол-во итераций)")
print()
print("Метод пассивного поиска, результат: ", my_pass_search(a, b, eps))
print()
print("Метод золотого сечения, результат:  ", my_gold_cut(a, b, eps))
print()
print("Метод дихотомии, результат:         ", my_dichotomy(a, b, eps))
print()
print("Метод касательных, результат:       ", my_newton(a, b, eps))
print()
print("Метод Ньютона-Рафсона, результат:   ", my_newt_raf(0.1, eps))
print()
print("Метод хорд, результат:              ", my_chords(a, b, eps))
print()
#print("Метод пассивного поиска, результат: ", my_pass_search(a, b, eps))
import math

# 42. Cosinusni Taylor qatori orqali hisoblash
def FunSimple42(x, eps):
    n = 0
    yigindi = 0
    while True:
        had = ((-1)**n * x**(2*n)) / math.factorial(2*n)
        if abs(had) < eps:
            break
        yigindi += had
        n += 1
    return yigindi

# 43. Ln(1+x) ni hisoblash (|x| < 1)
def FunSimple43(x, eps):
    n = 1
    yigindi = 0
    while True:
        had = ((-1)**(n-1) * x**n) / n
        if abs(had) < eps:
            break
        yigindi += had
        n += 1
    return yigindi

# 44. Arctg(x) ni hisoblash (|x| < 1)
def FunSimple44(x, eps):
    n = 0
    yigindi = 0
    while True:
        had = ((-1)**n * x**(2*n+1)) / (2*n + 1)
        if abs(had) < eps:
            break
        yigindi += had
        n += 1
    return yigindi

# 45. Power4 (Binomial yoyilma) (|x| < 1)
def FunSimple45(x, a, eps):
    n = 0
    yigindi = 0
    while True:
        # Kombinatsiya koeffitsiyenti: a*(a-1)...(a-n+1) / n!
        koeff = 1
        for i in range(n):
            koeff *= (a - i) / (i + 1)
        had = koeff * (x**n)
        if abs(had) < eps:
            break
        yigindi += had
        n += 1
    return yigindi

# 46. EKUB (Eng katta umumiy bo'luvchi)
def EKUB(A, B):
    while B:
        A, B = B, A % B
    return A

# 47. Kasrni qisqartirish (Frac1)
def Frac1(a, b):
    common = EKUB(a, b)
    return a // common, b // common

# 48. EKUK (Eng kichik umumiy karrali)
def EKUK(A, B):
    if A == 0 or B == 0: return 0
    return abs(A * B) // EKUB(A, B)

# 49. Uchta son uchun EKUK
def EKUK3(A, B, C):
    return EKUK(EKUK(A, B), C)

# 50. Sekundni Soat:Minut:Sekundga ajratish
def TimeToHMS(T):
    H = T // 3600
    M = (T % 3600) // 60
    S = T % 60
    return H, M, S

# 51. Vaqtni T sekundga oshirish
def IncTime(H, M, S, T):
    total_seconds = H * 3600 + M * 60 + S + T
    return TimeToHMS(total_seconds)

# 52. Kabisa yilini tekshirish
def IsLeapYear(Y):
    return (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0)

# 53. Oyning kunlar sonini aniqlash
def MonthDays(M, Y):
    if M in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif M in [4, 6, 9, 11]:
        return 30
    elif M == 2:
        return 29 if IsLeapYear(Y) else 28
    return 0

# 54. Oldingi sanani topish
def PrevDate(D, M, Y):
    if D > 1:
        return D - 1, M, Y
    else:
        new_M = M - 1 if M > 1 else 12
        new_Y = Y if M > 1 else Y - 1
        new_D = MonthDays(new_M, new_Y)
        return new_D, new_M, new_Y

# 55. Keyingi sanani topish
def NextDate(D, M, Y):
    if D < MonthDays(M, Y):
        return D + 1, M, Y
    else:
        new_M = M + 1 if M < 12 else 1
        new_Y = Y if M < 12 else Y + 1
        return 1, new_M, new_Y

# 56. Masofa (Leng)
def Leng(X1, Y1, X2, Y2):
    return math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)

# --- Test qilish ---
print(f"42. Cos(1, 0.001): {FunSimple42(1, 0.001)}")
print(f"46. EKUB(24, 36): {EKUB(24, 36)}")
print(f"50. 400 sekund: {TimeToHMS(400)}")
print(f"52. 2024 kabisami?: {IsLeapYear(2024)}")
print(f"55. 28-02-2024 dan keyingi kun: {NextDate(28, 2, 2024)}")
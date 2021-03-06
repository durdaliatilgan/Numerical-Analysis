def lsolve(a,b,l):#lu fonksiyonunda L matrisi ile  bulunan Y değerleri için kullanılıyor
    c= 0
    Y = [0 for i in range(a)]
    for i in range(0,a):
        for j in range(0,i):
            l[i][a]-=l[i][j]*Y[j]
        Y[i] = l[i][a]
    for i in range(0, a):
        print("Y{}={}".format(i+1, Y[i]))
    return  Y
def supur(matrix, a, b):  #son aşamada bilinmeyenleri bulmak için kullanılıyor
    satr = []
    a1 = 0
    x = [0 for i in range(a)]
    for i in range(a - 1, -1, -1):
        x[i] = round((matrix[i][a] / matrix[i][i]), 3)
        for k in range(i - 1, -1, -1):
            matrix[k][a] -= round((matrix[k][i] * x[i]), 3)

    for i in range(0, a):
        print("X{}={}".format(i+1, x[i]))
    return x
def lu(matrix,a,b):   #L ve U matrisleri elde ediliyor ve bilinmeyenler bulunuyor
    satr=[]
    satr1=[]
    u1=[]
    u=uc(matrix,a,b,1)
    ss=uc(matrix,a,b,3)
    matr=[]
    birm=[]
    l=[]
    for i in range(0,a):
        for j in range(0,b):
            a1=u[i][j]
            satr+=[a1]
            a2=matrix[i][j]
            satr1+=[a2]
        u1.append(satr)
        matr.append(satr1)
        satr1=[]
        satr=[]
    for i in range(0,a):
        for j in range(0,a):
            if(i==j):
                a1=1
            else:
                a1=0
            satr+=[a1]
        birm.append(satr)
        satr=[]
        f=1
        c=0
    for i in range(0,a-1):
        for j in range(f,a):
            birm[j][i]=ss[0][c]
            c+=1
        f+=1
    l=matrix
    for i in range(0,a):
        for j in range(0,b):
            l[i][j]=birm[i][j]
    print("L:",l)
    print("U:",u1)
    lsolve(a,b,l)
    supur(u,a,b)
def gaussjordan(matrix,a,b):
    a1=0
    a2=0
    for i in range(0,a):
        a1 = matrix[i][i]
        for j in range(0,b+1):
            matrix[i][j]=round(matrix[i][j]/a1,3)
    w=1
    for i in range(a-1,0,-1):
        for j in range(0,i):
            a1=round((matrix[i][i]*matrix[j][i]),3)
            a2=round((matrix[i][i+w]*matrix[j][i]),3)
            matrix[j][i]=round((matrix[j][i]-a1),3)
            matrix[j][i+w]=round((matrix[j][i+w]-a2),3)
        w+=1
    print("Gauss J:",matrix)
    supur(matrix,a,b)
def pivot(matrs, a, b):#köşegen elemanlarının 0 olup olmadığını denetliyor
    satr = []
    for f in range(0, a):
        if (matrs[f][f] == 0):
            satr = matrs[f]
            matrs[f] = matrs[f + 1]
            matrs[f + 1] = satr
    return matrs
def creat(a, b):                #kullanıcının katsayılar  matrisini girmesi için kullanılıyor
    satr = []
    matrix = []
    ymatrix = []
    a1 = 0
    for j in range(0, a):
        for i in range(0, b + 1):
            if (i < b):
                print("lütfen {}.satır {}.elemanı giriniz".format(j + 1, i + 1))
                a1 = int(input())
                satr += [a1]
            else:
                print("lütfen b vektörünüzün {}. elemanını giriniz".format(j + 1))
                a1 = int(input())
                satr += [a1]
        matrix.append(satr)
        satr = []
    print("A,b:",matrix)
    return matrix
def uc(matrix,a,b,sec): #Gauss Eliminasyon  üst üçgen matris oluşturmak için kullanılıyor
    satr = []
    a1 = 0
    a2 = 0
    c = 1
    d = 0
    sbt = 0
    mat1 = []
    sss=[]
    ss=[]
    while (c < a):
        for z in range(0, c):
            for k in range(0, b + 1):
                a2 = matrix[z][k]
                satr += [a2]
            mat1.append(satr)
            satr = []
        for j in range(d, a - 1):
            sbt = matrix[j + 1][c - 1] / matrix[c - 1][c - 1]
            sss+=[sbt]                                          #LU L için mij
            for i in range(0, b + 1):
                a1 = matrix[j + 1][i] - sbt * matrix[c - 1][i]
                satr += [round(a1, 4)]
            mat1.append(satr)
            satr = []
        matrix = mat1
        c += 1
        d += 1
        mat1 = []
        matrix = pivot(matrix, a, b)#matrisin köşegen elemanlarında o varmı kontrol ediliyor
    ss.append(sss)
    if(sec==1):                         #
        print("üst üçgen matrisi:",matrix)
        return  matrix                  #
    elif(sec==3):                       #secime uygun değer döndürülüyor
        return ss                       #
    elif(sec==2):                       #
        return matrix
def main():
    print("\t\t:):):):):)HOŞGELDİNİZ:):):):):):)\n")
    while True:
        print("******LÜTFEN YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ*******")
        print("1-->GAUSS ELİMİNASYON\n2-->GAUSS JORDAN\n3-->LU\n4-->ÇIKIŞ\n\n")
        sec = int(input())
        if (sec == 4):
            break
        a = int(input("lütfen lineer denklem takımınızın bilinmeyen sayısını giriniz:"))
       # b = int(input("lütfen katsayılar matrisinizin sütun sayısını giriniz:"))
        if (sec == 1):
            supur(uc(creat(a,a),a,a,sec),a,a)
        elif(sec==2):
            gaussjordan(uc(creat(a,a),a,a,sec),a,a)
        elif(sec==3):
            lu(creat(a,a),a,a)
main()
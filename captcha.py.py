from random import*
def saisir():
    B=False
    while not B:
        n=int(input("donner n: "))
        B= (1<n<11)
    return n



def remplir():
    ft=open("captcha.txt","w")
    
    for i in range(n):
        ch=""
        for j in range(26):
            ch=ch+str(randint(0,1))
            
        ft.write(ch+"\n")
    
    ft.close()


def afficher():
    ft=open("captcha.txt","r")
    ch=ft.readline()
    while ch!="":
        cap=generer(ch)
        ch=ft.readline()
        
    ft.close()
    
    
def generer(ch):
    
    cap=""
    nbv=0
    voy="AEIOUY"
    for i in range(len(ch)):
        if ch[i] =="1" :
            c=chr(ord("A")+i)
            cap=cap +c
            if voy.find(c)!=-1 :
                nbv=nbv+1
    if nbv!=0 :
        cap=cap +chr(nbv+70)    
    print(" captcha de : ",ch, "  est: ",cap )        
    return cap


#pp
n=saisir()
remplir()
afficher()
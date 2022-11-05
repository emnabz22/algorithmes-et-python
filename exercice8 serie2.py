
try:
    ft=open("test.txt","r")
    ch=ft.readline()
    v= int(ch)+1
    ft.close()
    ft=open("test.txt","w")
    ft.write(str(v))
    print("nbre de visite au fichier:  ", v)
    ft.close()

   
except:
    print("premiere creation du fichier ")
    ft=open("test.txt","w")
    v=1
    ft.write(str(v))
    ft.close()
  
#The Seth Cipher V.2.3.1     

def Decode():
  xyz = input("Enter the password!")
  if xyz == "pathswurd":
#    num = input("Enter the numbers you'd like to decode")
#    num = num.split()
#    num = list(map(int, num))
    num = []
    count = 0
    perc_count = 1
    for x in num:
      if num[count] != '\n':
        num[count] = abs(num[count]-10)+96
        if num[count] == 160:
          num[count] = " "
        elif num[count] == 148:
          num[count] = ","
        elif num[count] == 146:
          num[count] = "."
        elif num[count] == 129:
          num[count] = "?"
        else:
          print(num[count])
          num[count] = chr(num[count])
      else:
        num[count] = '\n'       
      perc = (perc_count/len(num))*100
      print(num[count], "         ", round(perc,2), "%")
      count+=1
      perc_count+=1
    maybe = ''.join(num)
    print("Code decoded: ", maybe)
    h = open("decoded.txt", "w")
    h.write(maybe)
def Encode():
  xyz = input("Enter the password!")
  if xyz == "pathswurd":
    txt = input("Type in the text you want you want to encode.")
    txtl = list(txt)
    idk = list(txt)
    count = 0
    perc_count = 1
    for z in txtl:
      txtl[count] = ord(txtl[count])-96
      for y in range(-22, 75):
        if txtl[count]+y == 10:
          perc = (perc_count/len(idk))*100
          idk[count] = y
          print(idk[count], "       ",round(perc, 2), "%")
          perc_count+=1
      count+=1
  print("Text encoded!: ", idk)
  f = open("encoded.txt","w")
  f.write(str(idk))
decode = "decode"
encode = "encode"
print("Welcome to the Seth Cipher v.2.3.1 Cipher design by: Seth. Encryption and decryption program written by: Brandon.")
boot = input("What would you like to do?(decode/encode)")
if boot == "decode":
  Decode()
elif boot == "encode":
  Encode()




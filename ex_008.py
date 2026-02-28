medida = float(input("Distância em metros: "))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000

# ':.0f' faz com que não apareça nenhum número depois da vírgula
print("A medida de {}m corresponde a {}km, {}hm, {}dam, {:.0f}dm, {:.0f}cm, {:.0f}mm, ".format(medida, km, hm, dam, dm, cm, mm))

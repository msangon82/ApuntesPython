
accidente_resp = int (input("Numero de accidentes responsables: "))
anos = int(input("Antigüedad en años: "))
km =int(input("Km de este año: "))


if anos < 4:
    prima_anos = 0
else:
    prima_anos = 200+((anos-4)*20)


prima_km = km * 0.01
if prima_km > 400:
    prima = 400

extra = prima_km + prima_anos

if accidente_resp == 1:
    extra /= 2
elif accidente_resp ==2:
    extra /= 4
elif accidente_resp ==3:
    extra = 0

print (round(extra,2))


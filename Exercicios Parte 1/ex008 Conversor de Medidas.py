m = float(input('Quantos metros? '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('A medida de {}m é:\n{} kilometros\n{} hectometros\n{} decamitros\n{} decimetros\n{} '
      'centímetros\n{} milimetros'.format(m, km, hm, dam, dm, cm, mm))


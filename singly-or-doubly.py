As = int(input('Reinforcement area(sq in)? '))
b = int(input('width of beam(in)? '))
d = float(input('What is reinforcement depth(in)? '))
fc = int(input('What is the value of fc(psi)? '))
fy = int(input('What is the value of fy(psi)? '))
b1 = 0.85 - ((0.05 * (fc - 4000)) / 1000)
eu = 0.003
ey = 0.004
p1 = As / (b * d)
p2 = 0.85 * b1 * (fc / fy) * (eu / (eu + ey))
if p1 >= p2:
    print('Double reinforcement')
else:
    print('Single reinforcement')

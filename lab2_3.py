x=2
y=3
z=1.5

t = y**(x+1)+(x+z**(y+1))-(1-x*y*z)/(abs(1-x**3)+1)

print ('Неокругленное значение =',t)
print ('Округленное до целых значение =',round(t))
print ('Округленное до десятых значение =',round(t,1))
print ('Округленное до сотых значение =',round(t,2))

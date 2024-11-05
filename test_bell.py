import bell

print('\nBell state from |00>')
q=bell.bell_state(0,0)
q.dump()

p=bell.ghz_state(3)
print('\nGHZ state',p)
p.dump()
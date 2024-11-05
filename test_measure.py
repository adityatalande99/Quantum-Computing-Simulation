import bell
import ops

psi=bell.bell_state(0,0)
print('Bell state |B00>')
psi.dump()



result, _ =ops.Measure(psi,1,1,True)
print('\nCollapsed State\n')
_.dump()
print('Probability ', result)

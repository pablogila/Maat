import maat as mt

H_mass = mt.atom['H'].mass
P_mass = mt.atom['H'].isotope[0].mass
D_mass = mt.atom['H'].isotope[1].mass
P_abundance = mt.atom['H'].isotope[0].abundance
D_abundance = mt.atom['H'].isotope[1].abundance
print(f'Hydrogen mass is:  {H_mass} uma\n'
      f'Protium mass is:   {P_mass} uma ({P_abundance} abundance)\n'
      f'Deuterium mass is: {D_mass} uma ({D_abundance} abundance)')

# If I don't know the isotope index, I can find it easily:
element, isotope_index = mt.atoms.get_isotope_index('H2')
D_cross_section = mt.atom['H'].isotope[isotope_index].cross_section

print(f'Used isotope index for D is: {isotope_index}\n'
      f'Total bound scattering cross section for D is: {D_cross_section}')

test_dict = {
    1: 'uno',
    15: 'quince'
}

print(test_dict[15])

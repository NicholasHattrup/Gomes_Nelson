import autode as ade
from argparse import ArgumentParser
ade.Config.n_cores = 8


parser=ArgumentParser()
parser.add_argument('--mol_one',required=True,type=str,help='Name of the first molecule to combine')
parser.add_argument('--charge_one',default=0,type=int,help='Net charge of the first molecule to combine')
parser.add_argument('--spin_one',default=0,type=int,help='Total spin of the first molecule to combine')
parser.add_argument('--mol_two',required=True,type=str,help='Name of the second molecule to combine')
parser.add_argument('--charge_two',default=0,type=int,help='Net charge of the second molecule to combine')
parser.add_argument('--spin_two',default=0,type=int,help='Total spin of the second molecule to combine')
args=parser.parse_args()
molecule_one=ade.Molecule(args.mol_one,c=args.charge_one,mult=2*args.spin_one+1)
molecule_two=ade.Molecule(args.mol_two,c=args.charge_two,mult=2*args.spin_two+1)
dimer=ade.NCIComplex(molecule_one,molecule_two)
dimer.find_lowest_energy_conformer(allow_connectivity_changes=False)



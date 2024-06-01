import numpy as np

def generate_sic_unit_cell(a, b, c, alpha, beta, gamma):
    # Convert angles from degrees to radians
    alpha = np.radians(alpha)
    beta = np.radians(beta)
    gamma = np.radians(gamma)

    v1 = [a, 0, 0]
    v2 = [b * np.cos(gamma), b * np.sin(gamma), 0]
    v3 = [c * np.cos(beta), c * (np.cos(alpha) - np.cos(beta) * np.cos(gamma)) / np.sin(gamma), c * np.sqrt(1 - np.cos(beta)**2 - ((np.cos(alpha) - np.cos(beta) * np.cos(gamma)) / np.sin(gamma))**2)]
    
    basis_atoms = np.array([
        [0, 0, 0],  # Si atom
        [1/3, 2/3, 0]  # C atom
    ])
    
    atom_types = ['Si', 'C']
    
    return np.array([v1, v2, v3]), basis_atoms, atom_types

def generate_sic_supercell(a, b, c, alpha, beta, gamma, nx, ny, z_height):
    lattice_vectors, basis_atoms, atom_types = generate_sic_unit_cell(a, b, c, alpha, beta, gamma)
    
    atom_positions = []
    atom_labels = []
    for i in range(nx):
        for j in range(ny):
            for k, atom in enumerate(basis_atoms):
                position = i * lattice_vectors[0] + j * lattice_vectors[1] + [0, 0, z_height] + atom
                atom_positions.append(position)
                atom_labels.append(atom_types[k])
    
    return np.array(atom_positions), atom_labels

def save_atom_positions(atom_positions, atom_labels, filename):
    with open(filename, 'w') as f:
        for pos, label in zip(atom_positions, atom_labels):
            f.write(f'{label} {pos[0]:.6f} {pos[1]:.6f} {pos[2]:.6f}\n')

a = 3.08  # lattice constant for SiC in angstroms
b = 3.08
c = 10.0
alpha = 90
beta = 90
gamma = 120

nx = int(input("Enter the size of the supercell in the x direction: "))
ny = int(input("Enter the size of the supercell in the y direction: "))
z_height = float(input("Enter the z-height for the SiC sheet: "))

atom_positions, atom_labels = generate_sic_supercell(a, b, c, alpha, beta, gamma, nx, ny, z_height)

# Save file
save_atom_positions(atom_positions, atom_labels, 'sic_supercell.txt')

print(f"SiC supercell with size {nx}x{ny}x1 at z-height {z_height} has been generated and saved to 'sic_supercell.txt'.")

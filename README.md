# SiC_Sheet_Generator_At_Any_Height

This repository contains a Python script that generates a 2D hexagonal SiC sheet based on user-defined unit cell parameters and supercell dimensions. Users can specify the height along the z-axis. The generated atomic positions are saved in a text file, making it suitable for simulations and computational studies.

## How to Use

### Prerequisites

Ensure you have Python3 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Instructions

1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/SiC_Sheet_Generator_At_Any_Height.git
    cd SiC_Sheet_Generator_At_Any_Height
    ```

2. **Run the Script**
    ```bash
    python3 generate_sic.py
    ```

3. **Input Parameters**
    ```bash
    Enter the size of the supercell in the x direction: 5
    Enter the size of the supercell in the y direction: 5
    Enter the z-height for the SiC sheet: 10.0
    SiC supercell with size 5x5x1 at z-height 10.0 has been generated and saved to 'sic_supercell.txt'.
    ```

### Note
The generated SiC supercell file (`sic_supercell.txt`) will contain the atomic positions of silicon and carbon atoms, suitable for simulations and computational studies.

---

Create the `generate_sic.py` script based on the provided Python script to complete the repository.

# Mixed Strategy Nash Equilibrium Calculator

This Python script calculates the **mixed strategy Nash equilibrium** for a two-player game using strategies and payoff matrices provided in an Excel file. The results are then output to a separate Excel file.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Input Excel File Format](#input-excel-file-format)
- [Output Excel File](#output-excel-file)
- [Example](#example)
- [License](#license)

## Features

- **Excel Integration**: Reads player strategies and payoff matrices from an Excel file and outputs results to an Excel file.
- **Flexible Input**: Supports any two-player game with any number of strategies.
- **Nash Equilibrium Calculation**: Utilizes the Nashpy library to compute mixed strategy Nash equilibria.
- **User-Friendly**: Easy to set up and run with minimal configuration.

## Requirements

- Python 3.x
- Libraries:
  - [pandas](https://pandas.pydata.org/)
  - [nashpy](https://nashpy.readthedocs.io/)
  - [openpyxl](https://openpyxl.readthedocs.io/)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Krminfinity/nash_equilibrium.git
   cd nash_equilibrium
   ```

2. **Install Required Libraries**:

   Use `pip` to install the necessary Python libraries:

   ```bash
   pip install pandas nashpy openpyxl
   ```

## Usage

1. **Prepare the Input Excel File**:

   - Create an Excel file named `game_input.xlsx` in the project directory.
   - Follow the format specified in the [Input Excel File Format](#input-excel-file-format) section.

2. **Run the Script**:

   Execute the Python script:

   ```bash
   python nash_equilibrium.py
   ```

3. **View the Results**:

   - The script will generate an output file named `game_output.xlsx`.
   - Open this file to see the calculated mixed strategy Nash equilibria.

## Input Excel File Format

The input Excel file should be named **`game_input.xlsx`** and should have the following structure:

### Sheet Name

- **`GameData`**

### Cells Structure

|       Cell        |                            Content                             |
|-------------------|----------------------------------------------------------------|
| **A1**            | `Player1_Strategies`                                           |
| **B1**            | Player 1 strategies (comma-separated), e.g., `A,B`             |
| **A2**            | `Player2_Strategies`                                           |
| **B2**            | Player 2 strategies (comma-separated), e.g., `C,D`             |
| **A4**            | `Payoff_Matrix_P1`                                             |
| **A5** to **An**  | Player 1 payoff matrix                                         |
| **A(n+2)**        | `Payoff_Matrix_P2`                                             |
| **A(n+3)** to **Am** | Player 2 payoff matrix                                      |

### Example

**Sample `game_input.xlsx`:**

|         A                |     B      |     C      |     D      |
|--------------------------|------------|------------|------------|
| **Player1_Strategies**   | A,B        |            |            |
| **Player2_Strategies**   | C,D        |            |            |
|                          |            |            |            |
| **Payoff_Matrix_P1**     |            |            |            |
|                          | **C**      | **D**      |            |
| **A**                    | 6          | 2          |            |
| **B**                    | 2          | 4          |            |
|                          |            |            |            |
| **Payoff_Matrix_P2**     |            |            |            |
|                          | **C**      | **D**      |            |
| **A**                    | 2          | 0          |            |
| **B**                    | 4          | 6          |            |

**Notes:**

- **Strategies Input**:
  - Enter Player 1 strategies in cell **B1** separated by commas.
  - Enter Player 2 strategies in cell **B2** separated by commas.
- **Payoff Matrices**:
  - Under **Payoff_Matrix_P1** and **Payoff_Matrix_P2**, list the strategies and their corresponding payoffs.
  - Ensure that the strategies and payoffs are correctly aligned.

## Output Excel File

The script outputs the results to an Excel file named **`game_output.xlsx`**.

### Output Format

| Player1_A | Player1_B | Player2_C | Player2_D |
|-----------|-----------|-----------|-----------|
|    0.5    |    0.5    |   0.3333  |   0.6667  |

**Columns Explanation:**

- **Player1_A**: Probability that Player 1 chooses strategy A.
- **Player1_B**: Probability that Player 1 chooses strategy B.
- **Player2_C**: Probability that Player 2 chooses strategy C.
- **Player2_D**: Probability that Player 2 chooses strategy D.

## Example

### Game Description

- **Player 1 Strategies**: A, B
- **Player 2 Strategies**: C, D

**Payoff Matrices**:

- **Player 1 Payoff Matrix**:

  |       | **C** | **D** |
  |-------|-------|-------|
  | **A** |   6   |   2   |
  | **B** |   2   |   4   |

- **Player 2 Payoff Matrix**:

  |       | **C** | **D** |
  |-------|-------|-------|
  | **A** |   2   |   0   |
  | **B** |   4   |   6   |

### Setting Up the Input File

Prepare `game_input.xlsx` as shown in the [Input Excel File Format](#input-excel-file-format) section with the above data.

### Running the Script

Execute:

```bash
python nash_equilibrium.py
```

### Expected Output

The `game_output.xlsx` file will contain:

| Player1_A | Player1_B | Player2_C | Player2_D |
|-----------|-----------|-----------|-----------|
|    0.5    |    0.5    |   0.3333  |   0.6667  |

This indicates that:

- Player 1 should play strategies A and B with equal probability (0.5 each).
- Player 2 should play strategy C with probability approximately 0.3333 and strategy D with probability approximately 0.6667.

## License

This project is licensed under the MIT License. 

---

**Note**: Ensure that the `game_input.xlsx` file is correctly formatted and placed in the same directory as the `nash_equilibrium.py` script before running the script.

For any questions or issues, please open an issue on the repository.

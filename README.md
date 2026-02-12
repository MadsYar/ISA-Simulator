# ISA Simulator - README

## What is this?

This is a simulator for a simple 8-bit processor. It executes assembly programs and shows what happens at each cycle.

## Processor Architecture

The simulated processor has:
- **16 registers** (R0 to R15) - 8-bit unsigned values (0-255)
  - R0 is read-only and always contains 0
- **256 instruction memory locations** - stores the program
- **256 data memory locations** - stores data that can be read/written during execution
- All arithmetic wraps at 255 (overflow results in modulo 256)

## Usage

```
python3 isa-sim.py <max_cycles> <program_file> <data_memory_file>
```

- **max_cycles**: Maximum number of cycles to execute
- **program_file**: Assembly program file
- **data_memory_file**: Initial data memory configuration

### Examples:

```
python3 isa-sim.py 50 ./test_1/program_1.txt ./test_1/data_mem_1.txt
python3 isa-sim.py 800 ./test_2/program_2.txt ./test_2/data_mem_2.txt
python3 isa-sim.py 100 ./test_3/program_3.txt ./test_3/data_mem_3.txt
```

## Program Format

Each line specifies an address and instruction:

```
0: LI R1, 10;
1: LI R2, 5;
2: ADD R3, R1, R2;
3: END;
```

Comments start with `#`:
```
0: LI R1, 10;  # Load 10 into R1
```

## Instruction Set

### Arithmetic & Logic
- `ADD R1, R2, R3` - R1 = R2 + R3
- `SUB R1, R2, R3` - R1 = R2 - R3
- `OR R1, R2, R3` - R1 = R2 | R3 (bitwise OR)
- `AND R1, R2, R3` - R1 = R2 & R3 (bitwise AND)
- `NOT R1, R2` - R1 = ~R2 (bitwise NOT)

### Data Movement
- `LI R1, <imm>` - Load immediate value into R1
- `LD R1, R2` - R1 = Memory[R2]
- `SD R1, R2` - Memory[R2] = R1

### Control Flow
- `JR R1` - PC = R1
- `JEQ R1, R2, R3` - if (R2 == R3) then PC = R1
- `JLT R1, R2, R3` - if (R2 < R3) then PC = R1

### Other
- `NOP` - No operation
- `END` - Terminate execution

## Data Memory File Format

Format: `<address>: <value>;`

```
0: 100;
1: 200;
5: 50;
```

Unspecified addresses default to 0.

## Output

For each cycle:
- Cycle number
- Program counter
- Current instruction
- Relevant register/memory values
- Operation results

At termination (END instruction or max_cycles reached):
- Final register file state
- Used data memory locations

## Example Output

```
Current cycle = 0
Program counter = 0
Instruction = LI R1, 10
R1 = 10
---------------------
Current cycle = 1
Program counter = 1
Instruction = LI R2, 5
R2 = 5
---------------------
Current cycle = 2
Program counter = 2
Instruction = ADD R3, R1, R2
R1 = 10 and R2 = 5
The new value is 15
---------------------
```

## Notes

- Programs should end with `END;` otherwise execution continues until max_cycles
- R0 is read-only and always 0
- All arithmetic operations use modulo 256
- Both input files must be properly formatted (see examples in test directories)

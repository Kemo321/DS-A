from dataclasses import dataclass


@dataclass
class Instruction:
    new_symbol: str
    direction: str
    new_state: str


class File:
    def __init__(self, filename: str) -> None:
        self._filename = filename

    def load_instructions(self):
        instructions = {}
        with open(self._filename, "r") as handle:
            for line in handle:
                instruction = line.strip().split(" ")
                state = instruction[0]
                symbol = instruction[1]
                new_symbol = instruction[2]
                direction = instruction[3]
                new_state = instruction[4]

                if (state, symbol) not in instructions:
                    instructions[(state, symbol)] = {}

                instructions[(state, symbol)] = Instruction(new_symbol, direction, new_state)

        return instructions

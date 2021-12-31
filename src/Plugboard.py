import string


class Plugboard:
    def __init__(self):
        circuit = {}
        circuit_map = {}
        for index in range(26):
            circuit[index] = index
            circuit_map[index] = False
        self.board = circuit
        self.board_map = circuit_map

    def flow(self, index):
        return self.board[index]

    def make_connection(self, targets):
        alphabet = list(string.ascii_uppercase)
        target_list = targets.split("-")
        target_indices = []
        has_errors = False
        for target in target_list:
            if target in alphabet and not self.board_map[alphabet.index(target)]:
                target_indices.append(alphabet.index(target))
            else:
                print(
                    "invalid connection at "
                    + target
                    + ", already occupied or not on plugboard"
                )
                has_errors = True

        if not has_errors:
            self.board_map[target_indices[0]] = True
            self.board[target_indices[0]] = target_indices[1]
            self.board_map[target_indices[1]] = True
            self.board[target_indices[1]] = target_indices[0]

    def show_connections(self):
        print(self.board_map)
        print(self.board)

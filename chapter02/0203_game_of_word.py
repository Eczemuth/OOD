class TorKham:
    def __init__(self, command_set):
        self.command_set = command_set
        self.word_history = []

    def check_available(self, new_word):
        try:
            last_word = self.word_history[-1].lower()
        except IndexError:
            return True

        first_two = sorted(new_word[0] + new_word[1])
        last_two = sorted(last_word[-1] + last_word[-2])
        return first_two == last_two and new_word not in self.word_history

    def play(self):
        for pair in self.command_set:
            try:
                command, word = pair.split()
            except ValueError:
                command = pair

            if command == 'P':
                available = self.next(word)
                if not available:
                    break
            elif command == 'R':
                self.reset()
            elif command == 'X':
                break
            else:
                print(f"'{pair}' is Invalid Input !!!")
                break

    def reset(self):
        self.word_history = []
        print("game restarted")

    def next(self, new_word):
        new_word_lower = new_word.lower()
        if self.check_available(new_word_lower):
            self.word_history.append(new_word)
            print(f"'{new_word}' -> {self.word_history}")
            return True
        else:
            print(f"'{new_word}' -> game over")
            return False


print("*** TorKham HanSaa ***")
command_set = [s for s in input('Enter Input : ').split(",")]
tor_kham = TorKham(command_set)
tor_kham.play()

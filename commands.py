from typing import Dict


class Command:

    commands: Dict[str, ] = {}

    def register(self, func):
        # @wraps(func)
        print(f'registering {func.__name__}')
        self.commands.update

        return func


@Command.register
def command_search(search:str):
    print(search)


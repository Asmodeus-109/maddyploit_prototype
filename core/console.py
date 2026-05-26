import os
from core.banner import show_banner


class Console:

    def __init__(self):
        self.current_module = None
        self.target = None

    def start(self):

        show_banner()

        while True:

            cmd = input("maddyploit > ")

            if cmd == "exit":
                break

            elif cmd == "help":
                self.help()

            elif cmd.startswith("use "):
                module_name = cmd.split(" ")[1]
                self.load_module(module_name)

                # ENTER MODULE MODE
                while self.current_module:

                    sub_cmd = input(f"maddyploit ({module_name}) > ")

                    if sub_cmd == "back":
                        self.current_module = None
                        self.target = None
                        break

                    elif sub_cmd.startswith("set target"):
                        try:
                            self.target = sub_cmd.split()[-1]
                            print("target set:", self.target)
                        except:
                            print("Invalid target command")

                    elif sub_cmd == "run":
                        if self.target:
                            self.current_module.run(self.target)
                        else:
                            print("No target set")

                    else:
                        print("Unknown command")

            else:
                print("Unknown command")

    def help(self):

        print("""
help            Show commands
use <module>    Load module
back            Exit module
set target <ip> Set target for module
run             Execute module
exit            Quit
""")

    def load_module(self, module_name):

        try:
            module_path = module_name.replace("/", ".")

            module = __import__(
                f"modules.{module_path}",
                fromlist=["Module"]
            )

            self.current_module = module.Module()

            print(f"Loaded {module_name}")

        except Exception as e:
            print("Error loading module:", e)
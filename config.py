from json import dumps
def run_config():
    config_file = open("config.json", "w")

    # Initial menu
    print("="*41)
    print("PYTHON NOTE ORGANIZER - Configurations".center(41, " "))
    print("="*41)

    # Configuration
    path = input("Insert the absolute path that the files should be moved: ")
    sufix = input("Insert the sufix that the files may have after the number of the day: ")

    # Parsing and writing JSON
    config_dict = {"path": path, "sufix": sufix}
    config_file.write(dumps(config_dict, indent=4))

    # Finalization
    print("=" * 41)

# If config.py was directly executed
if __name__ == "__main__":
    run_config()
from working_logic import do_logic
from downloading import do_download_logic

if __name__ == "__main__":

    data = do_logic()
    do_download_logic(data)

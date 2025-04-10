from charmanager import *

def main():
    #default character human with 12's
    #char = CharacterNode()

    #sample from Brett's character
    char = CharacterNode("Marissa Lawson", 11, 12, 12, 13, 14, 15, 16)

    print(char.name)
    char.print_attributes()
    char.print_move_rate()
    

if __name__ == "__main__":
        main()
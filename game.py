import dice as d
import craps

def main():
    basic_set = d.set_dice()
    basic_set.add_dice(2)
    p = craps.play_game(basic_set)

    craps.interactive_game(p)

main()
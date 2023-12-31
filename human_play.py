from GameControl import GameControl

def main():
    game = GameControl(
        play_mode="human_play", 
        display_solution=True
    )
    game.loop_run()

if __name__ == "__main__":
    main()
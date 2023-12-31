from GameSettings import COLOR, WINDOW_ATTRIBUTE
from GameObjects import GameObjects
from GameControl import GameControl

def main():
    game = GameControl(MODE="agent_play")
    game.loop_run()

if __name__ == "__main__":
    main()
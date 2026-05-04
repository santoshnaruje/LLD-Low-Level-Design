from src.ducks.decoy_duck import DecoyDuck
from src.ducks.mallard_duck import MallardDuck
from src.ducks.redheadh_duck import ReadHeadDuck
from src.ducks.rubber_duck import RubberDuck

if __name__ == "__main__":
    mallard_duck = MallardDuck()
    rubber_duck = RubberDuck()
    redhead_duck = ReadHeadDuck()
    decoy_duck = DecoyDuck()

    for duck in [mallard_duck, rubber_duck, redhead_duck, decoy_duck]:
        duck.quack()
        duck.fly()
        duck.display()
        duck.swim()
        print()

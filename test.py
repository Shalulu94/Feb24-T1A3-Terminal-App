from classes import Opponent


# Testing Global variables to allocate CPU opponents
def opponent():

    global Sandy
    Sandy = Opponent("Sandy", "Huynh", "Luxury", 80, 40, 500)

    print(Sandy.opp_attack)
    print(Sandy.opp_defence)
    print(Sandy.opp_hp)


opponent()


def battle():
    print(Sandy.opp_attack)
    print(Sandy.opp_defence)
    print(Sandy.opp_hp)
    print(Sandy.opp_full_name)


battle()

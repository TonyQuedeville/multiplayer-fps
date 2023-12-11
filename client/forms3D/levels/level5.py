"""_summary_
    Multiplayer-fps : projet Zone 01
    
    Tony Quedeville
    
    Parametres du 5ème étage
    theme abstrait
"""

# -----------------------------------------------------------------------------------------------

level5 = [ #    1       2       3       4       5       6       7       8       9       10      11      12      13      14
    ["  -  ","  -  ","  -  ","  -  ","  -  ","  -  ","  -  ","  -  ","  -  ","ml-00","rm-00","ml-00","  -  ","  -  ","  -  "], #0
    ["ml-00","bl-00","ml-00","bl-00","ml-00","bl-00","ml-00","bl-00","ml-00","bl-00","ch-05","bl-00","ml-00","bl-00","ml-00"], #1
    ["bl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","bl-00","sl-00","bl-00"], #2
    ["ml-00","sl-00","ml-00","sl-00","ml-00","bl-00","ml-00","bl-00","ml-00","bl-00","ml-00","sl-00","sl-00","sl-00","ml-00"], #3
    ["bl-00","sl-00","bl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","ml-00","bl-00","ml-00","bl-00","sl-00","bl-00"], #4
    ["ml-00","sl-00","ml-00","bl-00","ml-00","bl-00","sl-00","bl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","ml-00"], #5
    ["bl-00","sl-00","bl-00","sl-00","bl-00","ml-00","sl-00","ml-00","bl-00","ml-00","bl-00","ml-00","bl-00","sl-00","bl-00"], #6
    ["ml-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","ml-00","sl-00","ml-00"], #7
    ["bl-00","ml-00","bl-00","ml-00","sl-00","ml-00","bl-00","ml-00","bl-00","sl-00","bl-00","sl-00","sl-00","sl-00","bl-00"], #8
    ["ml-00","bl-00","sl-00","bl-00","sl-00","bl-00","ml-00","bl-00","ml-00","bl-00","ml-00","bl-00","ml-00","sl-00","ml-00"], #9
    ["bl-00","sl-00","sl-00","ml-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","bl-00"], #10
    ["ml-00","sl-00","ml-00","bl-00","sl-00","bl-00","sl-00","bl-00","sl-00","bl-00","sl-00","bl-00","ml-00","bl-00","ml-00"], #11
    ["bl-00","sl-00","bl-00","sl-00","sl-00","ml-00","sl-00","ml-00","sl-00","ml-00","sl-00","ml-00","bl-00","sl-00","bl-00"], #12
    ["ml-00","sl-00","sl-00","sl-00","ml-00","bl-00","sl-00","bl-00","sl-00","sl-00","sl-00","bl-00","sl-00","sl-00","ml-00"], #13
    ["bl-00","sl-00","bl-00","sl-00","bl-00","sl-00","sl-00","sl-00","sl-00","ml-00","bl-00","ml-00","sl-00","ml-00","bl-00"], #14
    ["ml-00","sl-00","ml-00","sl-00","ml-00","bl-00","ml-00","bl-00","sl-00","bl-00","sl-00","sl-00","sl-00","sl-00","ml-00"], #15
    ["bl-00","sl-00","sl-00","sl-00","sl-00","ml-00","bl-00","ml-00","sl-00","sl-00","sl-00","ml-00","bl-00","sl-00","bl-00"], #16
    ["ml-00","bl-00","ml-00","bl-00","sl-00","bl-00","sl-00","bl-00","sl-00","bl-00","sl-00","sl-00","ml-00","bl-00","ml-00"], #17
    ["bl-00","sl-00","sl-00","sl-00","sl-00","ml-00","sl-00","ml-00","sl-00","ml-00","bl-00","sl-00","sl-00","ml-00","bl-00"], #18
    ["ml-00","sl-00","ml-00","bl-00","ml-00","bl-00","sl-00","bl-00","sl-00","bl-00","ml-00","bl-00","sl-00","sl-00","ml-00"], #19
    ["bl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","sl-00","ml-00","bl-00","sl-00","bl-00"], #20
    ["ml-00","bl-00","ml-00","bl-00","ch-00","bl-00","ml-00","bl-00","ml-00","bl-00","ml-00","bl-00","ml-00","bl-00","ml-00"], #21
    ["  -  ","  -  ","  -  ","ml-00","rm-00","ml-00","  -  ","  -  ","  -  ","  -  ","  -  ","  -  ","  -  ","  -  ","  -  "], #22
]
player_position_init_5 = [10, 0, 1]
player_orientation_init_5 = 180
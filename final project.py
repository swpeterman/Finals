import random
def final():
    print('Welcome to the adventure game\n')
    print('You are a weary traveler from Goddard Kansas exploring the lands of agarhta.')
    name()
    classes()
    places()
    
def name():
    try:
        open_file = open('names.txt', 'w')
        
        name = input('What is your name traveler? ')
        
        open_file.write(name)
        
        print('Welcome to your journey through Agartha', name)
        
        open_file.close()

def classes():
    print('Pick from the classes following classes \n Archer \n Mage \n Knight')
    c = input('What class would you like to be: ')
    if c == 'archer' or c == 'Archer':
        print('You are granted a bow')
    elif c == 'mage' or c == 'Mage':
        print('You are granted a staff')
    elif c == 'knight' or c == 'Knight':
        print('You are granted a sword')
    else:
        print('Please choose a valid option')
        
def places():
    print('You are presented with 3 different roads.')
    print('1. Monster road \n2. Blue eyed valley \n3. Blonde haired river')
    road = input('Where would you like to take your journey(1, 2, or 3): ')
    
    if road == 'Monster road' or '1':
        m_r()
    elif road == 'Blue eyed valley' or '2':
        b_e_y()
    elif road == 'Blonde haired river' or '3':
        b_h_r()
    else:
        print('Choose a valid place to go')
        
def m_r():
    print('You have choosen to take the Monster road:')
    print('You have encountered a monster')
    monster = random.randint(1, 3)
    
    print('monster has', monster, 'health')
    
    choice = input('Would you like to attack the monster (y/n)? ')
    
    if choice = 'n':
        print('The monster shoots laser beams out of its eyes and you die')
    elif choice = 'y':
        
def b_e_y():
    pass

def b_h_r():
    pass
    
    
    
              
    
            
    
    

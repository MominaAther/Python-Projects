#########################################################################
# ----------------------------FUNCTIONS------------------------------###
#########################################################################
def inputs_easy(B):
    B[0][0] = validate_sudoko_input_easy("Enter the value for A : ")
    B[1][1] = validate_sudoko_input_easy("Enter the value for B : ")
    B[1][2] = validate_sudoko_input_easy("Enter the value for C : ")
    B[1][4] = validate_sudoko_input_easy("Enter the value for D : ")
    B[2][0] = validate_sudoko_input_easy("Enter the value for E : ")
    B[2][2] = validate_sudoko_input_easy("Enter the value for F : ")
    B[3][3] = validate_sudoko_input_easy("Enter the value for G : ")
    B[4][1] = validate_sudoko_input_easy("Enter the value for H : ")
    B[4][3] = validate_sudoko_input_easy("Enter the value for I : ")
    B[4][4] = validate_sudoko_input_easy("Enter the value for J : ")

# ---------------------------------------------------------------------

def validate_sudoko_input_easy(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Input is wrong.")
            continue
        if user_input > 5 or user_input <= 0:
            print("Input is exceeding.")
            continue
        else:
            break

    if 1 <= user_input <= 5:
        return user_input

# --------------------------------------------------------------------

def want_to_make_change_easy(B):
    while True:
        try:
            print('\n'"Do you want to make any change?")
            user_input = validate_yes_no("YES or NO: ")
        except ValueError:
            print("Input is wrong.")
            continue
        if user_input == 'YES':
            inputs_easy(B)
            for i in B:
                print(*i, sep='    ')
        else:
            break

#----------------------------------------------------------

def easy():
    print('\n''Okay lets play')
    print('\n')
    B = [[ 'A', 4, 1, 2, 5 ],[ 5, 'B', 'C', 4, 'D' ],[ 'E', 5, 'F', 3, 1 ],[ 4, 3, 5, 'G', 2 ],[ 1, 'H', 3, 'I', 'J' ]]
    for i in B:
        print(*i, sep = '    ') 
    inputs_easy(B)
    for i in B:
        print(*i, sep='    ')
    want_to_make_change_easy(B)
    for i in B:
        print(*i, sep='    ')
    rows_check(B)
    column_check(B)
    print('\n'"LETS SHOW YOU THE CORRECT BLOCK")
    print('\n')
    B = [[ 3, 4, 1, 2, 5 ],[ 5, 1, 2, 4, 3 ],[ 2, 5, 4, 3, 1 ],[ 4, 3, 5, 1, 2 ],[ 1, 2, 3, 5, 4 ]]
    for i in B:
        print(*i, sep = '    ')
    
#-------------------------------------------------------    

def inputs_normal(B):
    B[0][0] = validate_sudoko_input_normal("Enter the value for A : ")
    B[0][3] = validate_sudoko_input_normal("Enter the value for B : ")
    B[0][4] = validate_sudoko_input_normal("Enter the value for C : ")
    B[0][6] = validate_sudoko_input_normal("Enter the value for D : ")
    B[1][1] = validate_sudoko_input_normal("Enter the value for E : ")
    B[1][5] = validate_sudoko_input_normal("Enter the value for F : ")
    B[2][2] = validate_sudoko_input_normal("Enter the value for G : ")
    B[2][4] = validate_sudoko_input_normal("Enter the value for H : ")
    B[2][6] = validate_sudoko_input_normal("Enter the value for I : ")
    B[3][0] = validate_sudoko_input_normal("Enter the value for J : ")
    B[3][3] = validate_sudoko_input_normal("Enter the value for K : ")
    B[3][7] = validate_sudoko_input_normal("Enter the value for L : ")
    B[4][0] = validate_sudoko_input_normal("Enter the value for M : ")
    B[4][4] = validate_sudoko_input_normal("Enter the value for N : ")
    B[4][7] = validate_sudoko_input_normal("Enter the value for O : ")
    B[5][1] = validate_sudoko_input_normal("Enter the value for P : ")
    B[5][3] = validate_sudoko_input_normal("Enter the value for Q : ")
    B[5][5] = validate_sudoko_input_normal("Enter the value for R : ")
    B[6][2] = validate_sudoko_input_normal("Enter the value for S : ")
    B[6][6] = validate_sudoko_input_normal("Enter the value for T : ")
    B[7][1] = validate_sudoko_input_normal("Enter the value for U : ")
    B[7][3] = validate_sudoko_input_normal("Enter the value for V : ")
    B[7][4] = validate_sudoko_input_normal("Enter the value for W : ")
    B[7][7] = validate_sudoko_input_normal("Enter the value for X : ")

# -------------------------------------------------------------

def validate_sudoko_input_normal(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Input is wrong.")
            continue
        if user_input > 8 or user_input <= 0:
            print("Input is exceeding.")
            continue
        else:
            break

    if 1 <= user_input <= 8:
        return user_input

# ------------------------------------------------------------

def want_to_make_change_normal(B):
    while True:
        try:
            print('\n'"Do you want to make any change?")
            user_input = validate_yes_no("YES or NO: ")
        except ValueError:
            print("Input is wrong.")
            continue
        if user_input == 'YES':
            inputs_normal(B)
            for i in B:
                print(*i, sep='    ')
        else:
            break

#----------------------------------------------------------------------------

def normal():
    print('\n''Okay lets play')
    print('\n')
    B = [['A',8,6,'B','C',5,'D',7], [3,'E',5,1,6,'F',4,8],[8,3,'G',6,'H',1,'I',4], ['J',4,1,'K',8,6,2,'L'], ['M',2,8,7,'N',4,5,'O'], [5,'P',4,'Q',7,'R',6,2],[1,5,'S',4,2,3,'T',6], [2,'U',3,'V','W',7,1,'X']]
    for i in B:
        print(*i, sep = '    ')
    inputs_normal(B)
    for i in B:
        print(*i, sep='    ')
    want_to_make_change_normal(B)
    for i in B:
        print(*i, sep='    ')
    rows_check(B)
    column_check(B)
    print('\n'"LETS SHOW YOU THE CORRECT BLOCK")
    print('\n')
    B = [[4,8,6,2,1,5,3,7], [3,7,5,1,6,2,4,8],[8,3,2,6,5,1,7,4], [7,4,1,5,8,6,2,3], [6,2,8,7,3,4,5,1], [5,1,4,3,7,8,6,2],[1,5,7,4,2,3,8,6], [2,6,3,8,4,7,1,5]]
    for i in B:
        print(*i, sep = '    ')
        
#------------------------------------------------------------------------------------- 

def inputs_hard(B):
    B[0][0] = validate_sudoko_input_hard("Enter the value for A : ")       
    B[0][4] = validate_sudoko_input_hard("Enter the value for B : ")
    B[0][6] = validate_sudoko_input_hard("Enter the value for C : ")
    B[1][3] = validate_sudoko_input_hard("Enter the value for D : ")
    B[1][4] = validate_sudoko_input_hard("Enter the value for E : ")
    B[1][6] = validate_sudoko_input_hard("Enter the value for F : ")
    B[2][1] = validate_sudoko_input_hard("Enter the value for G : ")
    B[2][3] = validate_sudoko_input_hard("Enter the value for H : ")
    B[2][8] = validate_sudoko_input_hard("Enter the value for I : ")
    B[3][1] = validate_sudoko_input_hard("Enter the value for J : ")
    B[3][2] = validate_sudoko_input_hard("Enter the value for K : ")
    B[4][3] = validate_sudoko_input_hard("Enter the value for L : ")
    B[4][4] = validate_sudoko_input_hard("Enter the value for M : ")
    B[4][6] = validate_sudoko_input_hard("Enter the value for N : ")
    B[4][7] = validate_sudoko_input_hard("Enter the value for O : ")
    B[5][0] = validate_sudoko_input_hard("Enter the value for P : ")
    B[5][2] = validate_sudoko_input_hard("Enter the value for Q : ")
    B[5][4] = validate_sudoko_input_hard("Enter the value for R : ")
    B[5][6] = validate_sudoko_input_hard("Enter the value for S : ")
    B[6][2] = validate_sudoko_input_hard("Enter the value for T : ")
    B[6][3] = validate_sudoko_input_hard("Enter the value for U : ")
    B[6][5] = validate_sudoko_input_hard("Enter the value for V : ")
    B[6][6] = validate_sudoko_input_hard("Enter the value for W : ")
    B[7][2] = validate_sudoko_input_hard("Enter the value for X : ")
    B[7][8] = validate_sudoko_input_hard("Enter the value for Y : ")
    B[8][0] = validate_sudoko_input_hard("Enter the value for Z : ")
    B[8][8] = validate_sudoko_input_hard("Enter the value for * : ")

# -------------------------------------------------------------------------------

def validate_sudoko_input_hard(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Input is wrong.")
            continue
        if user_input > 9 or user_input <= 0:
            print("Input is exceeding.")
            continue
        else:
            break

    if 1 <= user_input <= 9:
        return user_input

#-------------------------------------------------------------------------

def want_to_make_change_hard(B):
    while True:
        try:
            print('\n'"Do you want to make any change?")
            user_input = validate_yes_no("YES or NO: ")
        except ValueError:
            print("Input is wrong.")
            continue
        if user_input == 'YES':
            inputs_hard(B)
            for i in B:
                print(*i, sep='    ')
        else:
            break

#--------------------------------------------------------------------------

def hard():
    print('\n''Okay lets play')
    print('\n')
    B = [['A',7,6,4,'B',1,'C',2,5],[1,4,3,'D','E',9,'F',8,6],[5,'G',8,'H',7,6,1,9,'I'],[6,'J','K',5,1,8,2,3,7],[8,1,2,'L','M',4,'N','O',9],['P',3,'Q',9,'R',2,'S',1,8],[4,6,'T','U',2,'V','W',5,1],[2,5,'X',6,9,7,8,4,'Y'],
            ['Z',8,9,1,4,5,6,7,'*']]        
    for i in B:
        print(*i, sep = '    ') 
    inputs_hard(B)
    for i in B:
        print(*i, sep='    ')
    want_to_make_change_hard(B)
    for i in B:
        print(*i, sep='    ')
    rows_check(B)
    column_check(B)
    print('\n'"LETS SHOW YOU THE CORRECT BLOCK")
    print('\n')
    B = [[9,7,6,4,8,1,3,2,5], [1,4,3,2,5,9,7,8,6],[5,2,8,3,7,6,1,9,4], [6,9,4,5,1,8,2,3,7], [8,1,2,7,3,4,5,6,9], [7,3,5,9,6,2,4,1,8],[4,6,7,8,2,3,9,5,1], [2,5,1,6,9,7,8,4,3], [3,8,9,1,4,5,6,7,2]]
    for i in B:
        print(*i, sep = '    ')
        
# ------------------------------------------------------------------------

def validate_yes_no(message):
    while True:
        try:
            user_input = input(message)
            user_input = user_input.upper()
        except ValueError:
            print("Input is wrong.")
            continue
        if user_input == 'YES' or user_input == 'NO':
            break
        else:
            continue
    return user_input

# ----------------------------------------------------------

def rows_check(B):
    rep_number = []
    num_repeated = False
    for i in B:
        for n in i:
            if i.count(n) > 1:
                num_repeated = True
                rep_number.append(n)
    if num_repeated == True:
        values = ','.join(str(v) for v in rep_number)
        print("A number is repeated in row " + (values))
    else:
        print("BINGO! You did it!, no number is repeated in a row")

# ----------------------------------------------------------

def column_check(B):
    rep_number = []
    num_repeated = False
    b = []
    for i in range(len(B[0])):
        row = []
        for item in B:
            row.append(item[i])
        b.append(row)
    for i in b:
        for n in i:
            if i.count(n) > 1:
                num_repeated = True
                rep_number.append(n)
    if num_repeated == True:
        values = ','.join(str(v) for v in rep_number)
        print("A number is repeated in column " + (values))
    else:
        print("BINGO! You did it!, no number is repeated in a column")

# ----------------------------------------------------------

def play():
    print('\n'"CHOOSE THE LEVEL")
    print("1)EASY")
    print("2)NORMAL")
    print("3)HARD")
    while True:
        try:
            ans_level = input("LEVEL: ")
            ans_level = ans_level.upper()
        except ValueError:
            print("Input is wrong.")
            continue
        if ans_level == 'EASY' or ans_level == 'NORMAL' or ans_level == 'HARD':
            break
        else:
            continue
    return ans_level

###################################################################
# ---------------------------START GAME------------------------###
###################################################################

print('\n'"HELLO!")
print('\n'"WELCOME TO THIS WONDERFUL GAME OF SUBOKU")
while True:
    try:
        print('\n'"DO YOU WANT TO START THE GAME?")
        ans_again = validate_yes_no('\n'"YES or NO: ")
        if ans_again == "YES":
            P = play()
            if P == "EASY":
                easy()
            if P == "NORMAL":
                normal()
            if P == "HARD":
                hard()
    except ValueError:
        print("Input is wrong.")
        continue
    if ans_again == 'NO':
        print("Thanks for coming!")
        break
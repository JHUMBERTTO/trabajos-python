
print('''    
         __________
        /LLLLLLLLLL|_____________________
       /LLLLLLLLLLL/LLLLLLLLLLLLLLLLLLLLLL\\
      /LLLLLLLLLLL/LLLLLLLLLLLLLLLLLLLLLLLL\\
      ^||^^^^^^^^/LLLLLLLLLLLLLLLLLLLLLLLLLL\\
       || |~[|]~|^^||^^^^^^^^^^||^|~[|]~|^||^^
       || | [|] |  ||  |~~~~|  || | [|] | ||
       || |_[|]_|  ||  | [] |  || |_[|]_| ||
       ||__________||  |   o|  ||_________||
     .'||][][][][][||  | [] |  ||[][][][][||.'.
    ."'||[][][][][]||_-`----'-_||][][][][]||"."
  .(')^(.)(').( )'^@/-- -- - --\@( )'( ).(( )^(.)^
 '( )^(`)'.(').( )@/-- -- - -- -\@ (.)'(.),( ).(').
 ".'.'." ." '.". @/- - --- -- - -\@ '.".'.".'.".'."
 ". '' ".".".'.'@/ - -- -- -- -- -\@".'..'".'."'.'.'
'.".".''.".''."@/ -- --- --- -- - -\@.".''.".''.".'".     


                                                    ''')

print("Welcome to Home sweet Home \nYour mission is to find your Home")

ask_L_R = str(input("left or right:\n"))
ask_L_R_Lower = ask_L_R.lower()
if ask_L_R_Lower == "left":
    print("Great the left street is the most safe  ")
    print("ohh there is a traffic light in green ")
    ask_S_W = str(input("Pass or wait:\n"))
    ask_S_W_Lower = ask_S_W.lower()
    if ask_S_W_Lower == "wait":
        print("Good answer now you can pass whit no danger ")
        print("Now in front you are 3 door choose one, (tip) your key is color yellow ")
        ask_W_D = str(input("which door u want to go? Red, Blue, Yellow:\n"))
        ask_W_D_Lower = ask_W_D.lower()
        if ask_W_D_Lower == "yellow":
            print("YOU WINN")
        else:
            print("Game over, you have been reported to the police")
    else:
        print("Game over, you have been run over ")
else:
    print("Game over,you have been kidnapped")
  

a = input("May i know your Name : ")
b = int(input("May i know your age: "))
count=0

if(b>10):
    count+=10
    print(f"Your Score : {count}")
    path=input("Left / Right --> ")
    if(path == "Left"):
        count+=10
        print(f"Your Score : {count}")
        reach_river = input("Wait / Swim --> ")
        if(reach_river == "Wait"):
            count+=10
            print(f"Your Score : {count}")
            boat_appears = input("Yes / No --> ")
            if(boat_appears == "Yes"):
                count+=10
                print(f"Your Score : {count}")
                cave=input("Enter / Back --> ")
                if(cave == "Enter"):
                    count+=10
                    print(f"Your Score : {count}")
                    torch = input("Yes / No --> ")
                    if(torch == "Yes"):
                        count+=10
                        print(f"Your Score : {count}")
                        choice = input("A / B / C --> ")
                        if(choice == "B"):
                            count+=10
                            print(f"Your Score : {count}")
                            guard_appears = input("Hide / Fight / Talk --> ")
                            if(guard_appears == "Hide"):
                                count+=10
                                print(f"Your Score : {count}")
                                puzzle_question = int(input("What's 7 + 5 --> "))
                                if(puzzle_question == 12):
                                    count+=10
                                    print(f"Your Score : {count}")
                                    door_color = input("Red / Blue /  Yellow / Green --> ")
                                    if(door_color == "Yellow"):
                                        count+=10
                                        print(f"Your Score : {count}")
                                        key_choice = input("Iron / Golden / Silver --> ")
                                        if(key_choice == "Golden"):
                                            count+=10
                                            print(f"Your Score : {count}")
                                            chest_choice =int(input("1 / 2 / 3 --> "))
                                            if(chest_choice == 2):
                                                count+=10
                                                print(f"Your Score : {count}")
                                                secret_code = input(" Enter your secret code --> ") #PYTHON123
                                                if(secret_code == "PYTHON123"):
                                                    count+=10
                                                    print("Congrats!!! you did it man...")
                                                    print(f"Your Score : {count}")
                                                else:
                                                    print("Game Over")
                                            else:
                                                print("Game Over")
                                        else:
                                            print("Game Over")
                                    else:
                                        print("Game Over")
                                else:
                                    print("Game Over")
                            else:
                                print("Game Over")
                        else:
                            print("Game Over")
                    else:
                        print("Game Over")
                else:
                    print("Game Over")
            else:
                print("Game Over")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
                                                                                                
                            
                            


    
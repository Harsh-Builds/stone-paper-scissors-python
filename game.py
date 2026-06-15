import random

def the_game(c, u):
    
    #draw
    if c == u:
       return None
   # stone vs paper
    if c == "s" and u == "p":
        return True
    
    if c == "p" and u == "s":
        return False
    
   # paper vs scissor
    if c == "p" and u == "sr":
        return True
    
    if c == "sr" and u == "p":
        return False
    
   # stone vs scissor
    if c == "sr" and u == "s":
        return True
    
    if c == "s" and u == "sr":
        return False
        

random_num = random.randint(1,3)

print("computer's turn : stone(s), paper(p), scissor(sr)")

if random_num == 1:
    computer = "s"
elif random_num == 2:
    computer = "p"
else:
    computer = "sr"


user = input("Your turn : stone(s), paper(p), scissor(sr): ").lower()

result = the_game(computer, user)

# here we are doing this thing by using if elif lader
# for computer
if computer == "s":
    real = "stone"
    print(f"compuer choose : {real}")
elif computer == "p":
    real = "paper"
    print(f"compuer choose : {real}")
else :
    real = "scissor"
    print(f"compuer choose : {real}")

# here we use dictionary to do that same thing but in structured way instead of large if elif
# for user
the_dict = {
    "s" : "stone",
    "p" : "paper",
    "sr" : "scissor"
}

the_real = the_dict.get(user)
print(f"You choose : {the_real}")


if result is None:
    print("Draw")

elif (result):
    print("You won 🏆🎉")

else:
    print("You lose 👎")
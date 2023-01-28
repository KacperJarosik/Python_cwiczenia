hello = "hello"

# Use hello to get the "hellohellohellohellohellohellohellohellohellohello" string ( "hello" repeated 10 times).
# ten_of_hellos = hello operator 10
pass
#
ten_of_hellos = hello
for i in range(0, 9):
    ten_of_hellos = ten_of_hellos + hello
print(ten_of_hellos)

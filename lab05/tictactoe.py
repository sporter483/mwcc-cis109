matrix = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

players = ["O", "X"]

turns = 0

winner = None 

while turns < 9 and winner is None: 
    print ("Tic-Tac-Toe") 
    for row in matrix:
        print(" | ".join(row))
    player = players[turns % 2]
    print(f"{player}'s Turn")
    row = input("Enter row (1-3): ") 
    col = input("Enter column (1-3): ")
    if not row.isdigit() or not col.isdigit():
        print("Please enter numbers from 1 to 3.")
        continue
    row = int(row) - 1 
    col = int(col) - 1
    if row < 0 or row > 2 or col < 0 or col > 2:
        print("Row and column must be between 1 and 3.")
        continue 
    if matrix[row][col] != "-":
        print("Cell is already taken. Choose another one.")
        continue
    matrix[row][col] = player 
    turns += 1
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != "-":
            winner = matrix[i][0]
            break
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != "-":
            winner = matrix[0][i]
            break
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != "-":
        winner = matrix[0][0]
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != "-":
        winner = matrix[0][2]

print("Final Board:") 
for row in matrix:
    print(" | ".join(row))
if winner:
    print(f"{winner} wins!")
else:
    print("It's a tie!")
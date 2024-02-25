import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#slot machine size
ROWS = 3
COLS = 3

symbol_count = {
    #symbol, how many times it appears
    "A": 2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value = {
    #symbol, value
    "A": 5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        #else statement executes if break is not executed(for loop is not interrupted)
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings,winning_lines
                

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    #appends all the values in the right amount into the list(ex: two As, four Bs)
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count): # _ works as a temporary variable
            all_symbols.append(symbol)
    
    columns = []# each position of the list contains another list, each one containing the values of each column on the machine
    #for loop pick random values for each row in the column
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #[:] copys the list, instead of the two having the same reference
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):#iterates throw the number of vertical spaces
        for i, column in enumerate(columns):#loops all the column for each row position
            if i != len(columns) - 1:
                print(column[row],end = " | ")
            else:
                print(column[row],end = "")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
            
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
            
    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")
            
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        #checks if there is money for the bet
        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is: ${balance}")
        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", * winning_lines)# * passes every winning line to print function
    
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play(q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
        if balance == 0:
            print("\nYou don't have more money!")
            break
    print(f"You left with ${balance}")
   
    

main()
import pandas as pd
from colorama import init, Fore, Style

def display_top_n(df, n):
    print(df.head(n).to_string(index=False))

def main():
    # Initialize colorama
    init(autoreset=True)
    
    # Variable to control the number of players displayed
    top_n = 50  # Change this to 25 if you want to display the top 25 players
    
    # Load the CSV file into a DataFrame
    df = pd.read_csv('./lib/fantasypros_adp.csv')
    
    # Display the top N ADP players
    print(f"Top {top_n} ADP players:")
    display_top_n(df, top_n)
    
    while True:
        # Take input from the user for the Rank to remove
        try:
            rank_to_remove = int(input(f"\nEnter the Rank of the player to remove (1-{top_n}): "))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a numerical rank.")
            continue
        
        # Check if the entered rank is valid
        if rank_to_remove not in df['Rank'].values:
            print(Fore.RED + "Rank not found. Please enter a valid rank from the list.")
            continue
        
        # Get the player information before removing
        player_info = df[df['Rank'] == rank_to_remove].iloc[0]
        
        # Remove the player with the specified Rank
        df = df[df['Rank'] != rank_to_remove].reset_index(drop=True)
        
        # Save the updated DataFrame to the CSV file
        df.to_csv('./lib/fantasypros_adp.csv', index=False)
        
        # Confirm the removal of the player and display their information
        print(Fore.GREEN + f"Player with Rank {rank_to_remove} has been removed successfully.")
        print(Fore.GREEN + f"Removed player information:\n{player_info.to_string(index=False)}")
        
        # Display the next N highest ADP players
        print(f"\nNext {top_n} highest ADP players after removal:")
        display_top_n(df, top_n)

if __name__ == "__main__":
    main()

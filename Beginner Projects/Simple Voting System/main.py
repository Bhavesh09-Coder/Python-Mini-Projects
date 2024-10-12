## Project title : Simple Voting System

def voting_system():
    candidates = {}
    voters = set()

    # Function to display the menu
    def display_menu():
        print("\nMenu:")
        print("1. Add candidate")
        print("2. Cast vote")
        print("3. View results")
        print("4. Exit and announce winner")
    
    # Function to add a candidate
    def add_candidate():
        candidate = input("Enter the name of the candidate to add: ")
        if candidate in candidates:
            print(f"Candidate {candidate} already exists.")
        else:
            candidates[candidate] = 0
            print(f"Candidate {candidate} added.")
    
    # Function to cast a vote
    def cast_vote():
        voter_id = input("Enter your voter ID: ")
        if voter_id in voters:
            print("You have already voted.")
            return
        
        if not candidates:
            print("No candidates available for voting.")
            return

        print("\nCandidates:")
        for idx, candidate in enumerate(candidates, start=1):
            print(f"{idx}. {candidate}")
        
        choice = int(input("Enter the number of the candidate you want to vote for: "))
        if 1 <= choice <= len(candidates):
            selected_candidate = list(candidates.keys())[choice - 1]
            candidates[selected_candidate] += 1
            voters.add(voter_id)
            print(f"Vote casted for {selected_candidate}.")
        else:
            print("Invalid candidate number.")
    
    # Function to view the results
    def view_results():
        if not candidates:
            print("No candidates available.")
        else:
            print("\nCurrent Results:")
            for candidate, votes in candidates.items():
                print(f"{candidate}: {votes} votes")
    
    # Function to announce the winner
    def announce_winner():
        if not candidates:
            print("No candidates available.")
            return
        winner = max(candidates, key=candidates.get)
        print(f"\nThe winner is {winner} with {candidates[winner]} votes!")
    
    # Main voting loop
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_candidate()
        elif choice == '2':
            cast_vote()
        elif choice == '3':
            view_results()
        elif choice == '4':
            announce_winner()
            print("Exiting the voting system.")
            break
        else:
            print("Invalid option. Please try again.")

voting_system()

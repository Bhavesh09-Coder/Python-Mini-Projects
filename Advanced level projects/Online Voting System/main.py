# Online Voting System

# Candidate class to store information about candidates
class Candidate:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.votes = 0

    def __str__(self):
        return f"{self.name} (ID: {self.id}, Votes: {self.votes})"

# Voting System class to handle voting operations
class VotingSystem:
    def __init__(self):
        self.candidates = {}
        self.voters = set()

    def add_candidate(self, id, name):
        if id in self.candidates:
            print("Candidate ID already exists.")
        else:
            self.candidates[id] = Candidate(id, name)
            print(f"Candidate {name} added.")

    def vote(self, voter_id, candidate_id):
        if voter_id in self.voters:
            print("Voter has already voted.")
            return
        if candidate_id not in self.candidates:
            print("Invalid candidate ID.")
            return
        self.candidates[candidate_id].votes += 1
        self.voters.add(voter_id)
        print(f"Vote cast for {self.candidates[candidate_id].name}.")

    def show_results(self):
        print("Election Results:")
        for candidate in self.candidates.values():
            print(candidate)

# Main function to run the voting system
def main():
    system = VotingSystem()

    # Adding candidates
    system.add_candidate(1, "Alice")
    system.add_candidate(2, "Bob")
    system.add_candidate(3, "Charlie")

    # Voting
    system.vote("voter1", 1)
    system.vote("voter2", 2)
    system.vote("voter1", 2)  # Should not allow multiple votes from the same voter
    system.vote("voter3", 4)  # Invalid candidate ID

    # Showing results
    system.show_results()

if __name__ == "__main__":
    main()

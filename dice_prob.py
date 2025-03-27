from collections import defaultdict

def dice_probability(dice_count, dice_sides):
    """Compute probability distribution for sum of 'dice_count' dice with 'dice_sides' sides."""
    # Initialize base case: one die
    ways = defaultdict(int)
    for i in range(1, dice_sides + 1):
        ways[i] = 1

    # Use recurrence relation to build up to 'dice_count' dice
    for _ in range(2, dice_count + 1):
        new_ways = defaultdict(int)
        for s in range(_, dice_sides * _ + 1):  # Possible sums for '_'-many dice
            new_ways[s] = sum(ways[s - k] for k in range(1, dice_sides + 1) if s - k in ways)
        ways = new_ways

    # Compute total outcomes and probabilities
    total_outcomes = dice_sides ** dice_count
    probabilities = {s: (ways[s] / total_outcomes) * 100 for s in sorted(ways.keys())}
    
    return probabilities

def main():
    while True:
        try:
            dice_count = int(input("Enter the number of dice: "))
            dice_sides = int(input("Enter the number of sides on each die: "))
            probabilities = dice_probability(dice_count, dice_sides)
            html_results = "\n".join(f"<tr><td>{s}</td><td>{prob:.2f}%</td></tr>" for s, prob in probabilities.items())
            print(html_results)
            break
        except ValueError:
            print("Please enter valid integers for the number of dice and sides.")

if __name__ == "__main__":
    main()

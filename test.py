def find_min_stops(D, m, distances):
    stops = 0  # Initialize the number of stops
    current_reach = m  # Current reach of the car
    i = 0  # Index of the current gas station
    stop_points = []  # To store the gas stations where stops are made

    while current_reach < D:
        # Find the farthest gas station reachable from the current position
        farthest_reach = current_reach
        while i < len(distances) and distances[i] <= current_reach:
            farthest_reach = max(farthest_reach, distances[i] + m)
            i += 1

        # If we can't reach the next gas station, it's impossible to complete the journey
        if farthest_reach == current_reach:
            return -1, []

        # Update the current reach and the number of stops
        current_reach = farthest_reach
        stops += 1
        stop_points.append(distances[i - 1])  # The last gas station used to reach farther

    return stops, stop_points

def main():
    D = int(input("Enter the distance (D): "))
    m = int(input("Enter the capacity of the gas tank (m): "))
    n = int(input("Enter the number of gas stations (n): "))

    distances_input = input("Enter the distances to the gas stations: ")
    distances = list(map(int, distances_input.split()))

    min_stops, stop_points = find_min_stops(D, m, distances)
    if min_stops == -1:
        print("It is impossible to complete the journey.")
    else:
        print(f"Minimum number of gas stops required: {min_stops}")
        for stop in stop_points:
            print(f"stop at gas station {distances.index(stop) + 1} ({stop} miles)")

if __name__ == "__main__":
    main()
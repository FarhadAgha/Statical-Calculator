import statistics
data = list(map(int, input("Enter numbers separated by commas: ").split(",")))
print("\nData:", data)
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
pop_var = statistics.pvariance(data)
sample_var = statistics.variance(data)
pop_std = statistics.pstdev(data)
sample_std = statistics.stdev(data)
count = 0
for i in data:
    if i == mode:
        count += 1

print("\n--- Statistics Results ---")
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Mode repeated:", count, "times")
print("Population Variance:", round(pop_var, 2))
print("Sample Variance:", round(sample_var, 2))
print("Population Standard Deviation:", round(pop_std, 2))
print("Sample Standard Deviation:", round(sample_std, 2))

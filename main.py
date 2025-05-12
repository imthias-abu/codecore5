from parser import parse_input
from strategies import same_order, reverse_order, random_order, order_by_tag_count
from scorer import score_order
from timer import measure_time
from output_writer import write_output

input_path = 'data/input1.txt'
output_base = 'data/output1'

frameglasses = parse_input(input_path)

strategies = {
    "same": same_order,
    "reverse": reverse_order,
    "random": random_order,
    "tag_count": order_by_tag_count,
}

for name, strategy in strategies.items():
    ordered, exec_time = measure_time(strategy, frameglasses)
    score = score_order(ordered)
    write_output(f"{output_base}_{name}.txt", ordered)
    print(f"{name.capitalize()} Order: Score = {score}, Time = {exec_time:.4f}s")

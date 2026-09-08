# Entire content of the run.py file
import json
import os

# Assume training code or other processing steps

# Function to simulate processing and saving results

def main(cfg_path):
    # Simulate some processing
    results = {
        'accuracy': 0.85,
        'loss': 0.15
    }

    # Correct path to save results
    result_dir = 'method_comparison/MetaMathQA/results'
    os.makedirs(result_dir, exist_ok=True)
    result_path = os.path.join(result_dir, 'results_{}.json'.format(os.path.basename(cfg_path)))

    with open(result_path, 'w') as f:
        json.dump(results, f)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])

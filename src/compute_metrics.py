from tabulate import tabulate 
import os 
import json 
import fire 
import numpy as np   
from pathlib import Path 

def single_eval_metrics(res_path: str, max_invocations: int, max_trials: int):
    res_ls = []
    for file in os.listdir(res_path):
        if file.endswith(".json"):
            with open(os.path.join(res_path, file), "r") as f:
                res = json.load(f)
            res_ls.append(res) 
    
    res_dct = {'Accuracy': [], 'Num Invocations': [], 'Num Trials': []}
    skip_count = 0
    for idx, res in enumerate(res_ls):
        if res['is_correct'] == None:
            # res_dct['Accuracy'].append(False)
            # We don't count None results for Num Invocations and Num Trials
            # res_dct['Num Invocations'].append(0)
            # res_dct['Num Trials'].append(0)
            # print(f"Skipping {idx} because it is not correct")
            skip_count += 1
            continue
        assert res['is_correct'] == True or res['is_correct'] == False
        res_dct['Accuracy'].append(res['is_correct'])
        if not res['is_correct']:
            res_dct['Num Invocations'].append(max_invocations)
            res_dct['Num Trials'].append(max_trials)
            continue
        num_invocations, num_trials = 0, 0 
        for iteration in res['results_trace'].values():
            if iteration['action'] == 'IMPLEMENTATION': 
                num_trials += 1 
                continue 
            elif iteration['action'] == 'INVOCATIONS':
                num_invocations += len(iteration['generated_invocations'])
        
        res_dct['Num Invocations'].append(num_invocations)
        res_dct['Num Trials'].append(num_trials)
    
    res_dct = {k : np.mean(v) for k, v in res_dct.items()}
    print(f"Skipped {skip_count} out of {len(res_ls)}")
    return res_dct

def main(output_dir: str = 'output/evaluation_results'):
    # Store configurations with their associated model results
    config_model_results = {}
    
    # Auto-detect all datasets
    for dataset in os.listdir(output_dir):
        dataset_path = Path(output_dir) / dataset
        if not dataset_path.is_dir():
            continue

        # Auto-detect all experiment configurations
        for config in os.listdir(dataset_path):
            config_path = dataset_path / config
            if not config_path.is_dir():
                continue
            
            # Parse max invocations and debug rounds from directory name
            if config.startswith("reasoning_guided_mi=") and "_mdr=" in config:
                parts = config.split("_mdr=")
                max_invocations = int(parts[0].replace("reasoning_guided_mi=", ""))
                max_debug_rounds = int(parts[1])
                
                # Create a unique key for this configuration
                config_key = f"mi{max_invocations}_mdr{max_debug_rounds}"
                if config_key not in config_model_results:
                    config_model_results[config_key] = {
                        'max_invocations': max_invocations,
                        'max_debug_rounds': max_debug_rounds,
                        'model_results': {}
                    }
            else:
                continue  # Skip if directory doesn't match expected format
                
            # Find all model paths (which might be nested)
            for root, dirs, files in os.walk(config_path):
                # Only process directories that contain JSON files (model result directories)
                json_files = [f for f in files if f.endswith('.json')]
                if json_files:
                    rel_path = os.path.relpath(root, config_path)
                    full_path = rel_path.replace(os.path.sep, '/')
                    
                    # Extract the actual model name (like gpt-4o-mini) from the path
                    if '/' in full_path:
                        # Paths like "openai/gpt-4o-mini" -> "gpt-4o-mini"
                        model_name = full_path.split('/')[-1]
                    else:
                        model_name = full_path
                    
                    # Compute metrics for this result directory
                    res_dct = single_eval_metrics(root, max_invocations, max_debug_rounds + 1)
                    
                    # Initialize model entry if not exists
                    if model_name not in config_model_results[config_key]['model_results']:
                        config_model_results[config_key]['model_results'][model_name] = {'annotated': {}, 'anonymous': {}}
                    
                    # Store results for this dataset
                    config_model_results[config_key]['model_results'][model_name][dataset] = {
                        'Num Invocations': res_dct['Num Invocations'],
                        'Num Trials': res_dct['Num Trials'],
                        'Success': res_dct['Accuracy'] * 100  # Convert to percentage
                    }
    
    # Generate a LaTeX table for each configuration
    for config_key, config_data in config_model_results.items():
        max_invocations = config_data['max_invocations']
        max_debug_rounds = config_data['max_debug_rounds']
        model_results = config_data['model_results']
        
        # Skip if no model results for this configuration
        if not model_results:
            continue
            
        print(f"\n--- Configuration: Max Invocations={max_invocations}, Max Debug Rounds={max_debug_rounds} ---\n")
        
        # Compute average success for sorting
        avg_success = {}
        for model, datasets in model_results.items():
            success_values = []
            if 'annotated' in datasets and datasets['annotated'] and 'Success' in datasets['annotated']:
                success_values.append(datasets['annotated']['Success'])
            if 'anonymous' in datasets and datasets['anonymous'] and 'Success' in datasets['anonymous']:
                success_values.append(datasets['anonymous']['Success'])
            
            if success_values:
                avg_success[model] = sum(success_values) / len(success_values)
            else:
                avg_success[model] = 0
        
        # Sort models by success rate (lowest to highest)
        sorted_models = sorted(model_results.keys(), key=lambda x: avg_success[x], reverse=False)
        
        # Generate a formatted table for console output
        print(f"\nResults with Max Invocations={max_invocations}, Max Debug Rounds={max_debug_rounds}")
        
        # Define column widths for better alignment
        model_width = max([len(str(model)) for model in sorted_models] + [20])
        col_width = 12
        
        # Print table header
        header = (
            f"{'Model':<{model_width}} | "
            f"{'--- Annotated Dataset ---':^{col_width*3}} | "
            f"{'--- Anonymized Dataset ---':^{col_width*3}}"
        )
        print(header)
        
        subheader = (
            f"{'':<{model_width}} | "
            f"{'Avg. I/O':<{col_width}}"
            f"{'Avg. Trials':<{col_width}}"
            f"{'Success (%)':<{col_width}} | "
            f"{'Avg. I/O':<{col_width}}"
            f"{'Avg. Trials':<{col_width}}"
            f"{'Success (%)':<{col_width}}"
        )
        print(subheader)
        
        # Print separator
        print("-" * (model_width + 3 + col_width*6 + 3))
        
        # Add each model to the table in sorted order
        for model in sorted_models:
            # Format model name
            line = f"{model:<{model_width}} | "
            
            # Annotated dataset metrics
            if 'annotated' in model_results[model] and model_results[model]['annotated']:
                data = model_results[model]['annotated']
                line += (
                    f"{data.get('Num Invocations', 0):.1f}".ljust(col_width) +
                    f"{data.get('Num Trials', 0):.1f}".ljust(col_width) +
                    f"{data.get('Success', 0):.1f}".ljust(col_width)
                )
            else:
                line += "".ljust(col_width*3)
            
            line += " | "
            
            # Anonymous dataset metrics
            if 'anonymous' in model_results[model] and model_results[model]['anonymous']:
                data = model_results[model]['anonymous']
                line += (
                    f"{data.get('Num Invocations', 0):.1f}".ljust(col_width) +
                    f"{data.get('Num Trials', 0):.1f}".ljust(col_width) +
                    f"{data.get('Success', 0):.1f}".ljust(col_width)
                )
            else:
                line += "".ljust(col_width*3)
            
            print(line)
        
        # Print bottom separator
        print("-" * (model_width + 3 + col_width*6 + 3))
        print()

if __name__ == "__main__":
    fire.Fire(main)

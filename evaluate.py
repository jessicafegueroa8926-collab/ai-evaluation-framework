import json
import pandas as pd

def load_json(filepath):
    """Loads a JSON file and returns the data."""
    with open(filepath, 'r') as file:
        return json.load(file)

def evaluate_response(response, rubric):
    """
    Evaluates a single AI response against the rubric.
    Starts with a perfect score of 100 and deducts points for missing requirements.
    """
    score = 100
    
    # 1. Check max length constraint
    if len(response) > rubric['max_length']:
        score -= 20
        
    # 2. Check for required keywords
    for keyword in rubric['required_keywords']:
        if keyword.lower() not in response.lower():
            score -= 10
            
    # Ensure score doesn't drop below 0
    return max(0, score)

def main():
    print("Initializing AI Evaluation Framework...")
    
    # Load configuration and sample data
    config = load_json('config.json')
    data = load_json('sample_data.json')
    rubric = config['rubric']
    
    results = []
    
    print(f"Evaluating {len(data)} responses against rubric...")
    
    # Process each response
    for item in data:
        final_score = evaluate_response(item['response_text'], rubric)
        results.append({
            "Prompt_ID": item["id"],
            "Response_Length": len(item['response_text']),
            "Final_Score": final_score
        })
        
    # Convert results to a DataFrame for reporting
    df = pd.DataFrame(results)
    
    # Export to CSV
    output_filename = 'evaluation_results.csv'
    df.to_csv(output_filename, index=False)
    
    print(df)
    print(f"Evaluation complete. Report saved to {output_filename}")

if __name__ == "__main__":
    main()

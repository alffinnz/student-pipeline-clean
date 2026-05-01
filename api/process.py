import pandas as pd
from pipeline import process_data


def handler(request):
    """
    Vercel serverless function to process student data.
    Accepts POST request with CSV text and returns processed CSV.
    """
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type',
            },
            'body': ''
        }
    
    if request.method != 'POST':
        return {
            'statusCode': 405,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': '{"error": "Method not allowed. Use POST."}'
        }
    
    try:
        # Get CSV data from request body
        body = request.get_json(silent=True)
        
        if not body or 'csv' not in body:
            return {
                'statusCode': 400,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': '{"error": "Missing csv field in request body"}'
            }
        
        csv_text = body['csv']
        
        # Convert CSV text to pandas DataFrame
        from io import StringIO
        df = pd.read_csv(StringIO(csv_text))
        
        # Process the data
        processed_df = process_data(df)
        
        # Convert back to CSV
        output_csv = processed_df.to_csv(index=False)
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'text/csv'
            },
            'body': output_csv
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': f'{{"error": "{str(e)}"}}'
        }
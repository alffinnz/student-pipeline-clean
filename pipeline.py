import pandas as pd


def process_data(df):
    """
    Process student data with the following operations:
    1. Handle missing values using fillna(0)
    2. Add Total and Average columns
    3. Assign grades (A, B, C, Fail)
    4. Sort by Average descending
    5. Add Rank column
    """
    # Handle missing values
    df = df.fillna(0)
    
    # Identify subject columns (numeric columns except Total, Average, Grade, Rank)
    subject_columns = [col for col in df.columns if col not in ['Name', 'Total', 'Average', 'Grade', 'Rank']]
    
    # Add Total column (sum of all subject marks)
    df['Total'] = df[subject_columns].sum(axis=1)
    
    # Add Average column
    df['Average'] = df[subject_columns].mean(axis=1)
    
    # Assign grades based on Average
    def assign_grade(avg):
        if avg >= 90:
            return 'A'
        elif avg >= 75:
            return 'B'
        elif avg >= 60:
            return 'C'
        else:
            return 'Fail'
    
    df['Grade'] = df['Average'].apply(assign_grade)
    
    # Sort by Average descending
    df = df.sort_values(by='Average', ascending=False)
    
    # Add Rank column
    df['Rank'] = range(1, len(df) + 1)
    
    # Reorder columns to have Rank first
    columns_order = ['Rank', 'Name'] + subject_columns + ['Total', 'Average', 'Grade']
    df = df[columns_order]
    
    return df


def load_sample_data():
    """Load sample student data for testing"""
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry'],
        'Math': [85, 92, 78, 95, 65, 88, 72, 90],
        'Science': [90, 88, 82, 91, 70, 85, 68, 87],
        'English': [88, 95, 75, 89, 72, 90, 80, 85],
        'History': [92, 90, 80, 88, 68, 82, 75, 83]
    }
    return pd.DataFrame(data)


if __name__ == '__main__':
    # Test with sample data
    df = load_sample_data()
    print("Original Data:")
    print(df)
    print("\n" + "="*50 + "\n")
    
    processed_df = process_data(df)
    print("Processed Data:")
    print(processed_df)
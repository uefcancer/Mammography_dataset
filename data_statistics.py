import pandas as pd

# Function to read and preprocess data
def read_and_preprocess_data(csv_file_path):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)
    # Extract image IDs without ".jpg" extension
    df['image_id'] = df['Filename'].str.replace('.jpg', '')
    return df

# Read and preprocess train data
train_data = read_and_preprocess_data('data/test.csv')

# Read annotations data
annotations_data = pd.read_csv('data/breast-level_annotations.csv')

# Filter annotations based on train data image IDs
filtered_annotations = annotations_data[annotations_data['image_id'].isin(train_data['image_id'])]

# Print total counts for laterality
print("Total counts for laterality:")
print(filtered_annotations['laterality'].value_counts())

# Function to print total counts for laterality and view position
def print_total_counts(laterality_df, laterality_name):
    print(f"\nTotal counts for {laterality_name} laterality:")
    for view_position in ['CC', 'MLO']:
        total_count = laterality_df[laterality_df['view_position'] == view_position].shape[0]
        print(f"{view_position}: {total_count}")

# Print total counts for left and right laterality
for laterality in ['L', 'R']:
    laterality_df = filtered_annotations[filtered_annotations['laterality'] == laterality]
    print_total_counts(laterality_df, 'Left' if laterality == 'L' else 'Right')

# Function to print statistics
def print_statistics(laterality, view_position, birads_counts, density_counts):
    print(f"\nStatistics for {laterality} laterality and {view_position} view position:")
    print("Breast BIRADS Counts:")
    for birads, count in birads_counts.items():
        print(f"- {birads}: {count}")
    print("\nBreast Density Counts:")
    for density, count in density_counts.items():
        print(f"- {density}: {count}")

# Print statistics for each laterality and view position
for laterality in ['L', 'R']:
    for view_position in ['CC', 'MLO']:
        laterality_view_df = filtered_annotations[(filtered_annotations['laterality'] == laterality) & (filtered_annotations['view_position'] == view_position)]
        birads_counts = laterality_view_df['breast_birads'].value_counts()
        density_counts = laterality_view_df['breast_density'].value_counts()
        print_statistics('Left' if laterality == 'L' else 'Right', view_position, birads_counts, density_counts)

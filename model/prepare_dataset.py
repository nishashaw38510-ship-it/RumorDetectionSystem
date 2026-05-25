import pandas as pd
import os

# Get current project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dataset paths
fake_path = os.path.join(BASE_DIR, 'dataset', 'Fake.csv')
true_path = os.path.join(BASE_DIR, 'dataset', 'True.csv')

# Load datasets
fake_df = pd.read_csv(fake_path)
true_df = pd.read_csv(true_path)

# Add labels
fake_df['label'] = 'rumor'
true_df['label'] = 'non-rumor'

# Keep only required columns
fake_df = fake_df[['text', 'label']]
true_df = true_df[['text', 'label']]

# Combine datasets
final_df = pd.concat([fake_df, true_df])

# Shuffle dataset
final_df = final_df.sample(frac=1).reset_index(drop=True)

# Save final dataset
output_path = os.path.join(BASE_DIR, 'dataset', 'rumor_dataset.csv')
final_df.to_csv(output_path, index=False)

print('Dataset Prepared Successfully')
print(final_df.head())
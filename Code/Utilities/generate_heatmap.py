# Generates heatmaps from eye tracking data to be used in the CNN model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
import os

# === CONFIGURATION ===
base_dir = r"C:\Users\tonyg\OneDrive\Desktop\University Files\Eye Tracking Research\Beach Gaze Data\Chopped_Fixation_BG\users_original_questions"
output_root = r"C:\Users\tonyg\OneDrive\Desktop\University Files\Eye Tracking Research\Heatmaps\Test"

# Original screen resolution (source)
screen_width = 1920
screen_height = 1080

# Target output resolution
target_width = 512
target_height = int(screen_height * (target_width / screen_width))  # Preserves 16:9 ratio

# Gaussian blur spread (adjust as needed)
sigma = 30

# Users to skip
skip_users = {5, 20}

# Create output directory if it doesn't exist
os.makedirs(output_root, exist_ok=True)

# === HEATMAP GENERATION FUNCTION ===
def generate_heatmap_image(csv_path, output_path, sigma=30):
    try:
        df = pd.read_csv(csv_path)
        df = df.dropna(subset=['FPOGX', 'FPOGY', 'FPOGD'])

        # Scale normalized coordinates to pixel space
        df['x_px'] = (df['FPOGX'] * target_width).astype(int)
        df['y_px'] = (df['FPOGY'] * target_height).astype(int)

        # Initialize heatmap canvas
        heatmap = np.zeros((target_height, target_width))

        # Accumulate fixation durations
        for _, row in df.iterrows():
            x, y = row['x_px'], row['y_px']
            if 0 <= x < target_width and 0 <= y < target_height:
                heatmap[y, x] += row['FPOGD']

        # Apply Gaussian blur
        heatmap_blurred = gaussian_filter(heatmap, sigma=sigma)

        # Normalize
        if heatmap_blurred.max() > 0:
            heatmap_blurred /= heatmap_blurred.max()

        # Plot heatmap
        dpi = 100
        figsize = (target_width / dpi, target_height / dpi)
        plt.figure(figsize=figsize, dpi=dpi)
        plt.imshow(heatmap_blurred, cmap='jet', interpolation='bilinear',
                   extent=[0, target_width, 0, target_height])
        plt.gca().invert_yaxis()
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(output_path, dpi=dpi, bbox_inches='tight', pad_inches=0)
        plt.close()

    except Exception as e:
        print(f"Failed to process {csv_path}: {e}")

# === MAIN LOOP ===
for user_id in range(1, 33):
    if user_id in skip_users:
        continue

    user_folder = f"user_{user_id}_questions"
    user_output_dir = os.path.join(output_root, f"user_{user_id}")
    os.makedirs(user_output_dir, exist_ok=True)

    for question_id in range(1, 51):
        question_folder = f"user_{user_id}_question_{question_id}"
        csv_name = f"{question_folder}_valid_fixations.csv"
        csv_path = os.path.join(base_dir, user_folder, question_folder, csv_name)

        if os.path.exists(csv_path):
            output_filename = f"{question_folder}_heatmap.png"
            output_path = os.path.join(user_output_dir, output_filename)
            generate_heatmap_image(csv_path, output_path, sigma=sigma)
            print(f"Saved: {output_path}")
        else:
            print(f"Missing file: {csv_path}")

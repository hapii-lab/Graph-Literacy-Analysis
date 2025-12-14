# Generates scanpaths from eye tracking data to be used in the CNN Model
import pandas as pd
import matplotlib.pyplot as plt
import os

# === CONFIGURATION ===
base_dir = r"C:\Users\tonyg\OneDrive\Desktop\University Files\Eye Tracking Research\Beach Gaze Data\Chopped_Fixation_BG\users_original_questions_beach_gaze"
output_root = r"C:\Users\tonyg\OneDrive\Desktop\University Files\Eye Tracking Research\Scanpaths\Test"
mapping_csv_path = r"C:\Users\tonyg\OneDrive\Desktop\University Files\Eye Tracking Research\Code\Utilities\YennhiThoaQuestionMapping.csv"

# Original screen resolution (source)
screen_width = 1920
screen_height = 1080

# Target output resolution
target_width = 512
target_height = int(screen_height * (target_width / screen_width))  # Preserves 16:9 ratio

# Adjust scale factor proportionally
original_area = screen_width * screen_height
target_area = target_width * target_height
scale_factor = 500 * (target_area / original_area)

# Users to skip
skip_users = {5, 20}

# Create output directory if it doesn't exist
os.makedirs(output_root, exist_ok=True)

# === LOAD QUESTION MAPPING ===
# Load the mapping CSV to convert presentation order to actual question ID
question_mapping = {}
mapping_df = pd.read_csv(mapping_csv_path)
for _, row in mapping_df.iterrows():
    user_id = int(row['User'])
    question_mapping[user_id] = {}
    for q_idx in range(1, 51):  # Q1 to Q50
        col_name = f'Q{q_idx}'
        actual_qid = row[col_name]
        # Handle missing values (e.g., User 11, Q50)
        if pd.notna(actual_qid):
            question_mapping[user_id][q_idx] = int(actual_qid)

# === SCANPATH DRAWING FUNCTION ===
def generate_scanpath_image(csv_path, output_path):
    try:
        df = pd.read_csv(csv_path)
        df = df.dropna(subset=['FPOGX', 'FPOGY', 'FPOGD'])  # ensure required fields

        # Scale normalized coordinates to target resolution
        df['x_px'] = df['FPOGX'] * target_width
        df['y_px'] = df['FPOGY'] * target_height

        # Prepare the figure with correct physical size
        dpi = 100
        figsize = (target_width / dpi, target_height / dpi)
        plt.figure(figsize=figsize, dpi=dpi)
        plt.imshow([[1]], extent=[0, target_width, 0, target_height], cmap='gray', alpha=0)
        plt.gca().invert_yaxis()
        plt.axis('off')

        # Draw fixations and saccades
        for i in range(len(df) - 1):
            x1, y1 = df.iloc[i]['x_px'], df.iloc[i]['y_px']
            x2, y2 = df.iloc[i + 1]['x_px'], df.iloc[i + 1]['y_px']
            duration = df.iloc[i]['FPOGD']
            plt.scatter(x1, y1, s=duration * scale_factor, color='blue', alpha=0.6)
            plt.plot([x1, x2], [y1, y2], color='red', linewidth=1, alpha=0.5)

        # Add fixation numbers
        for i, row in df.iterrows():
            plt.text(row['x_px'], row['y_px'], str(i + 1), fontsize=3, color='black')

        plt.tight_layout()
        plt.savefig(output_path, dpi=dpi)
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
            # Get the actual question ID from the mapping
            actual_question_id = question_mapping.get(user_id, {}).get(question_id)
            if actual_question_id is not None:
                output_filename = f"{question_folder}_ID_{actual_question_id}_scanpath.png"
            else:
                # Fallback if mapping is missing (e.g., User 11, Q50)
                output_filename = f"{question_folder}_ID_unknown_scanpath.png"
                print(f"Warning: No mapping found for user {user_id}, question {question_id}")
            output_path = os.path.join(user_output_dir, output_filename)
            generate_scanpath_image(csv_path, output_path)
            print(f"Saved: {output_path}")
        else:
            print(f"Missing file: {csv_path}")

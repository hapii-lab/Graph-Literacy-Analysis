# Graph Literacy Analysis - Eye-Tracking Study

This repository contains all files and notebooks used for the Graph Literacy Analysis study in the HAPII lab at Cal Poly Pomona. The project uses eye-tracking data to predict graph literacy levels through various machine learning and deep learning approaches.

---

## Study Overview

The study classifies participants as **literate** or **illiterate** in graph comprehension based on eye-tracking data collected during graph viewing tasks. Multiple model architectures were evaluated across different data representations and validation strategies.

## Repository Structure

```
Code/
├── Logistic Regression/     # Spring 2025 - Traditional ML baseline
├── Random Forest/            # Spring 2025 - Ensemble learning
├── CNN/                      # Spring 2025 - Convolutional architectures
├── BERT/                     # Fall 2025 - Transformer-based models
├── VTNet/                    # Fall 2025 - Visual Transformer Networks
├── LOUO CV/                  # Leave-One-User-Out cross-validation experiments
└── Utilities/                # Data preprocessing and visualization tools
```

---

## Data Representations

The study utilizes multiple eye-tracking data formats:

### 1. **Raw Fixations (2-column)**
- **Features:** FPOGX, FPOGY (Fixation Point of Gaze X/Y)
- **Format:** Raw gaze coordinates (0.0-1.0 normalized)

### 2. **Raw Fixations (6-column)**
- **Features:** FPOGX, FPOGY, LPS, RPS, LPMM, RPMM
  - LPS/RPS: Left/Right Screen Proximity (normalized)
  - LPMM/RPMM: Left/Right Pupil Size
- **Format:** Same as 2-column but with pupil measurements

### 3. **Raw Fixations (7-column)**
- **Additional feature:** Fixation duration
- **Format:** Temporal information added to 6-column data

### 4. **Descriptive Gaze Metrics (DGMs)**
- **1-row DGMs:** Single-row representations
- **3-second tumbling DGMs:** Temporal sliding windows
- **Format:** Image-based heatmap representations (32x32 or 64x64 pixels)

### 5. **Scanpaths**
- **Format:** Sequential gaze transition patterns for VTNet

---

## Models & Experiments

### **Spring 2025 Models**

#### 1. **Logistic Regression** (`Logistic Regression/`)
Classic statistical baseline for binary classification.

**Notebooks:**
- `log_reg_beach_gaze_full.ipynb` - Full dataset analysis
- `log_reg_beach_gaze_chopped.ipynb` - Subset analysis

---

#### 2. **Random Forest** (`Random Forest/`)
Ensemble learning with decision trees.

**Notebooks:**
- `RF_beach_gaze_full.ipynb` - Full dataset
- `RF_beach_gaze_chopped.ipynb` - Subset experiments

---

#### 3. **Convolutional Neural Networks (CNN)** (`CNN/`)
Image-based deep learning architectures for heatmap data.

**Subdirectories:**
- `conati_architecture_grouped/` - Replication of Conati et al.'s architecture
- `tony_architecture_full_study/` - Custom CNN for full study
- `tony_architecture_grouped/` - Custom CNN for grouped analysis

**Key details:**
- Processes DGM heatmap images
- Spatial feature extraction via convolution
- Multiple architecture variants tested
- Suitable for 2D gaze distributions

---

### **Fall 2025 Models**

#### 4. **BERT** (`BERT/`)
Transformer-based language models adapted for eye-tracking sequences.

**Notebooks:**
- `BERT_2col_LOUO_Contaminated.ipynb` - 2-column fixations (FPOGX, FPOGY)
- `BERT_6col_LOUO_Contaminated.ipynb` - 6-column fixations with pupil data
- `BERT_DGMs_LOUO_Contaminated.ipynb` - DGM-based BERT

**Key details:**
- **Architecture:** BERT-base-uncased (110M parameters)
- **Tokenization:** Custom `[ROW]` token for fixation delimiters
- **Format:** Text sequences (e.g., `[CLS] 0.50,0.36,3.2 [ROW] 0.47,0.26,3.1 [ROW] ... [SEP]`)
- **Max sequence length:** 512 tokens (truncation applied)
- **Training:**
  - Optimizer: AdamW with learning rate 2e-5
  - Batch size: 4
  - Epochs: 5
  - Loss: Cross-entropy
- **Evaluation:** Leave-One-User-Out (LOUO) cross-validation
- **Metrics:** Accuracy, Precision, Recall, F1-score

---

#### 5. **VTNet** (`VTNet/`)
Visual Transformer Networks for eye-tracking analysis.

**Subdirectories:**
- `Conati's Model/` - Original VTNet architecture from literature
- `VTNet Replication/` - Custom implementation and experiments

**Key details:**
- Transformer-based architecture for sequential eye-tracking
- Attention mechanisms for gaze pattern modeling
- Tested on multiple data formats (2-col, 6-col, 7-col, DGMs)
- Variants include normalized and contaminated datasets

---

## Cross-Validation Experiments (`LOUO CV/`)

**Leave-One-User-Out (LOUO) Validation:** Ensures user-independent generalization by training on N-1 users and testing on the held-out user.

### Logistic Regression LOUO
- `log_reg_DGM_LOUO.ipynb` - DGM-based features
- `log_reg_DGM_LOUO_normalized.ipynb` - Normalized version

### Random Forest LOUO
- `RF_DGM_LOUO.ipynb` - DGM-based features
- `RF_DGM_LOUO_normalized.ipynb` - Normalized version

### VTNet LOUO (Fall 2025)
- `vtnet_LOUO_XY.ipynb` - 2-column raw fixations
- `vtnet_LOUO_XY_6col.ipynb` - 6-column fixations
- `vtnet_LOUO_XY_6col_normalized.ipynb` - Normalized 6-column
- `vtnet_LOUO_XY_6col_Contaminated.ipynb` - Contaminated dataset
- `vtnet_LOUO_XY_7col_normalized.ipynb` - 7-column with duration
- `vtnet_LOUO_XY_Contaminated.ipynb` - 2-column contaminated
- `vtnet_LOUO_DGM_3s.ipynb` - 3-second tumbling DGMs
- `vtnet_LOUO_DGM_3s_normalized.ipynb` - Normalized DGMs

---

## Utilities (`Utilities/`)

### Data Processing Scripts
- `generate_heatmap.py` - Creates Dynamic Gaze Map (DGM) heatmaps
- `generate_scanpath.py` - Generates scanpath visualizations

### Metadata Files
- `QuestionToGraphMapping.csv` - Maps questions to graph types
- `users_literacy_results.csv` - User literacy classifications (grouped study)
- `users_literacy_results_full_study.csv` - User literacy classifications (full study)
- `YennhiThoaQuestionMapping.csv` - Question mapping reference

---
# Pre-VFall-Vision-Sensor-Simulated-Early-Signs-of-Fall-Dataset
This README provides detailed instructions on how to download and utilize the dataset, which is designed to enhance the robustness of fall detection systems.

## Dataset Description

The **Pre-VFall dataset** is a multimodal dataset that includes images, keygradient vector magnitude features, and keygradient vector direction features. It is specifically designed for researchers aiming to advance fall detection systems. The dataset offers valuable insights into how frailty states in older adults might precede fall incidents, thereby helping to improve fall detection accuracy by accounting for irregularities in movement and behavior.

### Key Content:
- **Video Recordings**: Captured using RGB cameras positioned at 90° and 45° angles, including forward-view and side-view perspectives. They are organized into folders named after each session type:
  - `confusion_delirium`
  - `confusion_nph`
  - `dizzy_fall_forward`
  - `dizzy_fall_side`
  - `weakness_fall_forward`
  - `weakness_fall_side`
- **Images**: Around 22K images selected from recorded videos.
- ** Gradient Magnitude and Gradient Direction Features.
- **Activity Classes**:
  - **Normal**: No signs of abnormality or falls.
  - **Abnormal**: Includes pre-fall activities like weakness, dizziness, delirium-confusion, and NPH-confusion.
  - **Fall**: Includes instances of falling and actual falls.

The dataset is intended for machine learning applications to identify pattern cues that signal the onset of falls, particularly focusing on how certain frailty states might indicate the risk of falls.

## Download Instructions

1. **Visit the Download Link**
   -(https://doi.org/10.6084/m9.figshare.26488216.v3)
2. **RE-Run Feature Extraction**
   -If you choose to use all frames of the recorded videos, use provided "Feature Extraction.py" python script for extracting magnitude and direction features. Additional script is provided for converting json-to-csv, should such function be needed. 


## Citation

If you use the Pre-VFall dataset in your research, please cite it as follows:

```markdown
@misc{olisah2024prevfall,
  author       = {Chollette C. Olisah and Xinran Yang},
  title        = {Pre-VFall: Vision Sensor Simulated Early Signs of Fall Dataset},
  year         = {2024},
  publisher    = {figshare},
  howpublished = {Dataset},
  doi          = {10.6084/m9.figshare.26488216.v3},
  url          = {https://doi.org/10.6084/m9.figshare.26488216.v3}
}
```


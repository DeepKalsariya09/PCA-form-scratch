# Principal Component Analysis Algorithm
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

# Load MNIST dataset and store in variables with proper data type
mnist = fetch_openml('mnist_784')
x, y = mnist.data.astype('float32'), mnist.target.astype('int')

# normalize all pixel values between 0 and 1
x /= 255.0

# Select images for only digits 4, 7, and 8 and only first 900 images
selected_digits = [4, 7, 8]
selected_indices = np.isin(y, selected_digits)
x_selected = x[selected_indices]
y_selected = y[selected_indices]
x_np = x_selected.to_numpy()
y_np = y_selected.to_numpy()

# select first 900 images and each row of 2D array stores one image with 784 pixel data in columns
x_np_selected = x_np[0:900]
y_np_selected = y_np[0:900]

# Calculate covariance matrix
sample_cov = np.cov(x_np_selected.T)

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eigh(sample_cov)

# Sort eigenvalues and corresponding eigenvectors in descending order
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

# Choose the number of principal components (m)
m_values = [2, 10, 25, 75, 100, 200]

# Visualize the reconstructed images for different m_values
for m in m_values:
    principal_components = eigenvectors[:, :m].T
    x_projected = np.dot(principal_components, x_np_selected.T)
    x_reconstructed = np.dot(principal_components.T, x_projected).T

    # Reshape the images to 28x28 for visualization
    original_images = x_np_selected[:10].reshape(-1, 28, 28)
    reconstructed_images = x_reconstructed[:10].reshape(-1, 28, 28)

    # Plot original and reconstructed images
    plt.figure(figsize=(12, 5))
    for i in range(10):
        plt.subplot(2, 10, i + 1)
        plt.imshow(original_images[i], cmap='gray')
        plt.title(f'Original {y_np_selected[i]}')
        plt.axis('off')
        plt.subplot(2, 10, i + 11)
        plt.imshow(reconstructed_images[i], cmap='gray')
        plt.title(f'Rec {y_np_selected[i]}')
        plt.axis('off')
        plt.suptitle(f'Reconstruction with {m} Principal Components')
    plt.show()

# Calculate the variance explained by each principal component
variance_explained = eigenvalues / np.sum(eigenvalues)

# Calculate the cumulative variance explained
cumulative_variance_explained = np.cumsum(variance_explained)

# Plot variance explained by each principal component
plt.figure(figsize=(10, 6))
plt.bar(np.arange(1, 785), variance_explained, color='b', alpha=0.7, label='Variance Explained')
plt.xlabel('Principal Component')
plt.ylabel('Variance Explained')
plt.title('Variance Explained by Each Principal Component')
plt.grid()
plt.legend(loc='upper right')
plt.show()

# Plot cumulative variance explained by including each additional principal component
plt.figure(figsize=(10, 6))
plt.plot(np.arange(1, 785), cumulative_variance_explained, color='r', marker='o', linestyle='-')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Variance Explained')
plt.title('Cumulative Variance Explained by Including Each Additional Principal Component')
plt.grid()
plt.show()
min_dim_98pc = 784 - (len(cumulative_variance_explained[cumulative_variance_explained > 0.98]))
print("dimensions need to use in PCA in order to keep 98 percent of the total variance in data")
print(min_dim_98pc)
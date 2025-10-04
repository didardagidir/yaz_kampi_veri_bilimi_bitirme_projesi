# 📊 Data Analysis & Visualization Projects

This repository contains four data analysis projects, each focusing on different datasets and analytical techniques. These projects cover data visualization, decision trees, clustering, and data filtering & sorting.

---

## 1. Data Visualization Project (`50_Startups.csv`)

**Objective:** Explore relationships between various expenditures and profit, and compare them across states.

**Tasks:**
1. Scatter plot of **R&D expenditure vs Profit**  
2. Scatter plot of **Administration expenditure vs Profit**  
3. Bar chart comparing **average profits across states**  
4. Boxplot comparing distributions of **R&D, Administration, and Marketing expenditures**

**Insights:**  
- Strong positive correlation between **R&D expenditure** and profit.  
- Administration expenditure shows less clear correlation with profit.  
- Some states perform significantly better in terms of profit.  
- Expenditure distributions differ across categories, with Marketing spending showing greater variability.

---

## 2. Decision Tree Project (`dava_sonuclari.csv`)

**Objective:** Predict case outcomes using decision tree modeling.

**Tasks:**
1. Handle missing and outlier data.  
2. Split data into **training (80%)** and **testing (20%)** sets.  
3. Build and train a Decision Tree model.  
4. Evaluate model performance with accuracy, precision, recall, and F1-score.  
5. Visualize the decision tree and interpret important features.

**Insights:**  
- Data cleaning improved model reliability.  
- The decision tree identifies the most significant features influencing case outcomes.  
- Evaluation metrics confirm model effectiveness in prediction tasks.

---

## 3. K-Means Clustering Project (`dava.csv`)

**Objective:** Group similar cases using clustering.

**Tasks:**
1. Select relevant features for clustering.  
2. Determine the optimal number of clusters using the **Elbow method**.  
3. Apply the **K-Means algorithm** to cluster the data.  
4. Visualize and interpret clustering results.

**Insights:**  
- Elbow method indicated **2 clusters** as optimal.  
- Clusters show distinct grouping based on case duration, witnesses, and legal fees.  
- Clustering provides insight into patterns in legal case data.

---

## 4. Data Filtering & Sorting Project (`country.csv`)

**Objective:** Filter and sort country data to answer specific questions.

**Tasks:**
1. List countries in descending order of population.  
2. List countries in ascending order of GDP per capita.  
3. Select countries with population above 10 million.  
4. Select top 5 countries by literacy rate.  
5. Filter countries with GDP per capita > 10,000.  
6. Find top 10 countries by population density.

**Insights:**  
- China, India, and the USA have the largest populations.  
- GDP per capita varies greatly between countries.  
- Literacy rate and GDP per capita do not always correlate directly.  
- Population density highlights different geographic and demographic trends.

---

### 📁 Repository Structure
├── Data_Visualization/
│ ├── 50_Startups.csv
│ ├── visualization.ipynb
├── Decision_Tree/
│ ├── dava_sonuclari.csv
│ ├── decision_tree.ipynb
├── KMeans_Clustering/
│ ├── dava.csv
│ ├── kmeans_clustering.ipynb
├── Filtering_Sorting/
│ ├── country.csv
│ ├── filtering_sorting.ipynb
├── README.md


---

### 📌 Tools & Libraries Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  

---

### 📌 How to Run  
1. Clone the repository.  
2. Install required packages: pip install pandas numpy matplotlib seaborn scikit-learn 
3. Open `.ipynb` notebooks in Jupyter Notebook or Jupyter Lab.  

---

### 📌 Author
Didar Dağıdır  
Data Science & Machine Learning Enthusiast  


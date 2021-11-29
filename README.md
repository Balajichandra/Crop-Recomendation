# Crop Recommendation Using Machine Learning

Crop recommendation is one of the most important aspects of precision agriculture. Crop recommendations are based on a number of factors. Precision agriculture seeks to define these criteria on a site-by-site basis in order to address crop selection issues. While the "site-specific" methodology has improved performance, there is still a need to monitor the systems' outcomes.Precision agriculture systems aren't all created equal. However, in agriculture, it is critical that the recommendations made are correct and precise, as errors can result in significant material and capital loss.


<p align="center">
<img src="https://www.opendei.eu/wp-content/uploads/2020/11/img-Yanewn0ORWCx4Jlm-w800.jpg" />
</p>
This application will assist farmers in increasing agricultural productivity, preventing soil degradation in cultivated land, reducing chemical use in crop production, and maximizing water resource efficiency.

# [Dataset]()
This dataset was build by augmenting datasets of rainfall, climate and fertilizer data available for India.

### [Attributes information:]()

* **N** - Ratio of Nitrogen content in soil
* **P** - Ratio of Phosphorous content in soil
* **K** - Ratio of Potassium content in soil
* **Temperature** -  temperature in degree Celsius
* **Humidity** - relative humidity in %
* **ph** - ph value of the soil
* **Rainfall** - rainfall in mm 

### [Experiment Results:]()
* **Data Analysis**
    * All columns contain outliers except for N.
 * **Performance Evaluation**
    * Splitting the dataset by 80 % for training set and 20 % validation set.
 * **Training and Validation**
   * We have trained the model with classification algorithms like Decision tree,Random forest,Support vector machine,GausianNB,XGBoost,Logistic regression 
   * XGBoost gets a higher accuracy score(99.31) than other classification models.
    
 * **Performance Results**
    * Training Score: 99.5%
    * Validation Score: 99.3%

# Demo
Live Demo: https://ml-crop-classification.herokuapp.com/

![](https://i.imgur.com/TnsSPQy.png)
# Predict
data = np.array([[104,18, 30, 23.603016, 60.3, 6.7, 140.91]])
prediction = RF.predict(data)
print(prediction)
# output
['coffee']
# Predict
data = np.array([[83, 45, 60, 28, 70.3, 7.0, 150.9]])
prediction = RF.predict(data)
print(prediction)
# Output
['jute']
# References
* https://www.kaggle.com/atharvaingle/crop-recommendation-dataset

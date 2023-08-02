# Chest X-Ray Classification using Deep-Learning
The objective of this project is to employ a Convolutional Neural Network (CNN) model to categorize chest X-ray images into three distinct classes: COVID-19, Pneumonia, and Normal.
Additionally, this project offers users a web-based implementation utilizing the Streamlit library, enhancing user accessibility and engagement.

<pre>
Domain             : Computer Vision, Machine Learning
Sub-Domain         : Deep Learning, Image Recognition
Techniques         : Deep Convolutional Neural Network
Application        : Image Recognition, Image Classification, Medical Imaging
</pre>

<pre>
<b>Dataset Details</b>
Dataset Name            : Chest X-Ray Images
Number of Class         : 2
Number/Size of Images   : Total      : 9951 images
                          COVID      : 3616 images
                          Normal     : 4990 images
                          Pneumonia  : 1345 images

<b>Model Parameters</b>
Machine Learning Library : Keras
Base Model               : Deep Convolutional Neural Network
Optimizers               : Adam

<b>For Custom Deep Convolutional Neural Network : </b>
<b>Training Parameters</b>
Batch Size               : 64
Number of Epochs         : 20

<b>Output (Prediction/ Recognition / Classification Metrics)</b>
<b>Testing</b>
Accuracy (F-1) Score     : 95.9%
Loss                     : 0.25
Precision  
  Precision (COVID)      : 96.4%
  Precision (Normal)     : 95.3%
  Precision (Pneumonia)  : 95.0%

Recall  
  Recall (COVID)         : 95.2%
  Recall (Normal)        : 95.5%
  Recall (Pneumonia)     : 92.2%
<!--Specificity             : -->
</pre>

##### Model Summary: 
<kbd>
<img src=https://github.com/SanskarBaluni/X-Ray-Classification-Deep-Learning/blob/main/Demo/images/model_summary.png>
</kbd>

<kbd>
<img src=https://github.com/SanskarBaluni/X-Ray-Classification-Deep-Learning/blob/main/Demo/images/Traing_grp.png>
</kbd>

##### Confusion Matrix: 
<kbd>
<img src=https://github.com/SanskarBaluni/X-Ray-Classification-Deep-Learning/blob/main/Demo/Report/heatmp.png alt="Confusion Matrix" width=800px height=600px>
</kbd>


##### Sample Output: 
<kbd>
<img src=https://github.com/SanskarBaluni/X-Ray-Classification-Deep-Learning/blob/main/Demo/sample/sample.png>
</kbd>

#### Tools / Libraries
<pre>
Languages               : Python
Tools/IDE               : Anaconda
Libraries               : Keras, TensorFlow, Streamlit
</pre>

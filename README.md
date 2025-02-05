# Network Anomaly Detection

## Overview
Network-Anomaly-Detection is a tool for detecting network threats using a Random Forest (RF) model trained on simulated network traffic. This project helps identify potential security threats by analyzing network behavior and classifying anomalies.

## Running the App
### **Setup Environment**
1. **Activate Conda Environment**  
   ```bash
   conda activate networkanomaly
   ```
2. **Install Dependencies**  
   Ensure all required dependencies are installed
 
3. **Run the Application**  
   Start the Streamlit app:
   ```bash
   streamlit run results.py
   ```

## Dataset Used
The model is trained on the **UNSW_NB15_training-set (1).csv**, a well-known dataset for network intrusion detection.

## Features
- Uses a **Random Forest** model for network threat detection.
- Analyzes simulated network traffic to identify anomalies.
- Provides an interactive visualization of results via **Streamlit**.

## Future Improvements
- Enhance model performance using deep learning techniques.
- Integrate real-time monitoring for live network anomaly detection.
- Implement additional feature engineering techniques to improve accuracy.



![Example Image](/home/Moraa/Projects/Network-Anomaly-Detection/Images/results.png)

![Dashboard](Images/results.png)

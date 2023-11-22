import json
import pandas as pd
import random
import time
import streamlit as st
#import smtplib
#from email.message import EmailMessage
import matplotlib.pyplot as plt
import seaborn as sns
import base64
#from plyer import notification


import asyncio
from desktop_notifier import DesktopNotifier




import joblib
# Load the model from the pickle file
rf = joblib.load('rf_model.pkl')



# path to my JSON file
json_file_path = 'validation.json' 

data = []

with open(json_file_path, 'r') as f:
    for line in f:
        data.append(json.loads(line))


# Select the 10 features in the same order as the training data
features = ['state', 'dbytes', 'rate', 'sttl', 'sload', 'dload', 'dinpkt', 'tcprtt', 'ackdat', 'ct_state_ttl']


##DASHBOARD

# Set the page title and icon

st.set_page_config(
    page_title = 'Real-Time Traffic Dashboard',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.title("Live Network Traffic Dashboard")



# Create two columns
#KPI METRICS
col1, col2 = st.columns(2)


metric_placeholder = col1.empty()


with col2:
   st.subheader(":white[Vulnerability Assesment]",divider='rainbow')

# Create three columns inside the second main column
subcol1, subcol2, subcol3 = col2.columns(3)

# Create placeholders for the metrics
high_risk_placeholder = subcol1.empty()
medium_risk_placeholder = subcol2.empty()
low_risk_placeholder = subcol3.empty()


#GRAPHSSSS
# create two columns for charts
fig_col1, fig_col2 = st.columns(2)

# Create a placeholder for the histogram
hist_placeholder = fig_col2.empty()

# Create a placeholder for the area chart in fig_col1
area_chart_placeholder = fig_col1.empty()
# Create a DataFrame to store the counts of normal traffic and attacks
traffic_counts = pd.DataFrame(columns=['Normal', 'Attack'])


# Create a placeholder for the table
table_placeholder = st.empty()



# Create a DataFrame to store all packets
all_packets = pd.DataFrame(columns=features + ['prediction'])



num_iterations = 4  # replace with the number of iterations you want

for _ in range(num_iterations):
    # Select a random packet
    packet = random.choice(data)

    # Select the 10 features from the packet
    selected_data = {feature: packet[feature] for feature in features}

    # Convert to DataFrame as the model expects input in this format
    df = pd.DataFrame([selected_data], columns=features)

    # Use the trained model to make predictions
    predictions = rf.predict(df)
    scores = rf.predict_proba(df)

    # Add the prediction to the DataFrame
    df['prediction'] = predictions[0]
    df['Probability score'] = scores.max(axis=1)[0]
    

    #     # Append the new packet to all_packets
    # all_packets = all_packets.append(df, ignore_index=True)
    # Append the new packet to all_packets
    all_packets = pd.concat([all_packets, df], ignore_index=True)



    # # Update the number of packets in the first column
    # with col1:
    #     st.metric(
    #         label="No of Packets",
    #         value=str(len(all_packets)),
    #     )

        # Update the metric in the placeholder
    metric_placeholder.metric(label="No of Packets ⏳", value=str(len(all_packets)))
    

        # Count the number of occurrences of each prediction
    prediction_counts = all_packets['prediction'].value_counts()





   # Define the prediction types that fall under each risk category
    high_risk_types = ['Backdoors', 'Exploits', 'Worms']
    medium_risk_types = ['DoS', 'Shellcode', 'Generic']
    low_risk_types = ['Fuzzers', 'Analysis', 'Reconnaissance']
    # Sum up the counts for the prediction types that fall under each risk category
    high_risk_count = prediction_counts[prediction_counts.index.isin(high_risk_types)].sum()
    medium_risk_count = prediction_counts[prediction_counts.index.isin(medium_risk_types)].sum()
    low_risk_count = prediction_counts[prediction_counts.index.isin(low_risk_types)].sum()
    # Update the metrics in the placeholders
    high_risk_placeholder.metric(label="High", value=str(high_risk_count))
    medium_risk_placeholder.metric(label="Medium", value=str(medium_risk_count))
    low_risk_placeholder.metric(label="Low", value=str(low_risk_count))




    # Count the number of normal traffic and attacks
    normal_count = prediction_counts[prediction_counts.index == 'Normal'].sum()
    attack_count = prediction_counts[prediction_counts.index != 'Normal'].sum()
    # Create a DataFrame with the counts of normal traffic and attacks
    new_counts = pd.DataFrame({'Normal': [normal_count], 'Attack': [attack_count]})
    # Append the counts to traffic_counts
    traffic_counts = pd.concat([traffic_counts, new_counts], ignore_index=True)
    # Create an area chart displaying the counts of normal traffic and attacks
    area_chart_placeholder.line_chart(traffic_counts)
    ## Create a line chart displaying the counts of normal traffic and attacks using matplot lib ( red and blue since stremlit library doesnt support)
    # plt.figure(figsize=(10,6))
    # plt.plot(traffic_counts.index, traffic_counts['Normal'], color='blue', label='Normal')
    # plt.plot(traffic_counts.index, traffic_counts['Attack'], color='red', label='Attack')
    # plt.title('Real-time Line Chart of Traffic Types')
    # plt.xlabel('Time')
    # plt.ylabel('Count')
    # plt.legend()

    # # Display the line chart in the Streamlit app
    # area_chart_placeholder.pyplot(plt)



    # Create a DataFrame with the counts of each prediction
    prediction_df = pd.DataFrame(prediction_counts).reset_index()
    prediction_df.columns = ['Type of Attack', 'Count']

    # Create a bar chart (which is effectively a histogram) using Streamlit
    hist_placeholder.bar_chart(prediction_df.set_index('Type of Attack'))

    # # Create a histogram displaying the type of attack and its frequency
    # plt.figure(figsize=(10,6))
    # sns.countplot(data=all_packets, x='prediction')
    # plt.title('Real-time Histogram of Attack Types')
    # plt.xlabel('Type of Attack')
    # plt.ylabel('Count')
    # plt.xticks(rotation=90)
    # plt.draw()
    # # Display the histogram in the Streamlit app
    # hist_placeholder.pyplot(plt)
    time.sleep(0.1) 

    
    if predictions[0] == 'Fuzzers, Analysis , Reconnaissance , DoS, Shellcode, Generic, Backdoors,Exploits,Worms':
        st.toast('Alert: An attack was predicted!', duration=30)

    # Display all_packets in the table
    table_placeholder.table(all_packets)
    time.sleep(5)
    
    # If an attack is predicted, show a toast notification in the Streamlit app



 








#END OF FOR LOOP

#code to download all packetsa as csv.
csv = all_packets.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
href = f'<a href="data:file/csv;base64,{b64}" download="all_packets.csv">Download CSV File</a>'
st.markdown(href, unsafe_allow_html=True)


















































    #     # Create a countplot of the predictions
    # sns.countplot(x='prediction', data=all_packets)

    # # Display the plot
    # chart_placeholder.pyplot(plt)

    # # Clear the current plot for the next one
    # plt.clf()


    

    #     # Check if the prediction is 'Attack'
    # if predictions[0] == 'Generic':
    #     st.error('Alert: Attack detected!')
    #     # send_email('Alert', 'Attack detected!')

    # print(selected_data, ':', predictions)



    # Wait for 5 seconds before selecting the next packet
   


    





# import pandas as pd

# # Set the maximum number of rows to display
# pd.set_option('display.max_rows', 100)

# # Set the maximum number of columns to display
# pd.set_option('display.max_columns', 50)

# # Set the width of the display in characters
# pd.set_option('display.width', 1000)

# # Set the precision for floating point numbers
# pd.set_option('display.precision', 2)



# def send_email(subject, body):
#     msg = EmailMessage()
#     msg.set_content(body)
#     msg['Subject'] = subject
#     msg['From'] = "cynthia.abugaa@gmail.com"  # replace with your email
#     msg['To'] = "moraabuga@gmail.com"  # replace with recipient's email

#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login("cynthia.abugaa@gmail.com", "moraabuga82001")  # replace with your email and password
#     server.send_message(msg)
#     server.quit()
















# # STOPS MANUALLY
# while True:
#     # Select a random packet
#     packet = random.choice(data)

#     # Select the 10 features from the packet
#     selected_data = {feature: packet[feature] for feature in features}

#     # Convert to DataFrame as the model expects input in this format
#     df = pd.DataFrame([selected_data] , columns=features)

#     df

#     # Use the trained model to make predictions
#     predictions = rf.predict(df)

#     print(selected_data, ':', predictions)


#     # Wait for 5 seconds before selecting the next packet
#     time.sleep(5)












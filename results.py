import json
import pandas as pd
import random
import time
import streamlit as st
import smtplib
from email.message import EmailMessage
import matplotlib.pyplot as plt
import seaborn as sns




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









# create three columns for VA

# col1, col2, col3 = st.columns(3)
# col1.metric(
#     label="No of Packets",
#     value= len(all_packets),)
# col2.metric("Wind", "9 mph", "-8%")
# col3.metric("Humidity", "86%", "4%")

# Create two columns
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



# Create a placeholder for the table
table_placeholder = st.empty()



# Create a DataFrame to store all packets
all_packets = pd.DataFrame(columns=features + ['prediction'])



num_iterations = 10  # replace with the number of iterations you want

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

    

    # Display all_packets in the table
    table_placeholder.table(all_packets)

    time.sleep(5)

















































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












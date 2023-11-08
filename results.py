import json
import pandas as pd
import random
import time
import streamlit as st


# import pandas as pd

# # Set the maximum number of rows to display
# pd.set_option('display.max_rows', 100)

# # Set the maximum number of columns to display
# pd.set_option('display.max_columns', 50)

# # Set the width of the display in characters
# pd.set_option('display.width', 1000)

# # Set the precision for floating point numbers
# pd.set_option('display.precision', 2)




import joblib

# Load the model from the pickle file
rf = joblib.load('rf_model.pkl')



# Specify the path to your JSON file
json_file_path = 'validation.json'  # replace with the path to your JSON file

data = []

with open(json_file_path, 'r') as f:
    for line in f:
        data.append(json.loads(line))


# Select the 10 features
# features = ['dload', 'ct_state_ttl', 'rate', 'sttl', 'tcprtt', 'sload', 'state', 'ackdat', 'dinpkt', 'dbytes']
features = ['state', 'dbytes', 'rate', 'sttl', 'sload', 'dload', 'dinpkt', 'tcprtt', 'ackdat', 'ct_state_ttl']



## FOR LOOP TO STOP AFTER 10 PACKETS ARE PICKED

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

    # Add the prediction to the DataFrame
    df['prediction'] = predictions[0]

    # # Display the DataFrame in the table
    # table_placeholder.table(df)
    

        # Append the new packet to all_packets
    all_packets = all_packets.append(df, ignore_index=True)

    # Display all_packets in the table
    table_placeholder.table(all_packets)

    print(selected_data, ':', predictions)

    # Wait for 5 seconds before selecting the next packet
    time.sleep(5)






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












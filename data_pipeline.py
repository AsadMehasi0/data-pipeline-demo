# %%
# !pip install -r requirements.txt

# %%
import functions as f
import time
import datetime

#################################### EXAMPLE OF HOW TO USE SECRETS ###############################################
import os
import base64

CLIENT_ID = os.environ["client_id"]
client_id_encoded = base64.b64encode(f"CLIENT_ID".encode("ascii"))
print(f"ID: {CLIENT_ID}")  # ***
print(f"ID encoded: {client_id_encoded}")
##################################################################################################################


print("Starting data pipeline at ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print("----------------------------------------------")

# Step 1: extract video IDs
t0 = time.time()
f.getVideoIDs()
t1 = time.time()
print("Step 1: Done")
print("---> Video IDs downloaded in", str(t1-t0), "seconds", "\n")

# Step 2: extract transcripts for videos
t0 = time.time()
f.getVideoTranscripts()
t1 = time.time()
print("Step 2: Done")
print("---> Transcripts downloaded in", str(t1-t0), "seconds", "\n")

# Step 3: Transform data
t0 = time.time()
f.transformData()
t1 = time.time()
print("Step 3: Done")
print("---> Data transformed in", str(t1-t0), "seconds", "\n")

# Step 4: Generate text emebeddings
t0 = time.time()
f.createTextEmbeddings()
t1 = time.time()
print("Step 4: Done")
print("---> Embeddings generated in", str(t1-t0), "seconds", "\n")



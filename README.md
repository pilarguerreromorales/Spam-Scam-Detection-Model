# Spam-Scam-Detection-Model

## Overview
In this project, we developed a dual framework that simulates both attacker and defender roles using fine-tuned LLMs, as spam/scam data to train our detection model was limited. At its core is a RoBERTa-based spam detector that achieved near-perfect classification performance. This framework powers **Scam Busters**, our proposed end-user application for real-time scam message detection.

With the rise of accessible LLMs (Large Language Models), malicious messages can now be generated at scale with convincing language and fluency, making traditional keyword or volume based filters much less effective at detecting and flagging them as scam or spam. In response, this project tackles this challenge and introduces a practical, AI powered approach to detect and counter them effectively.

To build this solution, we designed a dual framework that simulates both the attacker and defender roles using fine tuned LLMs, a necessary step due to limited availability of real world scam data. At the heart of our system is a RoBERTa based spam detector, which achieved a really good performance in classifying this type of messages. This framework powers Scam Busters, our prototype tool for real time scam detection.

## Setup Instructions (For Application Demo)
1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
3. **Download model outputs**  
   Follow the instructions in the `Outputs/` folder to download the file `roberta_detector_outputs.zip`. This folder contains the checkpoint for our trained RoBERTA Detector Model and is the one used in our application.
4. **Unzip the model folder**  
   Uncompress the zip file and store the folder in the `Outputs/` folder (if not, adjust the file path in the Python code).
5. **Run the prototype.**  

## Repository Structure
The following shocases the structure of the main folders in the repository. Additional README.md files have been included in some folders to facilitate usability and understanding.

- **Application/** – Python code to run the prototype/demo
- **Notebooks/** – All notebooks used during the project, including trials and main versions
- **Outputs/** – Instructions and assets to download saved outputs for faster testing
- **data/** – Original datasets and manual dataset download instructions (generated data should also be stored here)
- **requirements.txt** – Python dependencies needed to run the project
- **README.md** – This file


## Known Limitations
- Base or Original data used for the project is limited: has repetitive examples and strucutres that are easily learnt by models.
- Github's repository size: due to the limited space allowed in free accounts, notebook outputs had to be cleared and some files need to be manually downloaded and included in different folders in order to replicate this project. To counter this, some of the checkpoints used throughout the project are included in a shared Drive folder for manual download.
- **IMPORTANT**: some file paths throughout some notebooks **must be changed/adapted** to personal usage.

## Team
- Matías Arévalo
- Pilar Guerrero
- Moritz Goebbels
- Tomás Lock
- Allan Stalker 

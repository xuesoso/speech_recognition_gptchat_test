# Playing around with chatGPT API

Learning from chatGPT on how to build a speech-text-speech app to verbally communicate with chatGPT.

Install requirements
--------------

- Install anaconda/miniconda with python 3.7. 

- Install the dependent packages with:

        conda install -r requirements.txt

- ensure you have a functional microphone connected to your computer.

How to use
----------

1. configure your chatGPT key and save it to a safe location outside of this repository:

        echo "XXX-XXXXXXXXX" >> ~/.chatgpt_credentials/api_key.key

2. execute the following command and speak into the microphone:

        python run_speech_text_speech_gptchat.py

3. text transcripts of the input prompt and the response from chatGPT will be found with unique timestamps in the `./output/` directory.


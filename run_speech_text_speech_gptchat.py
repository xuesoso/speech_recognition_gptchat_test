#%%```python

def __main__():
    import speech_recognition as sr
    import openai, os, yaml, logging, datetime, uuid, subprocess

    # Set the log level to INFO and specify a custom log format
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    with open('config.yaml') as f:
        configs = yaml.load(f, Loader=yaml.FullLoader)

    api_dir = '{:}/{:}'.format(os.path.expanduser('~'), configs['api_key_path'])
    with open (api_dir, 'r') as f:
        api_key = f.read().strip()

    r = sr.Recognizer()

    with sr.Microphone() as source:
        logging.info("Speak now:")
        audio = r.listen(source)

    try:
        #### Requires internet connection ####
        text = r.recognize_google(audio, show_all=False)
        #### Does not require internet connection ####
        # text = r.recognize_sphinx(audio)
        logging.info("You asked: {}".format(text))
    except sr.UnknownValueError:
        logging.error("Could not understand audio")
    except sr.RequestError as e:
        logging.error("Could not request results; {0}".format(e))

    # Set the OpenAI API key
    openai.api_key = api_key

    # Define the prompt for the chatbot
    prompt = text
    # prompt = "Can you tell me about yourself?"

    # Request a response from the chatbot
    response = openai.Completion.create(
        prompt=prompt,
        engine=configs['engine'],
        max_tokens=configs['max_tokens'],
        n=configs['n'],
        temperature=configs['temperature'],
        )

    logging.info("chatGPT response: {:}".format(response['choices'][0]['text']))

    #### Write output if configs['write_output'] is True ####

    if configs['write_output']:
        os.makedirs(configs['output'], exist_ok=True)
        # Get the current date and time and then
        # format the date and time as a string (e.g. "2022-12-08-13-45-32")
        timestamp = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

        # Generate a unique ID (UUID)
        uid = uuid.uuid4().hex

        # Combine the timestamp and unique ID to create the file name
        fn = os.path.join(configs['output'], f'{timestamp}-{uid}.txt')

        logging.info("writing output to: {:}".format(fn))

        with open(fn, 'w') as w:
            w.write('input prompt:\n\n')
            w.write('{:}\n'.format(prompt))
            w.write('---------\n'.format(prompt))
            w.write('chatGPT response:\n\n')
            w.write('{:}\n'.format(response['choices'][0]['text'].strip()))
        
        # Generate speech from the text file
        speech_generation_cmd = ' '.join(['python', 'speech_generation_gtts.py', fn])
        subprocess.run(speech_generation_cmd, shell=True, check=True)
        logging.info("speech generation complete")

#%%```python

if __name__ == '__main__':
    __main__()

#%%```python

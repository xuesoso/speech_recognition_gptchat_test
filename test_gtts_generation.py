from gtts import gTTS
import os, yaml, logging, sys

def main():
    # Set the log level to INFO and specify a custom log format
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    keys_to_load = ['output', 'language']
    with open('config.yaml') as f:
        configs = yaml.safe_load(f)
    configs = {key:configs[key] for key in keys_to_load}

    gptchat_output = sys.argv[1]
    fn_path = gptchat_output.split('/')[-1].split('.')[0] + '.mp3'
    
    # Text that you want to convert to speech
    with open(gptchat_output, 'r') as f:
        text = f.read()

    logging.info('reading chatGPT output: {:}'.format(gptchat_output))

    # Language in which you want to convert the text
    language = configs['language']

    # Create a gTTS object
    speech = gTTS(text=text, lang=language)

    # Save the converted speech to a file
    speech.save(os.path.join(configs['output'], fn_path))

if __name__ == '__main__':
    main()
from gtts import gTTS
import os, yaml, logging, sys
_playsound_ = True

def main():
    # Set the log level to INFO and specify a custom log format
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    keys_to_load = ['output', 'language']
    with open('config.yaml') as f:
        configs = yaml.safe_load(f)
    configs = {key:configs[key] for key in keys_to_load}

    # Create the output directory if it doesn't exist
    os.makedirs(configs['output'], exist_ok=True)

    # Set the output path for mp3 file
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
    logging.info('saving converted speech mp3: {:}'.format(gptchat_output))
    mp3_path = os.path.join(configs['output'], fn_path)
    speech.save(mp3_path)

    if _playsound_:
        from playsound import playsound
        playsound(mp3_path, True)

if __name__ == '__main__':
    main()

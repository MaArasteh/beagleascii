import textwrap
import argparse

def read_ascii_art(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def format_message(message, width=40):
    return textwrap.fill(message, width=width)

def beagle_say(message, ascii_art_path):
    global combined
    ascii_art = read_ascii_art(ascii_art_path)
    formatted_message = format_message(message)
    
    # Construct the speech bubble
    bubble_width = max(len(line) for line in formatted_message.split('\n'))
    bubble_top = " " + "_" * (bubble_width + 2)
    bubble_middle = "\n".join([f"< {line.ljust(bubble_width)} >" for line in formatted_message.split('\n')])
    bubble_bottom = " " + "-" * (bubble_width + 2)
    
    speech_bubble = f"{bubble_top}\n{bubble_middle}\n{bubble_bottom}"
    
    combined = f"{speech_bubble}\n{ascii_art}"
    print(combined)

def extract_to_txt(file_path):
    with open(file_path, 'w') as f:
        f.write(combined)

def main():
    parser = argparse.ArgumentParser(description="A script similar to cowsay but with a custom ASCII art character.")
    parser.add_argument('message', help="The message to be displayed.")
    parser.add_argument('-ba', '--beagleascii', help="Path to the .beagleascii file.", default='snoopy.beagleascii')
    parser.add_argument('-ext', '--extract', help="Extract ASCII to file", default=None)
    
    args = parser.parse_args()
    
    try:
        beagle_say(args.message, args.beagleascii)
    except FileNotFoundError:
        print("No! This is not correct file path. Give a correct BeagleASCII file (.beagleascii). If you deleted snoopy.beagleascii, recover it or download it again from BeagleASCII GitHub repository. ")

    if not args.extract:
        pass
    else:
        extract_to_txt(args.extract)

if __name__ == "__main__":
    main()

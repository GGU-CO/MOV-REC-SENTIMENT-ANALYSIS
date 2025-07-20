import re
import csv

def extract_dialogues(script_path):
    with open(script_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    dialogues = []
    current_character = None
    current_dialogue = []

    # Iterate through the lines in the script
    for i in range(len(lines) - 1):
        line = lines[i].strip()
        next_line = lines[i + 1].strip()

        # Regular expression to match character lines (uppercase, may contain numbers or certain symbols)
        is_character_line = re.match(r"^[A-Z0-9# ]+(?<!:)$", line)

        # Check if the line matches the character line pattern and is followed by a non-empty line
        if is_character_line and line and next_line:
            if current_character:
                # Save the previous dialogue before starting a new one
                dialogues.append((current_character, " ".join(current_dialogue).strip()))
            current_character = line
            current_dialogue = [next_line]
        elif current_character and line:
            # Continue capturing dialogue if the line is not empty
            current_dialogue.append(line)
        elif current_character and not line:
            # Stop capturing dialogue on empty line
            dialogues.append((current_character, " ".join(current_dialogue).strip()))
            current_character = None
            current_dialogue = []

    # Append the last captured dialogue if not ended by an empty line
    if current_character and current_dialogue:
        dialogues.append((current_character, " ".join(current_dialogue).strip()))

    return dialogues

def save_to_csv(dialogues, output_csv_path):
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Character', 'Dialogue'])
        for name, dialogue in dialogues:
            writer.writerow([name, dialogue])

script_path = 'C:\Users\khmra\Desktop\Avnegers\Avengers_Script.txt'
output_csv_path = 'Avengers_Dialogues.csv'

# Extract and save dialogues
dialogues = extract_dialogues(script_path)
save_to_csv(dialogues, output_csv_path)

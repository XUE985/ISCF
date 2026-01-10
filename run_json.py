import json

def read_qa_data(file_path):
    try:
    
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"wrong: {file_path}")
        return None

if __name__ == "__main__":

    file_name = "qa_dataset.json"
    qa_list = read_qa_data(file_name)

    if qa_list:
        print(f"read {len(qa_list)} ：\n")
        for item in qa_list:
            print(f"model: {item['model']}")
            print(f"question: {item['question']}")
            print(f"answer: {item['answer']}")
            print("-" * 20)
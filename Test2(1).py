import pandas as pd
import openai

class ExcelReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_excel(self):
        try:
            self.data = pd.read_excel(self.file_path)
            return self.data
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return None

class GPTSummarizer:
    def __init__(self, api_key):
        openai.api_key = api_key

    def summarize(self, text):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Updated model
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Summarize the following data:\n{text}"}
                ],
                max_tokens=100
            )
            summary = response.choices[0].message['content'].strip()
            return summary
        except Exception as e:
            print(f"Error during summarization: {e}")
            return None


class RAGSystem:
    def __init__(self, file_path, api_key):
        self.reader = ExcelReader(file_path)
        self.summarizer = GPTSummarizer(api_key)

    def execute(self):
        data = self.reader.read_excel()
        if data is not None:
            text_data = data.to_string(index=False)
            summary = self.summarizer.summarize(text_data)
            print("Summary:\n", summary)
        else:
            print("No data to summarize.")

# Example usage
if __name__ == "__main__":
    file_path = "Employee_Data.xlsx"  # Path to the Excel file
    api_key = "sk-OOMMKS2qwt1tsKq9BLL7h2hdXNpfY_N-imtNXzWJkqT3BlbkFJ-ZOAM1TlNm1w0zSCOJ2w7ST3p4RSto8FN1X4VufYwA"  
    rag_system = RAGSystem(file_path, api_key)
    rag_system.execute()

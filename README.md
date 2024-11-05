
# MeddiHelp & PillPaw

**MeddiHelp** is a user-centric web platform designed to offer general medical guidance and support, developed with HTML, CSS, and JavaScript to ensure a smooth, visually engaging experience. This website includes an AI-based chatbot, **PillPaw**, which is positioned to provide users with reliable, concise health-related responses. MeddiHelp aims to be an accessible resource for users seeking information on wellness, common symptoms, and basic medical topics.

**PillPaw**, MeddiHelp’s AI-powered assistant, is developed to respond to user queries with short, clear, and straightforward health information. Leveraging the Gemini AI API, PillPaw operates as an interactive virtual assistant capable of delivering answers to questions about symptoms, wellness, and other basic health concerns. Although it’s designed to give general medical information only, PillPaw is dedicated to providing easy-to-understand guidance that promotes wellness and informed decision-making.

## Getting Started

### Prerequisites

To begin working with MeddiHelp, ensure your system meets the following prerequisites:

1. **Python**: MeddiHelp requires Python, which will be used to manage server-side operations and dependencies.
2. **Git**: Ensure Git is installed on your machine to facilitate repository cloning.

### Cloning the Repository

To get the latest version of MeddiHelp, clone the repository from GitHub. This will create a local copy of the project files and directory structure on your machine.

```bash
git clone https://github.com/shrek1918/MeddiHelp.git
cd MeddiHelp
```

### Installing Dependencies

MeddiHelp relies on certain Python libraries to function properly. To install the necessary dependencies, use the following command:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains a list of all libraries needed for MeddiHelp to function. This includes web framework libraries like Flask for backend operations, as well as any packages required by PillPaw.

### Setting Up Environment Variables

To securely manage your API keys and any sensitive data, you’ll need to create a `.env` file:

1. In the `MeddiHelp` directory, create a `.env` file.
2. Go to [Google-AI Studio](https://aistudio.google.com/apikey) and generate your aAPI Key.
3. Add your Google API key by creating a .env file as follows:

   ```plaintext
   GOOGLE_API_KEY=your_api_key_here
   ```

This environment variable is essential for PillPaw to access the Gemini AI API for generating responses.

### Running the Application

Once all dependencies are installed, start the application using the following command:

```bash
python app.py
```

Upon successful execution, you should see output similar to the following in your terminal:

```
================= Start Your Query =================
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
================= Happy Chatting =================
```

### Accessing the Interface

To access MeddiHelp’s interface, open a web browser and go to the address displayed in your terminal, usually [http://127.0.0.1:5000/](http://127.0.0.1:5000/). This is the primary user interface for MeddiHelp where users can interact with the chatbot and explore available resources.

## Features

MeddiHelp offers a range of features to assist users with basic medical inquiries:

- **Intuitive Interface**: MeddiHelp is built to be user-friendly, enabling users of all technical backgrounds to navigate and access information effortlessly.

- **Ask our Chatbot**: The core feature of MeddiHelp, PillPaw, is a conversational AI chatbot that answers user queries on general medical topics. With its integration with the Gemini AI API, PillPaw provides quick responses related to symptoms, wellness tips, and general health inquiries. Designed to be brief and clear, the answers ensure users receive valuable, easy-to-understand information.

- **General Health Tips**: MeddiHelp also includes a section with curated health tips and wellness advice to encourage a healthy lifestyle. This area may provide insights on topics like nutrition, exercise, and self-care practices.

### Notes on Functionality

While MeddiHelp is a front-end-based project with basic backend setup for demonstration purposes, several features, such as user authentication or data persistence, are simplified or non-functional. The primary interactive element, PillPaw, is fully operational and optimized for delivering quick medical insights.

## Future Development

In future iterations, MeddiHelp aims to include additional features, such as:

- **Symptom Checker**: An expanded symptom analysis tool to help users assess health concerns.
- **Medical Resources Database**: An integrated database of general medical conditions, treatments, and guidelines.
- **User Accounts**: Personalized accounts to store user history, enabling continuity in advice and guidance.

MeddiHelp and PillPaw provide an essential foundation for a general medical assistance platform that can be expanded in future development cycles. Whether users seek quick health tips or general guidance, MeddiHelp and PillPaw aim to make health information easily accessible and understandable.

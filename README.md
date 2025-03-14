# AutoGen Azure OpenAI Chatbot

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28%2B-FF4B4B.svg)](https://streamlit.io)
[![AutoGen](https://img.shields.io/badge/autogen-0.2.0%2B-green.svg)](https://github.com/microsoft/autogen)

A powerful chatbot interface that leverages Microsoft's AutoGen framework with Azure OpenAI Services to provide intelligent responses using multiple specialized agents.

## 🌟 Features

- **Multi-Agent System**:
  - 🌐 Web Surfer Agent: Browses the web for real-time information
  - ✅ Verification Assistant: Verifies and summarizes information
  - 👤 User Proxy: Provides human feedback when needed
- **Modern Interface**:
  - 💻 Clean web interface built with Streamlit
  - 📝 Real-time chat history
  - 🔍 Configuration status display
  - ⚠️ Comprehensive error handling and user feedback

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- Azure OpenAI API access
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/loraddineva/autogendemo.git
cd autogendemo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.template .env
```

4. Configure your `.env` file with Azure OpenAI credentials:
```env
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=your_endpoint_here
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name_here
```

### Running the Application

Launch the chatbot:
```bash
streamlit run app.py
```

The application will automatically open in your default web browser.

## 🔧 Configuration

The chatbot behavior is controlled by `team-config.json`. You can modify this file to:
- Adjust agent behaviors
- Change model parameters
- Update conversation settings
- Modify termination conditions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🔍 Troubleshooting

If you encounter issues:

1. Verify environment variables in `.env`
2. Check Azure OpenAI deployment status
3. Review console output for errors
4. Confirm API permissions
5. Check Python version compatibility

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

If you have any questions or need help, please:
1. Check the [Issues](https://github.com/loraddineva/autogendemo/issues) page
2. Create a new issue if your problem isn't already listed
3. Provide as much context as possible in your issue 
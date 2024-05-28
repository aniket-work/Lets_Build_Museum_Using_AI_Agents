## 🏛️ Let's Build a Museum Using AI Agents 🏛️

In this project, we'll build virtual museum using AI agents.  Get ready for an exciting journey!

**Prerequisites:**

* Python installed on your system.
* A basic understanding of virtual environments and command-line tools.

**Steps:**

1. **Virtual Environment Setup:**

   - Create a dedicated virtual environment for our project:
   
     ```bash
     python -m venv museum_with_ai_agents 
     ```

   - Activate the environment:
   
     * Windows:
        ```bash
        museum_with_ai_agents\Scripts\activate
        ```
     * Unix/macOS:
        ```bash
        source museum_with_ai_agents/bin/activate
        ```

2. **Install Project Dependencies:**

   - Grab the necessary packages with the help of `pip`:
   
     ```bash
     pip install -r requirements.txt
     ```

3. **Install Ollama:**

   - Download Ollama from the official website: [https://ollama.com/download](https://ollama.com/download)
   - Follow the installer instructions for your operating system (Windows or macOS).
   - Once installed, launch Ollama.

4. **Install LLaMA-3:**

   - Within the Ollama application, download and run the LLaMA-3 language model:
   
     ```bash
     ollama run llama3:8b
     ```

5. **Start Building!** (Not included in this snippet)
   - Now you're ready to use your AI agents. The rest of the tutorial would involve code and instructions on how to interact with the models, design your museum layout, and create exhibits.
   
6. **Install https://mpv.io/ for your resp. OS**
    ```bash
    Open Powershell terminal and run below command 
    choco install mpv
    ```
   
7. Run 
```python
(museum_with_ai_agents) ~\PycharmProjects\Lets_Build_Museum_Using_AI_Agents>python main.py
```
8. test
```commandline
(museum_with_ai_agents) ~\PycharmProjects\Lets_Build_Museum_Using_AI_Agents>curl -X POST -H "Content-Type: application/json" -d "{\"query\": \"What day comes after Tuesday?\"}" http://127.0.0.1:8080/llm
```

9. run mesuem
```python
streamlit run museum_board.py
```

---

**Additional Tips:**

* Consider using a code editor (like VS Code) for better organization.
* Refer to the Ollama documentation for more detailed instructions and model options.
* Get creative with your AI agents and the exhibits you curate!

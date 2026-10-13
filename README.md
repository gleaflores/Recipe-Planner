# AI Meal Recipe Planner 🍳

A cloud-native, AI-powered web application that generates healthy, structured cooking recipes based on user-inputted ingredients, dietary restrictions, and specific fitness goals. This project utilizes a **Python + Streamlit** architecture, connects to the high-performance **Groq Cloud API** for text inference, and is fully deployed on an **AWS EC2** instance.

---

## 🚀 Live Application
* **Deployment URL:** `http://13.60.27.7:8501`
* **Cloud Infrastructure:** AWS EC2 (Ubuntu Server 24.04 LTS)

---

## 🛠️ Tech Stack & Architecture

* **Frontend & Backend UI:** Python 3.x with **Streamlit** (bypasses traditional heavy JS/HTML frameworks for rapid interface assembly).
* **Generative AI Inference Engine:** **Groq Cloud API** running the active free developer-tier production model (**`gemma2-9b-it`**).
* **Cloud Hosting Platform:** **AWS EC2** configured with explicit network route tables and custom firewall parameters (Level 3 Infrastructure Blueprint).

---

## 📋 Project Development Phases

### Phase 1: Research & Scope
* Developed the functional requirements for an automated kitchen assistant focused on food-waste reduction.
* Analyzed multiple GenAI vendors and selected the Groq Cloud SDK due to its superior inference speeds, comfortable developer limits, and zero-cost accessibility.

### Phase 2: Implementation & Local Validation
* Built the core processing script (`recipe_planner.py`) featuring structural input controls and error handling.
* Engineered strict prompt structures to guarantee the AI response maps to organized Markdown categories (Nutritional Overview, Prep Time, Step-by-Step Instructions).

### Phase 3: Cloud Deployment & Security Configuration
* Provisioned an Ubuntu-backed virtual web server on the AWS cloud fabric.
* Modified underlying AWS Security Group inbound policies to establish safe operational traffic lines (Port 22 for SSH management and Port 8501 for external HTTP application traffic).
* Configured isolated background processes using `nohup` execution wrappers to maintain server persistence.

---

## 🔧 Comprehensive Troubleshooting Ledger

Below is the compilation of the real-world technical and infrastructure errors encountered and successfully resolved during development:

| Phase | Technical Error / Block | Underlying Root Cause | Engineering Solution |
| :---: | :--- | :--- | :--- |
| **2** | `The term 'pip' is not recognized...` | Python environment binaries were unmapped from the global system PATH execution variables. | Bypassed global paths by invoking the package installer directly through the Python wrapper flag (`python -m pip install`). |
| **2** | `UnauthorizedAccess / Script Execution Disabled` | Windows OS security policies blocked the activation script (`Activate.ps1`) of the local virtual environment. | Executed `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process` to unlock execution privileges for the active shell session. |
| **2** | `ModuleNotFoundError: No module named 'streamlit'` | Dependencies were inadvertently installed into the global workspace before the local `venv` shell was active. | Activated the `venv` shell and forced execution alignment by re-running the installation command directly within the isolated scope. |
| **2** | `404 - model_not_found (llama-3.3-70b / llama-3.1-8b)` | The initial target model identifiers were retired and decommissioned from Groq's developer tier. | Audited the active vendor model registry and refactored payload strings to map to the supported production-tier endpoint (`gemma2-9b-it`). |
| **3** | `OSError: [Errno 99] Cannot assign requested address` | Streamlit attempted to bind its underlying Starlette web server directly to an external, unroutable public IP. | Altered the initialization parameters to use `--server.address 0.0.0.0`, forcing the listener across all local network adapters. |
| **3** | `ERR_CONNECTION_TIMED_OUT` (Private IP) | Attempted to access the live dashboard via an internal AWS private subnet IP block (`172.31.x.x`), which is unroutable publicly. | Swapped out the network string inside the web browser to target the true external `Public IPv4 address`. |
| **3** | `ERR_CONNECTION_TIMED_OUT` (Public IP) | The external browser request hit an AWS infrastructure firewall wall because traffic on Port 8501 was dropped by default. | Modified the active AWS Security Group's inbound rule table to explicitly allow incoming Custom TCP traffic on Port `8501` from anywhere. |
| **3** | `ModuleNotFoundError: No module named 'groq'` (On EC2) | The remote AWS Linux runtime environment was executing the target script outside of the configured Python virtual environment context. | Sourced the remote environment wrapper (`source venv/bin/activate`) and ran a explicit `pip install` loop to cleanly populate the server cache. |

---

## 🏃‍♂️ Local Installation & Setup

To pull this code and evaluate its functionality locally, execute the following block inside your terminal:

```bash
# 1. Clone the repository tree
git clone https://github.com
cd ai-meal-recipe-planner

# 2. Configure isolated environment wrapper
python -m venv venv
# On Windows PowerShell: Set-ExecutionPolicy Bypass -Scope Process; .\venv\Scripts\Activate.ps1
# On Mac/Linux: source venv/bin/activate
source venv/bin/activate

# 3. Synchronize project dependencies
python -m pip install streamlit groq pillow

# 4. Inject your Groq authentication credentials
# On Windows PowerShell: \$env:GROQ_API_KEY="your_key"
export GROQ_API_KEY="your_actual_groq_api_key_here"

# 5. Boot the engine locally
python -m streamlit run recipe_planner.py
```

---

## 📊 Evaluation & Future Improvements
* **Current Achievements:** Achieved an automated execution loop running on AWS infrastructure with high-speed generation rates.
* **Key Insights:** Gained practical validation experience dealing with virtual shell management, cloud firewall rules, and API lifecycle deprecation tracks.
* **Future Scaling Paths:** Intend to append an AWS RDS PostgreSQL database layer to securely cache user history, and utilize AWS Route 53 to map the raw cloud IP to a domain name.

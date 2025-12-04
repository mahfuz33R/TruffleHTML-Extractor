# TruffleHTML-Extractor

TruffleHTML-Extractor parses TruffleHog HTML reports, lists detector types, filters or extracts all findings, removes HTML tags, and outputs unique raw results with related repositories. Ideal for auditing leaked secrets and simplifying secret rotation.


---



```markdown
# 🔍 TruffleHog HTML Result Extractor

A Python tool that extracts **secrets**, **tokens**, and **raw results** from TruffleHog HTML output files.

The tool supports:

✔ Parsing TruffleHog HTML export  
✔ Collecting **unique Raw result values**  
✔ Filtering by **Detector Type**  
✔ Automatic filename generation (no overwrite)  
✔ Removing HTML tags from results  
✔ Producing clean output files  
✔ Listing available detector types for user to choose  
✔ Output includes Detector Type + Raw Result + All Repositories  

---

## 📌 Features

### ✅ 1. Load TruffleHog HTML file  
The tool reads **any HTML output** produced by TruffleHog or similar GitHub secret scanners.

---

### ✅ 2. Detect all available **Detector Types**
The tool scans the entire file and prints:

```

Detected Detector Types:

* AzureSasToken
* SlackWebhook
* GoogleAPIKey
* AWSSecretKey
* …

```

Then the user can choose one.

---

### ✅ 3. User chooses a specific detector OR press Enter  
- **Enter a detector name** → only extract secrets of that detector type  
- **Press Enter** → extract **all detector types**

---

### ✅ 4. Output file naming logic  
- If user selects `AzureSasToken`:  
  → Output file = `AzureSasToken.txt`

- If file exists:  
  → `AzureSasToken1.txt`  
  → `AzureSasToken2.txt`  
  → etc.

- If user extracts ALL:  
  → Output = `output.txt`, `output1.txt`, `output2.txt`, ...

---

### ✅ 5. Each result is UNIQUE  
If same Raw result appears multiple times from different repos, **only one is written**, but **all repositories are listed**.

---

### ✅ 6. Output format example

```

Detector Type: AzureSasToken
Raw result: [https://mahfuz33r.github.io/container/file.png](https://mahfuz33r.github.io/container/file.png)


Repositories:

* [https://github.com/consonant/business.git](https://github.com/consonant/business.git)

---

Detector Type: SlackWebhook
Raw result: [https://hooks.slack.com/services/xxx/yyy/zzz](https://hooks.slack.com/services/xxx/yyy/zzz)


Repositories:

* [https://github.com/example/project.git](https://github.com/example/project.git)

---

````

---

## 🛠 Installation

### **1. Install Python (3.8 or higher required)**  
Download from:  
https://www.python.org/downloads/

---

### **2. Clone the Repository**

```bash
git clone https://github.com/mahfuz33r/TruffleHTML-Extractor.git
cd TruffleHTML-Extractor
````

---

### **3. (Optional) Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

---

### **4. Install dependencies**

This script uses only built-in libraries, **no extra packages required** 🎉

---

## ▶️ **How to Run**

Place your TruffleHog HTML output file (example: `report.html`) inside the project folder.

Then run:

```bash
python extract.py
```

---

## 📝 **Program Flow Example**

### Step 1 — User Input:

```
Enter input HTML file path: report.html

Detected Detector Types:
 - AzureSasToken
 - SlackWebhook
 - StripeToken

Press ENTER to extract ALL detector types
Enter Detector Type to filter:
```

### Step 2 — User presses Enter (extract all)

```
✔ Scan & extraction complete!
✔ Total unique raw results: 4
✔ Saved to: output.txt
```

### Step 3 — Output written to:

```
output.txt
output1.txt  # if output.txt file already existed
```

---

## 📄 **Output File Structure**

Each secret entry looks like:

```
Detector Type: AzureSasToken
Raw result: https://datasheet.blob.core.windows.net/files/demo.png
Repositories:
  - https://github.com/project1/example.git
  - https://github.com/project2/example.git
------------------------------------------------------------
```

---

## 🧪 Supported Input Formats

* TruffleHog HTML export
* GitHub secret scan HTML
* Any text/HTML that contains patterns like:

```
Detector Type: X
Raw result: Y
Repository: Z
```

---

## 🧹 Cleaning & Sanitization

This tool automatically removes HTML tags including:

* `</h3>`
* `<pre>`
* `<div>`
* `<span>`
* etc.

Ensuring clean and readable output.

---

## 📦 File Included in this Project

```
extract.py        # main script
README.md         # documentation
```

---

## 💡 Use Cases

* Secret rotation
* Security auditing
* GitHub repo scanning
* CI pipeline secret validation
* Batch secret cleanup

---

## 📜 License

MIT License – free to use, modify, distribute.

---

## 🤝 Contribution

Pull requests are welcome!

---

## ✉️ Contact

If you need improvements or custom integration, feel free to open an issue.

```

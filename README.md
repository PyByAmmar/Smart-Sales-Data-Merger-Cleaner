
# Smart Sales Data Merger & Cleaner 

A robust Python tool designed to automate the merging and cleaning of multiple sales data files (CSV) into a single, clean Excel report. Built specifically to handle messy, real-world client data with encoding issues, missing values, and corrupted rows.

## Key Features
- **Multi-File Batch Processing**: Dynamically locates and merges all matching CSV files in a directory using `glob`.
- **Fault-Tolerant Parsing**: Skips bad or corrupted rows automatically (`on_bad_lines='skip'`).
- **Encoding Auto-Fix**: Handles Windows Arabic encoding (`cp1256`) and non-UTF-8 characters smoothly to prevent crash errors (`UnicodeDecodeError`).
- **Data Standardization**: Coerces invalid dates and drops incomplete or empty rows automatically.
- **Automated Monthly Aggregation**: Groups valid sales data by month and exports a clean `.xlsx` summary report.

## 🛠️ Built With
- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **OpenPyXL** - Excel file generation

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/PyByAmmar/Smart Sales Data Merger & Cleaner.git](https://github.com/YOUR_USERNAME/sales-data-merger.git)
   cd sSmart Sales Data Merger & Cleaner

So, you've used the RosterScraper. **How do you read your file?**

While the backend of this program is still on v2.0, you will need to manually convert your .csv (comma separated value document) files to .xlsx (Excel 2007-23+ spreadsheet document) files. 

Keep in mind that this program currently exports .csv files as semicolon-delimited, so this is a necessary process.

**Step 0:** ensure that you have your file(s) already exported from the RosterScraper and that you know their location. Let us assume that our files are named example_fine.csv, example_raw.csv, and are located on the Desktop.

**What is the difference between _fine.csv and _raw.csv?**
- The _fine.csv is what you, the end-user, will use. The _raw.csv is a debug generated in case things break due to a new Examsoft update.

**Step 1:** Create a new Excel file (.xlsx) by opening Excel, and clicking on Blank Workbook.

**Step 2:** In the top ribbon, navigate to Data > Get External Data > From Text.

**Step 3:** A dialog box should appear asking you to pick your file. Choose example_fine.csv (or whatever you've named your _fine.csv).

**Step 4:** A Text Import Wizard dialog box should appear. Make sure Delimited is checked, click the Next button.

**Step 5: [IMPORTANT]** On the Text Import Wizard (step 2 of 3), it will ask about your Delimiters. Uncheck the "Tab" delimiter, check the "Semicolon" delimiter. Click the Next button.

**Step 6:** Click the Next button when it asks about Dates, General, etc.

**Step 7:** Click the Next button when it asks where you'd like to save this. 

**Step 8:** Your data should look perfectly readable. If not, send me a message.

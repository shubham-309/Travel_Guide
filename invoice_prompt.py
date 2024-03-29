prompt_template = """As a technical bot, I need you to convert all of the invoice text into JSON format, ensuring that the output includes the following fields:

Sample Json:
{
  "Sender Information": "",
  "Recipient Information": "",
  "Invoice Number": "",
  "Invoice Date": "",
  "Due Date": "",
  "Purchase Order Number": "",
  "Post Office Number": "",
  "Itemized Description": "",
  "Total Amount Due": "",
  "Tax Information": "",
  "Discounts": "",
  "Subtotals": "",
  "Taxes": "",
  "Account Number": "",
  "Grand Total": "",
  "Payment Instructions": "",
  "Tracking Info": "",
  "Terms and Conditions": ""
}

Please note that you should include the currency sign if applicable. Make sure to exclude any extra text that is not part of the JSON format. Also, avoid providing answers outside the context and refrain from overfitting the information. """

import os
import markdown2
import pdfkit

def markdown_folder_to_pdf(folder_path, output_pdf_name):
    # CSS to ensure all headings are left-aligned
    css = """
    <style>
    h1, h2, h3, h4, h5, h6 {
        text-align: center;
    }
    </style>
    """
    html_content = '<meta charset="UTF-8">' + css  # Add CSS to the HTML content
    first_file = True  # Flag to prevent adding a page break before the first file

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_pdf_name), exist_ok=True)

    for markdown_file in sorted(os.listdir(folder_path)):
        if markdown_file.endswith('.md'):
            file_path = os.path.join(folder_path, markdown_file)
            with open(file_path, 'r', encoding='utf-8') as file:
                markdown_text = file.read()
                # Extract title from filename (remove digits, underscores, and the file extension)
                title = markdown_file.split('_', 1)[-1].replace('.md', '').replace('_', ' ').title()
                # Add a page break before each file's content except the first
                if first_file:
                    first_file = False
                else:
                    html_content += '<div style="page-break-before: always;"></div>'
                # Add the title and the converted Markdown content
                html_content += f"<h1><u>{title}</u></h1>" + markdown2.markdown(markdown_text)
                
    # Convert combined HTML to PDF
    pdfkit.from_string(html_content, output_pdf_name)


# Example usage
folder_path = '/Users/jvcte/Documents/School/Random py scripts/mdfiles'  # Update this path
output_pdf_name = '/Users/jvcte/Documents/School/Random py scripts/converted.pdf'  # Update this path
markdown_folder_to_pdf(folder_path, output_pdf_name)

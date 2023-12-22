# Creating Documentation for Argos

## Writing Documentation

1. **Create Individual Markdown Files**: For each aspect of your project, create a separate Markdown file. This includes an overview, getting started guides, etc.

2. **ChatGPT Usage Caution**: Do not use ChatGPT for creating Markdown files with sensitive content. Use it only for public, non-sensitive information.

3. **Markdown Syntax Reference**: Learn Markdown syntax from [Markdown Guide](https://www.markdownguide.org/basic-syntax/). For a visual preview, use [Dillinger](https://dillinger.io/).

4. **Converting Word to Markdown**: Convert Word documents to Markdown using [Word2MD](https://word2md.com/). Note that post-conversion editing might be necessary.

## Organizing Documentation

- **Tree Structure for Navigation**: Organize your documentation using a tree structure in a text file, as shown below:

    ```md
    nav:
      - Index:
        - Welcome: index.md
      - Project Title (e.g., PMS7003):
        - Section Title (e.g., Sensor Connection Guide): folder_name/file_name.md
        - Another Section Title: folder_name/another_file.md
    ```

    Each project should have its own folder. Name each Markdown file to clearly reflect its content.
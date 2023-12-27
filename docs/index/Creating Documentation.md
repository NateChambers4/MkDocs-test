# Creating Documentation for Argos

## Writing Documentation

1. **Create Individual Markdown Files**: For each aspect of your project, create a separate Markdown file. This includes an overview, getting started guides, etc.

2. **ChatGPT Usage Caution**: Do not use ChatGPT for creating Markdown files with sensitive content. Use it only for public, non-sensitive information. Using ChatGPT may be permitted if chat history is turned off. Go to Settings, Data Controls, Chat History and Training. Turn this setting off. (You must start a new chat)

3. **Markdown Syntax Reference**: Learn Markdown syntax from [Markdown Guide](https://www.markdownguide.org/basic-syntax/). For a visual preview, use [Dillinger](https://dillinger.io/).

4. **Converting Word to Markdown**: Convert Word documents to Markdown using [Word2MD](https://word2md.com/). Note that post-conversion editing might be necessary.

## Organizing Documentation

- **Tree Structure for Navigation**: Organize your documentation using a tree structure in a text file, as shown below:

    ```md
    nav:
      - Index:
        - Welcome: index.md
        - Creating Documentation: index/Creating Documentation.md
        
      - PMS7003:
        - Sensor Connection Guide: pms7003/PMS7003.md
        - Running the Script: pms7003/Running the Script.md
        - Understanding the Data: pms7003/Understanding the Data.md

      - Your Project Title:
        - Page 1 Title: projectFolderName/page1.md
        - Page 2 Title: projectFolderName/page2.md
    ```

    Each project should have its own folder. Name each Markdown file to clearly reflect its content.
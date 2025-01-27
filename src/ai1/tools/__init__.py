from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
  MDXSearchTool,
  SerperDevTool
)

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
read_resume = FileReadTool(file_path='/home/thomas/ai1/cv/cv-ts1.md')
semantic_search_resume = MDXSearchTool(mdx='/home/thomas/ai1/cv/cv-ts1.md')

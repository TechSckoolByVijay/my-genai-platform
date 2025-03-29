from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import BaseTool
import yfinance as yf
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class Fetch_stock_data(BaseTool):
    name: str = "fetch_stock_data"
    description: str = "Fetches real-time stock data including price, P/E ratio, market cap, beta, and dividend yield."
    
    def _run(self, stock_symbol: str)-> str:
        """Fetches real-time stock data including price, P/E ratio, market cap, beta, and dividend yield."""
        stock = yf.Ticker(stock_symbol)
        #stock = ""
        stock_info = stock.info

        return f"""
		  Stock: {stock_info.get('longName', stock_symbol)}
		- Price: ₹{stock_info.get('currentPrice', 'N/A')}
		- P/E Ratio: {stock_info.get('trailingPE', 'N/A')}
		- Market Cap: {stock_info.get('marketCap', 'N/A')}
		- Beta (Volatility): {stock_info.get('beta', 'N/A')}
		- Dividend Yield: {stock_info.get('dividendYield', 'N/A')}%
		- Debt-to-Equity Ratio: {stock_info.get('debtToEquity', 'N/A')}
		"""


NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")  # Store API key in environment variable

class Fetch_stock_news(BaseTool):
    name: str = "fetch_stock_news"
    description: str = "Fetches recent financial news related to a stock and determines sentiment (Positive/Neutral/Negative)."
    
    def _run(self, stock_symbol: str)-> str:
        url = f"https://newsapi.org/v2/everything?q={stock_symbol}&language=en&sortBy=publishedAt&apiKey={NEWSAPI_KEY}"
        response = requests.get(url)
        news_data = response.json()
        
        if "articles" in news_data and news_data["articles"]:
            top_articles = news_data["articles"][:3]  # Get top 3 news headlines
            news_summary = "\n".join([f"- {article['title']} ({article['source']['name']})" for article in top_articles])
            # Basic sentiment analysis: Count positive vs negative words
            positive_words = ["gain", "growth", "profit", "surge", "strong"]
            negative_words = ["loss", "decline", "fall", "weak", "drop"]
            sentiment_score = sum(1 for word in positive_words if word in news_summary.lower()) - \
                              sum(1 for word in negative_words if word in news_summary.lower())

            sentiment = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"

            return f"""
				Sentiment for {stock_symbol}: {sentiment}
				Latest News:
			{news_summary}
            """
        else:
            return f"No recent news found for {stock_symbol}."







@CrewBase
class StockMarketAnalysis():
	"""StockMarketAnalysis crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def risk_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['risk_analyst'],
			tools=[Fetch_stock_data()],
			verbose=True
		)

	@agent
	def market_sentiment_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['market_sentiment_analyst'],
   			tools=[Fetch_stock_news()],
			verbose=True
		)
	@agent
	def investment_advisor(self) -> Agent:
		return Agent(
			config=self.agents_config['investment_advisor'],
			tools=[Fetch_stock_data(), Fetch_stock_news()],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def risk_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['risk_analysis_task'],
		)

	@task
	def sentiment_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['sentiment_analysis_task']
		)
	@task
	def investment_recommendation_task(self) -> Task:
		return Task(
			config=self.tasks_config['investment_recommendation_task']
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the StockMarketAnalysis crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)

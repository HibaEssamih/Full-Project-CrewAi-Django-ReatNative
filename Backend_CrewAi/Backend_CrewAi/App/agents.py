from textwrap import dedent
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from .tools.ExaSearchTool import ExaSearchTool

llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             verbose=True,
                             temperature=0.6,
                             google_api_key="AIzaSyAjiz-9TsZ7CbhjF_gRioS-VqLPVPVpjUQ")


class LegalQueryAgents():
    def data_gathering_agent(self):
        return Agent(
            role='Legal Data Gatherer',
            goal='Gather relevant legal information from various sources',
            tools=ExaSearchTool.tools(),
            llm=llm,
            backstory=dedent("""\
                    As a Legal Data Gatherer, your task is to collect comprehensive
                    information on Canadian laws relevant to the given query."""),
            verbose=True
        )

    def natural_language_processing_agent(self):
        return Agent(
            role='NLP Specialist',
            goal='Process legal queries using Natural Language Processing techniques',
            tools=ExaSearchTool.tools(),
            llm=llm,
            backstory=dedent("""\
                    As an NLP Specialist, your role is to analyze and understand legal queries
                    using advanced Natural Language Processing algorithms."""),
            verbose=True
        )

    def search_algorithm_agent(self):
        return Agent(
            role='Search Algorithm Developer',
            goal='Develop algorithms to search for legal information efficiently',
            tools=ExaSearchTool.tools(),
            llm=llm,
            backstory=dedent("""\
                    As a Search Algorithm Developer, your task is to create algorithms
                    to search the web effectively and filter results for accuracy
                    and reliability."""),
            verbose=True
        )

    def legal_analysis_agent(self):
        return Agent(
            role='Legal Analyst',
            goal='Analyze legal documents to provide accurate answers',
            tools=ExaSearchTool.tools(),
            llm=llm,
            backstory=dedent("""\
                    As a Legal Analyst, your expertise is crucial in analyzing legal
                    documents and statutes to extract relevant information for
                    answering legal queries."""),
            verbose=True
        )

    def quality_assurance_agent(self):
        return Agent(
            role='Quality Assurance Specialist',
            goal='Ensure the accuracy and reliability of legal answers',
            tools=ExaSearchTool.tools(),
            llm=llm,
            backstory=dedent("""\
                    As a Quality Assurance Specialist, your role is to verify the accuracy
                    and reliability of the legal answers provided by the AI agents."""),
            verbose=True
        )

    def report_generation_agent(self):
        return Agent(
            role='Report Generator',
            goal='Generate concise reports summarizing legal analysis',
            tools=ExaSearchTool.tools(),
            llm=llm,
            backstory=dedent("""\
                    As a Report Generator, your task is to create concise reports summarizing
                    the legal analysis and providing answers to legal queries."""),
            verbose=True
        )
    
    def decision_maker_agent(self):
        return Agent(
            role='Decision Maker',
            goal='Make informed decisions based on legal analysis and context',
            tools=ExaSearchTool.tools(),
            llm=llm,
            backstory=dedent("""\
                    As a Decision Maker, your role is to make informed decisions based on
                    the analysis of legal data and understanding of the context."""),
            verbose=True
        )

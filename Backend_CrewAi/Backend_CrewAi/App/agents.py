from textwrap import dedent
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from .tools.ExaSearchTool import ExaSearchTool

llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             verbose=True,
                             temperature=0.6,
                             google_api_key="")


class LegalQueryAgents():
    
    def check_legal_assistance_agent(self):
        return Agent(
            role='Legal Assistance Checker',
            goal='Check if a query needs legal assistance or not',
            tools=[],  
            llm=llm,  
            backstory = dedent("""\
                As a Legal Assistance Checker, your task is to determine whether a given query 
                requires legal assistance or not. You need to analyze the query along with the 
                chat history to make a decision. Factors such as the presence of legal terms, 
                sensitive topics, and past interactions in the chat history will influence your decision. 
                This comprehensive approach ensures that you provide accurate and relevant assistance 
                based on the context of the conversation."""),

            verbose=True
        )
        
    def document_generation_check_agent(self):
        return Agent(
            role='Document Generation Checker',
            goal='Check if a query is for document generation',
            tools=[],  
            llm=llm,
            backstory=dedent("""\
                As a Document Generation Checker, your task is to determine whether a given query 
                is for document generation or not. You need to analyze the query to identify any 
                indications of a request for document creation. This role ensures that document 
                generation requests are appropriately identified and handled."""),
            verbose=True
        )
        
    def simple_query_agent(self):
        return Agent(
            role='Simple Query Analyst',
            goal='Analyze simple queries and provide helpful responses, showcasing ability to assist with legal information',
            tools=[],  
            llm=llm,
            backstory=dedent("""\
                As a legal ai assistant, your task is to analyze simple queries and
                provide straightforward responses. You can assist users with a wide range
                of legal topics and showcase our ability to help with legal information 
                on any topic. This role is suitable for handling non-legal inquiries or 
                basic questions while demonstrating our expertise in legal matters."""),
            verbose=True
        )

            
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
                    using advanced Natural Language Processing algorithms. """),
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
        
    
    def document_generation_submission_agent(self):
        return Agent(
            role='Document Generation Agent',
            goal='Prompt users to provide necessary information and extract it for document generation',
            tools=[],  
            llm=llm,  
            backstory=dedent("""\
                As a Document Generation Agent, your task is to both prompt users to provide necessary 
                information for document generation and to extract this information from their responses. 
                You will interact with users to gather details about the type and topic of the document needed 
                and ensure all required details are accurately extracted. Your role is crucial in ensuring that 
                users understand the importance of providing this information and that all needed details are 
                collected for the document generation process."""),
            verbose=True
        )
        
    def document_generation_agent(self):
        return Agent(
            role='Document Generation Agent',
            goal='Prompt users to extract necessary information, and generate a legal letter based on the provided and extracted information.',
            tools=[],  
            llm=llm,  
            backstory=dedent("""\
                As a Document Generation Agent, your task is to extract relevant details from the chat history, and create the document. 
                You will ensure all required details are accurately extracted. And that all needed details are collected 
                and used effectively for the document generation process."""),
            verbose=True
        ) 
    
    def document_check_agent(self):
        return Agent(
            role='Document Check Agent',
            goal='Ensure all necessary information for document creation is available and return a boolean indicating completeness.',
            tools=[],  
            llm=llm,  
            backstory=dedent("""\
                As a Document Check Agent, your task is to verify that all necessary information 
                for creating a document is present based on the user's query and chat history. 
                You will analyze the provided information and determine if it is complete. 
                Your role is crucial in ensuring that the document can be accurately and completely generated."""),
            verbose=True
        )


        
    
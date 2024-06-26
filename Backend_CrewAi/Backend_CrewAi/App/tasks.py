from textwrap import dedent
from crewai import Task

class LegalQueryTasks():
    def check_legal_assistance_task(self, agent, query, chat_history=None):   
        needs_legal_assistance = False  
        
        return Task(
            description=dedent(f"""\
                Check if the query or the chat history requires or contains legal assistance or not.
                
                Query: {query}
                Chat History: {chat_history}"""),
            
            expected_output=dedent("""\
                Boolean indicating whether legal assistance is needed."""),
            async_execution=False,
            agent=agent,
            return_value=needs_legal_assistance
        )
        
    def document_generation_check_task(self, agent, query, chat_history=None):
        is_document_generation_query = False        
        return Task(
            description=dedent(f"""\
                Check if the query is for document generation.
                
                Query: {query}"""),
            expected_output=dedent("""\
                Boolean indicating whether the query is for document generation or not."""),
            async_execution=False,
            agent=agent,
            return_value=is_document_generation_query
    )

        
    def simple_query_analysis_task(self, agent, query, chat_history=None):
        return Task(            
            description=dedent(f"""\
                Analyze the query and provide a response, showcasing the ability to assist with legal information on any topic.
                
                Query: {query}
                Chat History: {chat_history}"""),
            expected_output=dedent("""\
                Response to the query, demonstrating our ability to assist with legal information."""),
            async_execution=False,  # Assuming synchronous execution
            agent=agent
        )

        
    def data_gathering_task(self, agent, query, chat_history=None):
        return Task(
            description=dedent(f"""\
                Gather information on Canadian laws related to the given query.
                Utilize legal databases, government websites, and reputable law
                firms' resources to collect relevant data.

                Query: {query}
                Chat History: {chat_history}"""),
            expected_output=dedent("""\
                Comprehensive collection of legal information related to the query."""),
            async_execution=True,
            agent=agent
        )

    def natural_language_processing_task(self, agent, query, chat_history=None):
        return Task(
            description=dedent(f"""\
                Process the legal query using Natural Language Processing (NLP)
                algorithms. Parse the question, identify key legal concepts,
                and understand the context of the inquiry.

                Query: {query}
                Chat History: {chat_history}"""),
            expected_output=dedent("""\
                NLP analysis result identifying key legal concepts and context."""),
            async_execution=True,
            agent=agent
        )

    def search_algorithm_task(self, agent, query, chat_history=None):
        return Task(
            description=dedent(f"""\
                Develop and execute search algorithms to efficiently find relevant
                legal information on the web based on the input query. Utilize
                search engines effectively and filter results for accuracy
                and reliability.

                Query: {query}
                Chat History: {chat_history}"""),
            expected_output=dedent("""\
                Efficiently retrieved and filtered web search results."""),
            async_execution=True,
            agent=agent
        )

    def legal_analysis_task(self, agent, query, data, chat_history=None):
        return Task(
            description=dedent(f"""\
                Analyze legal documents and statutes to extract relevant information
                and provide accurate answers to the legal query. Summarize,
                analyze citations, and cross-reference information.

                Query: {query}
                Legal Data: {data}
                Chat History: {chat_history}"""),
            expected_output=dedent("""\
                Accurate legal analysis and answer to the query."""),
            async_execution=True,
            agent=agent
        )

    def quality_assurance_task(self, agent, answer):
        return Task(
            description=dedent(f"""\
                Verify the accuracy and reliability of the provided legal answer.
                Conduct fact-checking, validation against authoritative sources,
                and monitor for updates or changes in laws.

                Answer: {answer}"""),
            expected_output=dedent("""\
                Verified and reliable legal answer."""),
            # async_execution=True,
            agent=agent
        )

    def report_generation_task(self, agent, query, answer, chat_history=None):
        return Task(
            description=dedent(f"""\
                Generate a concise report summarizing the legal query, analysis,
                and provided answer. Include references to authoritative sources.

                Query: {query}
                Answer: {answer}
                Chat History: {chat_history}"""),
            expected_output=dedent("""\
                Concise report summarizing the legal query, analysis, and answer."""),
            agent=agent
        )

    def decision_making_task(self, agent, analysis, context):
        return Task(
            description=dedent(f"""\
                Make a decision based on the legal analysis and context of the situation.
                Consider relevant laws, precedents, and ethical implications.

                Analysis: {analysis}
                Context: {context}"""),
            expected_output=dedent("""\
                Well-informed decision regarding the legal matter."""),
            async_execution=True,
            agent=agent
        )
    

    def document_generation_submission_task(self, agent, query, chat_history=None):
        return Task(
            description=dedent(f"""\
                Gather information needed to generate the demanded document using chat history and the query.
                Prompt the user that it's important to enter this information for generating the document.
                
                Query: {query}
                Chat History: {chat_history}"""),
            expected_output=dedent(f"""\
                A simple response to prompt the user to enter this important information without listing those information.
                Just a list of the important information for generating the document."""),
            async_execution=False,
            agent=agent,
        )
    

    def document_generation_task(self, agent, query, chat_history=None):
        return Task(
            description=dedent(f"""\
                Generate a legal letter based on the user's recent query and chat history. 
                First, prompt the user for any additional necessary information. 
                Then, extract the relevant details and use them to create the letter.

                Query: {query}
                Chat History: {chat_history}"""),
            expected_output=dedent("""\
                The generated legal letter based on the provided and extracted information."""),
            async_execution=False,
            agent=agent,
        )

    def check_information_task(self, agent, query, chat_history=None):
        return Task(
            description=dedent(f"""\
                Check if all necessary information for creating the document is available based on the user's recent query and chat history. 
                Return a boolean indicating whether the information is complete (True) or if there are any missing details (False).

                Query: {query}
                Chat History: {chat_history}"""),
            expected_output=dedent("""\
                Boolean indicating whether is all necessary information is available or not."""),
            async_execution=False,
            agent=agent,
        )

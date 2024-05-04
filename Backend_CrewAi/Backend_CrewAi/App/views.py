from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from crewai import Crew
from .tasks import LegalQueryTasks
from .agents import LegalQueryAgents

@csrf_exempt
def legal_query_view(request):
    print(request.POST)
    if request.method == 'POST':
        print(request.POST)
        query = request.POST.get('query', '')  
        if not query:
            return JsonResponse({'error': 'No query provided'}, status=400)
        
        try:
            tasks = LegalQueryTasks()
            agents = LegalQueryAgents()

            # Create Agents
            data_gathering_agent = agents.data_gathering_agent()
            nlp_agent = agents.natural_language_processing_agent()
            search_algorithm_agent = agents.search_algorithm_agent()
            legal_analysis_agent = agents.legal_analysis_agent()
            quality_assurance_agent = agents.quality_assurance_agent()
            report_generation_agent = agents.report_generation_agent()

            # Create Tasks
            data_gathering = tasks.data_gathering_task(data_gathering_agent, query)
            nlp_processing = tasks.natural_language_processing_task(nlp_agent, query)
            search_algorithm = tasks.search_algorithm_task(search_algorithm_agent, query)
            legal_analysis = tasks.legal_analysis_task(legal_analysis_agent, query, data_gathering.expected_output)
            quality_assurance = tasks.quality_assurance_task(quality_assurance_agent, legal_analysis.expected_output)
            report_generation = tasks.report_generation_task(report_generation_agent, query, legal_analysis.expected_output)

            # Set up task context
            legal_analysis.context = [data_gathering]
            quality_assurance.context = [legal_analysis]
            report_generation.context = [legal_analysis, quality_assurance]

            # Create Crew responsible for Legal Query
            crew = Crew(
                agents=[
                    data_gathering_agent,
                    nlp_agent,
                    search_algorithm_agent,
                    legal_analysis_agent,
                    quality_assurance_agent,
                    report_generation_agent,
                ],
                tasks=[
                    data_gathering,
                    nlp_processing,
                    search_algorithm,
                    legal_analysis,
                    quality_assurance,
                    report_generation,
                ]
            )

            # Start the crew's activities
            game = crew.kickoff()

            # Return results
            return JsonResponse({'result': str(game)})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
